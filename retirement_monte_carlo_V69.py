#!/usr/bin/env python3
"""Household retirement simulation. Run --help for usage and limitations."""
import argparse,csv,hashlib,json,math,sys
from pathlib import Path
import numpy as np
import openpyxl

N=10000; SEED=642032
# IRS Uniform Lifetime Table: ages 72-120 (divisors for ages used are 78-99).
DIV=[27.4,26.5,25.5,24.6,23.7,22.9,22.0,21.1,20.2,19.4,18.5,17.7,16.8,16.0,15.2,14.4,13.7,12.9,12.2,11.5,10.8,10.1,9.5,8.9,8.4,7.8,7.3,6.8,6.4,6.0,5.6,5.2,4.9,4.6,4.3,4.1,3.9,3.7,3.5,3.4,3.3,3.1,3.0,2.9,2.8,2.7,2.5,2.3,2.0]
def div(age):
 if age<72 or age>120: raise ValueError(f'Age {age} outside divisor table')
 return DIV[age-72]
def compound_factor(target, sigma, z):
 # Lognormal gross return has median 1+target, so annual log return
 # averages log(1+target); solve for its log variance to retain the
 # specified standard deviation of simple annual returns exactly.
 g=1+target
 if g<=0 or sigma<0: raise ValueError('Invalid compound return or volatility')
 mean2=0.5*g*g*(1+math.sqrt(1+4*(sigma/g)**2))
 logvar=math.log(mean2/(g*g))
 return np.exp(math.log(g)+math.sqrt(logvar)*z)
def number(ws,cell):
 v=ws[cell].value
 if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v): raise ValueError(f'Missing calculated numeric value: {ws.title}!{cell} ({v!r}). Recalculate workbook in Excel first.')
 return float(v)
def tax(ss,other,year,joint,inf,ded):
 # Same simplified federal / CA retirement tax formula as the workbook.
 # Not a tax return calculator; highest modeled federal marginal bracket is 24%.
 f=(1+inf)**(year-2032); mult=1 if joint else .5
 lo,hi,extra=(32000,44000,6000) if joint else (25000,34000,4500)
 provisional=other+ss/2
 taxable_ss=np.minimum(.85*ss,.85*np.maximum(0,provisional-hi)+np.minimum(extra,.5*np.maximum(0,provisional-lo)))
 fedbase=np.maximum(0,other+taxable_ss-ded*f*mult)
 federal=.1*fedbase+.02*np.maximum(0,fedbase-28059*mult*f)+.10*np.maximum(0,fedbase-114046*mult*f)+.02*np.maximum(0,fedbase-239180*mult*f)
 ca=np.maximum(0,other-12912*mult*f)
 state=np.maximum(0,.01*ca+.01*np.maximum(0,ca-25070*mult*f)+.02*np.maximum(0,ca-59431*mult*f)+.02*np.maximum(0,ca-93798*mult*f)+.02*np.maximum(0,ca-130207*mult*f)+.013*np.maximum(0,ca-164561*mult*f)-692*mult*f)
 return federal+state

def init_accounts(w,case):
 s=w['Savings Forecast']; cash=w['Cash flow overview']; freq=number(s,'B34');fx=number(s,'B31')
 ira,stock,sipp,deposit=case
 # same mid-year contribution / distribution convention as workbook
 bal=np.array([number(s,'B24'),number(s,'B25'),number(s,'B26'),number(s,'B27'),0.,number(s,'B28'),number(s,'B29')*fx],dtype=float)
 returns=np.array([stock,deposit,ira,ira,stock,stock,sipp]);bal*=np.power(1+returns,freq)
 for y,col in zip(range(2027,2032),'CDEFG'):
  ian=bal[2]/number(s,col+'40');stacey=(bal[3]+bal[4])/number(s,col+'41') if number(s,col+'41') else 0
  trad_rmd=bal[4]/number(s,col+'41') if number(s,col+'41') else 0
  ira_rmd=stacey-trad_rmd
  rmd=ian+stacey
  # Pre-retirement net RMD reinvestment uses workbook modeled annual tax-share approximation.
  share=number(s,col+'43');net=rmd*(1-share)
  flows=np.array([net,number(s,col+'42'),-ian,-ira_rmd,number(s,col+'37')-trad_rmd,number(s,col+'38'),0.])
  bal=bal*(1+returns)+flows*np.sqrt(1+returns)
 # Anchor the working-return scenario to actual workbook balances.
 # Alternative return cases retain the modeled pre-2032 approximation.
 if all(abs(x-y)<1e-12 for x,y in zip(case,(number(s,'E26'),number(s,'E24'),number(s,'E29'),number(s,'E25')))):
  bal=np.array([number(s,c) for c in ['B69','C69','D69','E69','L69','M69','G69']])
 # Trust Cash modeled-interest balance plus separately tracked unallocated Trust cash; neither is a separate account.
 ctp = sum(number(w['Trust Cash savings'], f'B{r}') for r in range(8,38)) if deposit == 0 else number(w['Assets to 2042'],'K6')
 bac=number(w['BAC RSU Stock'],'B3')*(1+stock)**freq
 for r in range(11,16):bac=bac*(1+stock)+number(w['BAC RSU Stock'],f'F{r}')*math.sqrt(1+stock)
 if all(abs(x-y)<1e-12 for x,y in zip(case,(number(s,'E26'),number(s,'E24'),number(s,'E29'),number(s,'E25')))): bac=number(w['BAC RSU Stock'],'H15')
 return np.r_[bal,ctp,bac,number(w['2031 Account Ledger'],'M94')]

def initialize_variable_paths(w,case,n,rng,history=None):
 """Project 2027-31 from 2026 balances, with path-dependent RMDs.

 Employer pay, pensions, budget and deposit transfers remain deterministic.
 RMD taxes use the workbook's year-specific approximate effective tax share.
 """
 s=w['Savings Forecast'];ira,stock,sipp,deposit=case;freq=number(s,'B34');fx=number(s,'B31')
 returns=np.array([stock,deposit,ira,ira,stock,stock,sipp])
 initial=np.array([number(s,'B24'),number(s,'B25'),number(s,'B26'),number(s,'B27'),0.,number(s,'B28'),number(s,'B29')*fx])
 bal=np.tile(initial*np.power(1+returns,freq),(n,1))
 bac=np.full(n,number(w['BAC RSU Stock'],'B3')*(1+stock)**freq)
 bac_return=number(w['BAC RSU Stock'],'B4') if abs(ira-number(s,'E26'))<1e-12 and abs(stock-number(s,'E24'))<1e-12 else stock
 for year,col,rsurow in zip(range(2027,2032),'CDEFG',range(11,16)):
  ian=bal[:,2]/number(s,col+'40'); stdiv=number(s,col+'41')
  sr=bal[:,3]/stdiv if stdiv else np.zeros(n); tr=bal[:,4]/stdiv if stdiv else np.zeros(n)
  net=(ian+sr+tr)*(1-number(s,col+'43'))
  flows=np.zeros_like(bal);flows[:,0]=net;flows[:,1]=number(s,col+'42');flows[:,2]=-ian;flows[:,3]=-sr
  flows[:,4]=number(s,col+'37')-tr;flows[:,5]=number(s,col+'38')
  common=rng.standard_normal((n,1));ind=rng.standard_normal((n,5));z=np.sqrt(.7)*common+np.sqrt(.3)*ind
  factors=np.ones_like(bal);factors[:,1]=1+deposit
  for k,(j,mu,sigma) in enumerate([(0,stock,.18),(2,ira,.12),(3,ira,.12),(4,stock,.18),(5,stock,.18)]):
   factors[:,j]=compound_factor(mu,sigma,z[:,k])
  zs=np.sqrt(.7)*common[:,0]+np.sqrt(.3)*rng.standard_normal(n);factors[:,6]=compound_factor(sipp,.18,zs)
  bal=np.maximum(0,bal*factors+flows*np.sqrt(factors))
  zb=np.sqrt(.7)*common[:,0]+np.sqrt(.3)*rng.standard_normal(n);bf=compound_factor(bac_return,.30,zb)
  bac=bac*bf+number(w['BAC RSU Stock'],f'F{rsurow}')*np.sqrt(bf)
  # At each year end include the same categories used by the 2032 start:
  # the modelled surplus ledger and the ledger's unallocated Trust cash.
  # Transition reserves are already included in bal[:,1], not added again.
  if history is not None:
   unallocated=(number(w['2027 Account Ledger'],'M54') if year==2027 else
                number(w['2028 Account Ledger'],'M54') if year==2028 else
                number(w[f'{year} Account Ledger'],'M94'))
   endrow={2027:7,2028:7,2029:13,2030:25,2031:37}[year]
   if endrow==7: surplus=0.0
   elif deposit==0: surplus=sum(number(w['Trust Cash savings'],f'B{r}') for r in range(8,endrow+1))
   else: surplus=number(w['Trust Cash savings'],f'F{endrow}')
   total=bal.sum(axis=1)+bac+surplus+unallocated
   q=np.percentile(total,[10,25,50,75,90])
   history.append({'year':year,'p10':q[0],'p25':q[1],'median':q[2],
                   'p75':q[3],'p90':q[4],'funded_fraction':None})
 ctp=sum(number(w['Trust Cash savings'],f'B{r}') for r in range(8,38)) if deposit==0 else number(w['Assets to 2042'],'K6')
 return np.column_stack((bal,np.full(n,ctp),bac,np.full(n,number(w['2031 Account Ledger'],'M94'))))

def run(w,case,kind,n,seed):
 rng=np.random.default_rng(seed); p=w['Retirement 2032-2042']; s=w['Survivor expense inputs']; rate,stock,sipp,dep=case; inf=number(p,'B4');ded=number(w['2032 Tax & Cash Flow'],'B53')+2*number(w['2032 Tax & Cash Flow'],'B54')
 series=[]; accounts=initialize_variable_paths(w,case,n,rng,series); starting=accounts.sum(axis=1); failed=np.zeros(n,bool)
 if kind=='Ian alone': accounts[:,2]+=accounts[:,3]+accounts[:,4];accounts[:,3:5]=0
 if kind=='Stacey alone': accounts[:,3]+=accounts[:,2];accounts[:,2]=0
 for year in range(2032,2054 if kind!='Ian alone' else 2050):
  joint=kind=='Joint then Stacey' and year<=2049
  if kind=='Joint then Stacey' and year==2050: accounts[:,3]+=accounts[:,2];accounts[:,2]=0
  ai=78+(year-2032); ast=74+(year-2032)
  rmd_i=accounts[:,2]/div(ai) if (joint or kind=='Ian alone') else np.zeros(n)
  rmd_s=(accounts[:,3]+accounts[:,4])/div(ast) if (joint or kind=='Stacey alone' or (kind=='Joint then Stacey' and year>=2050)) else np.zeros(n)
  # Withdraw mandatory amount proportionally from Stacey's traditional balances.
  total=accounts[:,3]+accounts[:,4]; ratio=np.divide(accounts[:,3],total,out=np.zeros(n),where=total>0)
  accounts[:,2]-=rmd_i;accounts[:,3]-=rmd_s*ratio;accounts[:,4]-=rmd_s*(1-ratio)
  factor=(1+inf)**(year-2032)
  # Follow each workbook annual retirement/survivor schedule through 2042.
  # After the final modeled year, extend its 2042 values with workbook inflation.
  offset=min(year-2032,10); extension=(1+inf)**max(0,year-2042)
  row=(14 if joint else (31 if kind=='Ian alone' else 48))+offset
  ss=(number(p,f'B{row}')+number(p,f'C{row}'))*extension
  uk_income=number(p,f'D{row}')*extension
  spend=number(p,f'P{row}')*extension
  interest=(accounts[:,1]+accounts[:,7])*dep
  rmd=rmd_i+rmd_s;other=uk_income+rmd+interest
  tax0=tax(ss,other,year,joint,inf,ded); budget=ss+other-tax0-spend
  # Positive cash remains in Trust Cash; deficits draw in order.
  accounts[:,7]+=np.maximum(budget,0); need=np.maximum(-budget,0)
  for j in [7,9,1,0,8,5]:
   take=np.minimum(accounts[:,j],need);accounts[:,j]-=take;need-=take
  # Extra traditional/SIPP withdrawals are taxable; solve gross amount iteratively.
  taxable_extra=np.zeros(n)
  for j in [2,3,4,6]:
   available=accounts[:,j];lo=np.zeros(n);hi=available.copy()
   for _ in range(32):
    mid=(lo+hi)/2; marginal=tax(ss,other+taxable_extra+mid,year,joint,inf,ded)-tax(ss,other+taxable_extra,year,joint,inf,ded)
    enough=mid-marginal>=need;hi=np.where(enough,mid,hi);lo=np.where(enough,lo,mid)
   marginal=tax(ss,other+taxable_extra+hi,year,joint,inf,ded)-tax(ss,other+taxable_extra,year,joint,inf,ded)
   accounts[:,j]-=hi;need=np.maximum(0,need-(hi-marginal));taxable_extra+=hi
  failed|=need>0.01
  # Lognormal factors calibrated to each account's compound rate and volatility;
  # common shock accounts for 70% of each pair's correlation.
  common=rng.standard_normal((n,1));independent=rng.standard_normal((n,5));z=np.sqrt(.7)*common+np.sqrt(.3)*independent
  for k,(j,mu,sigma) in enumerate([(0,stock,.18),(2,rate,.12),(3,rate,.12),(4,stock,.18),(5,stock,.18)]):
   accounts[:,j]*=compound_factor(mu,sigma,z[:,k])
  # BAC stock: 30% annual volatility, correlated with market shock.
  bac_return=number(w['BAC RSU Stock'],'B4') if abs(rate-number(w['Savings Forecast'],'E26'))<1e-12 and abs(stock-number(w['Savings Forecast'],'E24'))<1e-12 else stock
  zb=np.sqrt(.7)*common[:,0]+np.sqrt(.3)*rng.standard_normal(n);accounts[:,8]*=compound_factor(bac_return,.30,zb)
  # SIPP uses an independent idiosyncratic shock plus the shared shock.
  zs=np.sqrt(.7)*common[:,0]+np.sqrt(.3)*rng.standard_normal(n);accounts[:,6]*=compound_factor(sipp,.18,zs)
  # Deposit interest has already entered cash income; do not add it a second time.
  total=np.sum(accounts,axis=1);q=np.percentile(total,[10,25,50,75,90]);series.append({'year':year,'p10':q[0],'p25':q[1],'median':q[2],'p75':q[3],'p90':q[4],'funded_fraction':float(np.mean(~failed))})
 return series,starting

def validate_tax(w):
 p=w['Retirement 2032-2042'];inf=number(p,'B4');ded=number(w['2032 Tax & Cash Flow'],'B53')+2*number(w['2032 Tax & Cash Flow'],'B54')
 for r,joint in [(14,True),(31,False),(48,False)]:
  ss=number(p,f'B{r}')+number(p,f'C{r}');other=sum(number(p,f'{col}{r}') for col in ['D','J','K','L','AA'])
  got=float(tax(ss,other,2032,joint,inf,ded)); expected=number(p,f'AE{r}')+number(p,f'AF{r}')
  if abs(got-expected)>0.02:raise ValueError(f'Tax model does not reconcile for row {r}: {got:.2f} vs {expected:.2f}. Workbook model may have changed.')

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('workbook',type=Path);ap.add_argument('--output',type=Path,default=Path('simulation_results'));ap.add_argument('--paths',type=int,default=N);ap.add_argument('--seed',type=int,default=SEED);args=ap.parse_args()
 if args.paths<1:ap.error('--paths must be positive')
 w=openpyxl.load_workbook(args.workbook,data_only=True);validate_tax(w)
 s=w['Savings Forecast'];cases={'working':(number(s,'E26'),number(s,'E24'),number(s,'E29'),number(s,'E25')),'lower':(.06,.065,.06,.0384),'6 percent':(.06,.06,.06,.0384),'5 percent':(.05,.05,.05,.0384),'0 percent':(0.,0.,0.,0.)};args.output.mkdir(parents=True,exist_ok=True)
 results=[];starting_rows=[]
 for case,assumptions in cases.items():
  for i,kind in enumerate(['Joint then Stacey','Ian alone','Stacey alone']):
   print('Running',case,kind,flush=True);rows,starting=run(w,assumptions,kind,args.paths,args.seed+i)
   q=np.percentile(starting,[10,25,50,75,90]);starting_rows.append(dict(case=case,scenario=kind,p10=q[0],p25=q[1],median=q[2],p75=q[3],p90=q[4]))
   for row in rows:results.append({'case':case,'scenario':kind,**{k:float(v) if isinstance(v,np.floating) else v for k,v in row.items()}})
 with (args.output/'fan_data.csv').open('w',newline='') as f:
  wr=csv.DictWriter(f,fieldnames=list(results[0]));wr.writeheader();wr.writerows(results)
 with (args.output/'starting_2032.csv').open('w',newline='') as f:
  wr=csv.DictWriter(f,fieldnames=list(starting_rows[0]));wr.writeheader();wr.writerows(starting_rows)
 metadata={'workbook':args.workbook.name,'workbook_sha256':hashlib.sha256(args.workbook.read_bytes()).hexdigest(),'paths_per_scenario':args.paths,'seed':args.seed,'return_basis':'geometric (compound) targets, lognormal annual returns','random_returns_start':2027,'pre_2032_snapshots':'Year-end modeled accounts plus the workbook surplus ledger and unallocated Trust cash. Transition reserve is already included in deposit.','pre_2032_rmd_tax':'Year-specific workbook effective RMD tax-share approximation; not a full path-by-path tax return','pre_2032_income_and_expense':'Fixed forecast; 2027–2031 cash shortfalls and unexpected events are not simulated','method':'Pre-retirement RMDs and reinvestment depend on path balances; survivor scenarios apply from 2032. Annual pension and spending values follow workbook 2032–2042 schedules including modeled healthcare, then grow at workbook inflation.'}
 (args.output/'run_metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
 for case in cases:
  for kind in ['Joint then Stacey','Ian alone','Stacey alone']:
   final=[r for r in results if r['case']==case and r['scenario']==kind][-1];print(case,kind,f"funded={100*final['funded_fraction']:.2f}%",f"median=${final['median']:,.0f}")
if __name__=='__main__':main()
