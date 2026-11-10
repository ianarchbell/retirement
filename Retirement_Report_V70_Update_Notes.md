# V69 update: IRA mix and Monte Carlo

The financial master is `Retirement_Plan_V69.xlsx`. The full single-document V69 report has been updated for the IRA allocation, revised forecast, Monte Carlo results and the approved combined crash-test page.

- IRA allocation and long-run return: `Savings Forecast` B32–B33 and E24/E26. Retirement forecast links to this working return.
- Annual Monte Carlo output, including 2027–2031: `MC annual 2027+`. All original Monte Carlo snapshot tables and their chart caches were refreshed after the IRA mix changed.
- Crash-test inputs, scenarios, output and limitations: `Market stress inputs`. The stress routine uses the allocation and Treasury rate from `Savings Forecast`; refer to workbook cells for numerical assumptions.
- Run the base simulation from `retirement_monte_carlo_V69.py` and the stress test from `stress_analysis.py` after financial inputs change. These are snapshots, not automatically recalculating results. Refresh workbook outputs and charts after rerunning. The stress routine reads the workbook inputs and uses the base code.
- Before producing the report page, reconcile it with the latest workbook results. Distinguish 10th-percentile asset paths from withdrawals, and identify the joint-to-survivor timing. The stress model treats brokerage, 401(k), SIPP and BAC as equity, matching the existing simulation, but their actual holdings have not been verified. Its pre-2032 cash forecast is fixed except for path-dependent RMD reinvestment.
- The workbook contains linked iterative calculations. In this update the working file was recalculated repeatedly until two successive runs agreed within one cent, and account-ledger and retirement tax checks passed. Revalidate convergence after changes.


## V69 report assembly and refresh — 9 November 2026

- The approved joint Monte Carlo and crash-test sample replaces report page 13. Its scenario summary, annual percentile chart and cash stress inputs are mapped to workbook sources in `Report source map`, including the V69 additions at the end of that sheet. Ages use the workbook healthcare age inputs.
- Refreshed the affected cash flow, retirement, survivor and investment figures, return assumptions, 2027 monthly scenario, tax and annual reconciliation, account diagrams and 2028–2032 ledger extracts. The original designs, page order, bridges and the appendix structure remain in place.
- Rebuilt the survivor Monte Carlo bands from the current workbook snapshots. The charts retain their prior axes, colors and scenario definitions. Refreshed labels in the embedded waterfall and surplus charts from the current source values.
- Checked the full report visually at page level, plus selected charts in detail. Compared 579 entries on the principal cash-flow, retirement, survivor, investment and purchasing-power tables with the workbook; all matched at displayed rounding. Checked 1,099 selected later-ledger entries: all agreed except two unchanged half-dollar property-tax ties, which retain the prior report's rounding. Checked 198 entries in the tax, reconciliation and savings tables against their sources. This checks report presentation against workbook data; it is not an independent audit of the model.
- Page 4's previously clipped explanatory sentence about Trust Cash interest was restored. Page 13 was rebuilt as vector text and graphics, so the approved page does not contain the prior sample's hidden obsolete text. All 54 pages use the V69 footer; existing page references and Appendix A–T order were retained.
- Reproduction scripts and their limitations are saved in `Retirement_Report_V69_Refresh_Tools.zip`. They capture the V68-to-V69 assembly and are not a one-click updater for later changes.
- Future refresh: use the workbook's `Report source map` and page crosswalk. `MC annual 2027+` and `Market stress inputs` are fixed simulation snapshots; rerun both simulation scripts when their inputs change, then refresh page 13 and the survivor charts. Do not use the older V68 or V69 draft samples as the financial source.


---

# Retirement report V68 — practical update guide

Checkpoint: 9 November 2026. This guide records page-by-page actions and progress. The workbook holds the source map and financial details.

## Authoritative files

- [Design master: Retirement_Plan_V6.pdf](https://chatgpt.com/library?file_id=libfile_e70e19fa591c819190ad3eb8242894ee&account_id=personal)
- [Financial master: Retirement_Plan_V68.xlsx](https://chatgpt.com/library?file_id=libfile_686f64f5dd4c8191b8b4585855f45920&account_id=personal)
- [Report in progress](https://chatgpt.com/library?file_id=libfile_f75f1315f69081919b3169491f891f56&account_id=personal)

The workbook is the financial authority. The PDF is the visual authority for layout and graphics. All original pages 1–50 have been updated in the working report; Appendix O on pages 51–55 contains selected ledger extracts. This is not a finished or approved report. The page instructions below are an update guide, not a claim that all pages have been verified.

## Fast update procedure

1. Open the latest workbook and latest working report; confirm their versions. Find changed inputs or outputs and use the page index below and the workbook’s Report source map to identify affected report items. The workbook’s Report source map is the single source for report-to-workbook references.
2. Recalculate or confirm the workbook’s cached results and check relevant formulas and control totals. Keep financial calculations and assumptions in the workbook. If a value or assumption cannot be traced, flag it instead of inventing or carrying it forward.
3. Update every affected table, chart, label, summary, commentary and cross-reference. Preserve the original design, including waterfalls and graphics; ask Ian before redesigning a page. Use the corrected Monte Carlo snapshots and workbook survivor assumptions. Keep contingency examples outside the forecast.
4. For each affected page compare displayed numbers and units to the mapped cells, check the period, signs and rounding, and inspect the rendered page. Verify related repeated values elsewhere. Do not remove NOT UPDATED until a page is updated and checked.
5. Keep report and workbook version labels aligned; for this version use “Our Retirement Plan V68” as the consistent footer. Record changed pages, workbook version and unresolved issues at the next checkpoint.

**Important:** the report is manually edited; no complete automatic updater has been saved. Use the current workbook’s Report source map for sheet and cell references. A mapped source still needs to be checked against the displayed figure and its meaning.

## Page-by-page instructions

### Page 1 — EXECUTIVE SUMMARY / Our six-year plan and the retirement that follows / Stacey’s Career Transition Plan takes us through 2031 to full joint retirement in 2032, while we complete the renovation and continue to save.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the executive-summary figures and accompanying narrative, including 2032 surplus and investments, reserve, renovation, and age-95 test. Preserve the existing summary layout.

### Page 2 — ANNUAL SURPLUS / Calendar-year totals include tax and the estimated interest on CTP cash. The 2029 amount includes the benefit of the reserve used in January-June. / before the next July payment.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the annual surplus bars, labels and commentary. Use full-year 2029 rather than either half-year alone; explain reserve funding separately.

### Page 3 — Annual household cash after taxes, spending and planned savings / 3 / WHY CASH SURPLUS CHANGES

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh both waterfall charts, their bar labels and commentary from the cash-surplus bridge. Explain planned savings versus cash surplus; retain the existing two-chart design.

### Page 4 — INCOME CHANGES | 2026 TO 2027 / The first CTP employment year / Lower compensation is offset in part by the start of Stacey's pensions, lower tax and changes in payroll deductions. Net RMD proceeds are saved rather than spent. This

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the 2026–27 income waterfall, labels and explanatory text from the Comparison sheet; preserve its chart structure.

### Page 5 — INCOME CHANGES | 2028 TO 2029 / From salary to an annual payment / even though the first CTP cash does not arrive until July.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the 2028–29 income waterfall, labels and explanatory text from the workbook waterfall source; retain the two-period basis.

### Page 6 — INCOME CHANGES | 2031 TO 2032 / After the final CTP payment / household spending budget is assessed separately.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the 2031–32 income waterfall, labels and commentary from the workbook waterfall source; preserve the graphic.

### Page 7 — CASH FLOW / The transition to retirement / 7

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh all income, tax, spending, savings and surplus rows and totals. Respect the two 2029 half-year columns and do not count RSUs as spendable income.

### Page 8 — HOUSEHOLD EXPENSES / Our monthly household budget / Monthly averages for each year; 2029 is split into January-June and July-December.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh monthly household spending totals and categories for each displayed period; preserve the 2029 split and table.

### Page 9 — HOUSEHOLD EXPENSES / Our 2027 spending choices / Monthly averages in 2027 dollars | Both of us | Provisional classification

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh each 2027 spending-choice amount and the subtotal and total from the report support table. Preserve classification and layout.

### Page 10 — HOUSEHOLD EXPENSES / Our 2032 spending choices / Monthly averages in 2032 dollars | Both of us | Provisional classification

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh each 2032 spending-choice amount and the subtotal and total from the report support table. Preserve classification and layout.

### Page 11 — FULL RETIREMENT / Income and expenses through 2042 / IN 2026 PURCHASING POWER

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the 2032–2042 retirement income, spending and surplus table and purchasing-power commentary; retain stated units and base-year basis.

### Page 12 — INDIVIDUAL SCENARIOS / If one of us is living alone / Separate illustrations assume one spouse is alive from January 2032, with ownership of the traditional

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the individual survivor illustrations using the workbook survivor income and expense assumptions; do not substitute independent assumptions.

### Page 13 — INDIVIDUAL SCENARIOS / Living alone: income and spending through 2042 / Separate illustrations assume the other spouse has died before 2032. Amounts are annual future dollars.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh both survivor tables through 2042, their labels, time horizon and relevant commentary; keep each person’s scenario distinct.

### Page 14 — SAVINGS / Investment accounts from 2026 to 2042 / Starting balances, then modeled year-end balances. SIPP shown in US dollars at $1.30 per £1.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh starting balances and each investment-account projection and chart through 2042. Check year-end versus starting balances and USD conversions.

### Page 15 — OUR HOME / Home value and renovation / Starting at $1.45 million in 2026, the home is projected to appreciate by 4% a year. At the end of 2028, a $200,000 estimated renovation uplift is added to the then-current

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh home value, renovation and HELOC commentary and numbers, distinguishing forecast cost from financing and interest.

### Page 16 — PENSIONS AND OVERALL PICTURE / Three sources of financial value / Illustrative 2032 values: investment accounts and home equity at year-end; pension value at the start of the year.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the three 2032 financial-value components and graphics. Distinguish projected home and pension values from liquid investment balances.

### Page 17 — TESTING THE PLAN / Monte Carlo through age 95 / 10,000 paths per scenario | Funded means spending and tax are met without using the home.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh Monte Carlo outcome labels, values and explanatory text using the corrected workbook snapshots. Preserve chart layout and scenario definitions.

### Page 18 — TESTING THE PLAN / If one of us is living alone / 5% compound investment target | 10,000 paths | Through age 95

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh both survivor Monte Carlo results from the current workbook snapshots and use its survivor assumptions; preserve scenario labels.

### Page 19 — PUTTING THE PLAN INTO PRACTICE / How we manage the plan / Use our existing accounts, keep the transition reserve separate and review progress regularly.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Update regular and January transition reserve contributions, the 2027/2028 monthly allocation table, total and operational commentary. Make Trust-to-Joint funding of scheduled payments visible and do not double-count transfers as spending. Verify each allocation against both annual ledgers.

### Page 20 — OUR PLAN / 2032 HOUSEHOLD BUDGET / After income tax and household spending

**Status:** Updated in working report; recheck when inputs change.

**Action:** Update the summary cards and notes for 2032 spending, cash surplus, investments and other claims. Keep the Medicare work-stoppage relief prompt and verify all Monte Carlo commentary against the snapshot.

### Page 21 — OUR TRANSITION / How cash flows change / Monthly averages; annual figures are divided by 12 and 2029 periods by six. January 2027 is exceptional.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the transition table and supporting text for 2027, 2028, each half of 2029 and 2032. The current table uses the workbook’s monthly figures before deposit interest and related tax; distinguish existing savings funding from income and retain that basis unless the workbook provides an interest-inclusive monthly table.

### Page 22 — OUR RETIREMENT PLAN / How money moves between our accounts / 2026 expense base | Normal February income | HELOC and reserve as planned

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the 2027 money-movement diagram, amounts, arrows and commentary using the mapped account-flow and diagram sources and the ledger. Make January exceptions and Trust-to-Joint support clear; UK money is reserved for travel/carers.

### Page 23 — OUR RETIREMENT PLAN / 2026 expense base | Normal February income | HELOC and reserve as planned / JOINT ACCOUNT

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the 2027 account-by-account table, individual Bills items, allocations, transfers and January exceptions. Check against the ledger and mapped diagram sources, not the obsolete values on this page.

### Page 24 — SUPPORTING MATERIAL / Guide to the appendices / Use these pages to check the calculations, assumptions and detail behind the main report.

**Status:** Updated in working report; recheck if pagination changes.

**Action:** Refresh the appendix guide and page references if content or pagination changes; no financial figures should be invented.

### Page 25 — Assumptions and items to refine / Assumption / Treatment

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the assumptions and refinements table from the mapped workbook inputs. Flag any statement for which no current workbook assumption can be found.

### Page 26 — Inputs, units and annual increases - 1 of 3 / Monthly and annual bill inputs are separate. A dash means that input column is unused; explicit $0 means a zero budget. Rates apply to the stated base year unless noted. / Expense / base input

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the first block of expense inputs, units, annual increases and notes from the mapped Expense Inputs rows.

### Page 27 — Inputs, units and annual increases - 2 of 3 / Monthly and annual bill inputs are separate. A dash means that input column is unused; explicit $0 means a zero budget. Rates apply to the stated base year unless noted. / Expense / base input

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the second block of expense inputs, units, annual increases and notes from the mapped Expense Inputs rows.

### Page 28 — Inputs, units and annual increases - 3 of 3 / Monthly and annual bill inputs are separate. A dash means that input column is unused; explicit $0 means a zero budget. Rates apply to the stated base year unless noted. / Expense / base input

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the third block of expense inputs, units, annual increases and notes from the mapped Expense Inputs rows.

### Page 29 — The controls behind the expense forecast / Control / Active treatment

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh expense-control assumptions and timing from the workbook. Keep building, HELOC and reserve treatment aligned with their sources.

### Page 30 — Individual household expenses / Expense / 2026

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the first section of itemised expense table for all periods using the mapped Expense Detail rows and correct monthly basis.

### Page 31 — Individual household expenses (continued) / Monthly averages in each period. These are the individual expense lines from the workbook; group subtotals reconcile to the household spending total. / Expense

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the second section of itemised expense table for all periods using the mapped Expense Detail rows and correct monthly basis.

### Page 32 — Individual household expenses (continued) / Monthly averages in each period. These are the individual expense lines from the workbook; group subtotals reconcile to the household spending total. / Expense

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the final section of itemised expense table for all periods using the mapped Expense Detail rows and correct monthly basis.

### Page 33 — How the joint tax provision is calculated / Annual USD / 2026

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the joint tax provision table from each annual tax sheet and its mapped cells. Preserve annual basis and show tax provisions consistently with workbook.

### Page 34 — Annual USD; 2029 is split to make the reserve and the July payment visible. / Annual amount / 2026

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the annual cash-flow table from Cash flow overview. Keep 2029 split and interest and associated tax treatment consistent.

### Page 35 — Company deductions and separate vesting / 2027 benefit deduction / Per period

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh company deductions, payroll and separate RSU vesting from the mapped payroll and stock sheets. Keep investment vesting distinct from spendable income.

### Page 36 — Starting accounts and return assumptions / Balances provided for the 2026 starting point; modeled annual nominal returns. / The SIPP is converted at $1.30 per £1. The existing deposit earns 3.84% in every case.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh starting account balances and return assumptions using Savings Forecast and Account overview; verify balances and reporting date.

### Page 37 — The same forecast in 2026 purchasing power / Year / Gross income

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the same forecast in 2026 purchasing power using the mapped workbook outputs; preserve its base-year and units.

### Page 38 — How we save through the transition / savings and includes deposit interest and its tax. / Monthly average

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh transition savings and reserve build by year from the mapped workbook outputs. Distinguish planned savings, cash surplus and earmarked reserves.

### Page 39 — How the transition reserve is used / Monthly cash timing: pensions continue; the first CTP payment arrives on 1 July. / THE RESERVE BEFORE JULY

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the reserve-use schedule and CTP timing, including the pre-payment period and first July payment; use the workbook timing rather than an assumed monthly salary.

### Page 40 — 2027 income and essential outgoings / ITEM  |  USD / JAN

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the 2027 month-by-month income and essential-outgoings table, including annual totals, from Cash Flow 2027.

### Page 41 — 2027 expenses and HELOC float / Continued: individual budget lines, including planned savings; amounts in parentheses indicate a shortfall. / ITEM  |  USD

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the remaining 2027 monthly expense, HELOC and savings rows and annual totals from Cash Flow 2027; keep transfers and expenses distinct.

### Page 42 — HELOC repayment and building schedule / Illustrative monthly cash timing | interest paid separately | $52,000 of building work in 2027 / PEAK 2027 BALANCE

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh monthly HELOC repayment, interest and building schedule from HELOC and Building and the 2027/2028 ledgers. Reconcile opening and ending balances and timing.

### Page 43 — APPENDIX M | CONTINGENCY PLANNING / Contingencies to revisit together / For a future review. The amounts below are proposed stress-test inputs and reserve targets. The base forecast continues to use its current assumptions.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Keep the contingency discussion as examples for future discussion, not as forecast assumptions. Flag any financial assertion that appears to be part of the forecast but lacks a workbook source.

### Page 44 — APPENDIX N | ACCOUNT FLOWS / 2028 | How money moves between accounts / Monthly averages in projected dollars. Transfers marked proposed need agreement before autopay.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the 2028 account-flow diagram and notes from the mapped account-flow and diagram tables; show scheduled Trust support, reserve and actual cash routing.

### Page 45 — APPENDIX N | ACCOUNT FLOWS / 2028 | Account-by-account monthly budget / Individual expenses and proposed transfers; projected monthly averages, not instructions to banks.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the 2028 detailed account budgets, individual Bills expenses, Trust allocations and other-account flows from mapped sources and 2028 ledger.

### Page 46 — APPENDIX N | ACCOUNT FLOWS / 2029 | How money moves between accounts / Monthly averages in projected dollars. Transfers marked proposed need agreement before autopay.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the 2029 account-flow diagram, distinguishing January–June reserve support from the July lump-sum CTP payment and its subsequent use.

### Page 47 — APPENDIX N | ACCOUNT FLOWS / 2029 | Account-by-account monthly budget | January-June / Individual expenses and proposed transfers; projected monthly averages, not instructions to banks.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the January–June 2029 account-by-account table using 2029 ledger and mapped sources. Preserve its half-year basis and reserve treatment.

### Page 48 — APPENDIX N | ACCOUNT FLOWS / 2029 | Account-by-account monthly budget | July-December / Individual expenses and proposed transfers; projected monthly averages, not instructions to banks.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the July–December 2029 account-by-account table using 2029 ledger and mapped sources. Distinguish a monthly average from the actual July lump-sum timing.

### Page 49 — APPENDIX N | ACCOUNT FLOWS / 2032 | How money moves between accounts / Monthly averages in projected dollars. Transfers marked proposed need agreement before autopay.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the 2032 money-movement diagram, income, RMDs, transfers and Trust/Bills routing from 2032 mapped sources. Do not treat RMDs as additional income on top of their existing source.

### Page 50 — APPENDIX N | ACCOUNT FLOWS / 2032 | Account-by-account monthly budget / Individual expenses and proposed transfers; projected monthly averages, not instructions to banks.

**Status:** Updated in working report; recheck when inputs change.

**Action:** Refresh the 2032 account-by-account table, Bills details, RMD allocations, Trust transfers and other accounts using the 2032 ledger and mapped sources.

## Known open work at this checkpoint

- The original 50 pages have been updated, but the report is not complete: verify figures and appearance page by page, resolve outstanding source issues, and decide whether Appendix O needs more ledger detail.
- Page 19 was updated using the 2027 and 2028 account ledgers, including January reserve funding and Trust-to-Joint support; recheck it if those ledgers change.
- Page 21 uses the workbook’s before-interest monthly table; the report explicitly identifies that basis and points to the interest-inclusive figures on pages 1 and 20.
- Check each mapped item in context. A sheet or range in the workbook map may require further item-level tracing; record any real gap in the workbook.
- Add a new appendix for the later-years account ledgers, using the workbook as the source. The existing appendix on pages 44–50 contains account-flow diagrams and account-by-account summaries for 2028, 2029 and 2032; do not assume these replace the additional ledger appendix. Determine the years, level of ledger detail, pagination and design from the workbook and earlier agreed guidance; flag any unresolved scope or design choice. Update the appendix guide and cross-references.
- Add material introduced since the design master in the appropriate existing design, and verify report figures and appearance page by page before issuing a completed report.

Checkpoint: report version 9. Updated pages 22, 25–39, 43–44, 46 and 49; the remaining original pages retain their NOT UPDATED markers. The later-years ledger appendix has not been added.

Checkpoint: report version 10; page 37 purchasing-power table refreshed from the workbook.

Checkpoint: report version 11; page 36 contribution assumptions and workbook reference refreshed.

Checkpoint: report version 12. Pages 30–32 expense tables and page 35 benefits/RSUs updated; page 32 states its listed expenses are selected lines and its subtotal includes additional workbook items. Additional itemized detail remains to be included when the appendix is completed.

Checkpoint: report version 13; pages 26–29 expense assumptions and controls updated.

Checkpoint: report version 14; page 25 planning assumptions and page 33 tax table updated. Page 33 tax amounts exclude incremental Trust Cash interest and its tax.

Page 42 needs an explicit source decision when updating: HELOC and Building shows a 2027 closing balance of $28,050, while the 2027 Account Ledger closes at $27,699.42 after additional property-tax borrowing and repayments. The 2028 schedule opens from the ledger. Use the account ledger to show the complete account movement and retain the building-only scenario as such; do not silently mix the two.

Checkpoint: report version 15. Page 42 distinguishes the 2027 building-only schedule from the full account-ledger closing balance, and uses the ledger opening for 2028.

Checkpoint: report version 16. Page 40 refreshed using Cash Flow 2027, the account ledger and workbook deposit-interest outputs. It flags that the monthly scenario has no existing-savings transfer while the annual overview has $100.

Checkpoint: report version 17. Page 41 refreshed directly from 2027 Monthly Scenario; it identifies the scenario timing and uses its own cash summary.

Checkpoint: report version 18. Added Appendix O, pages 51–55, with selected monthly account-ledger movements for 2028–2032, and updated page 24. These are explicitly labelled extracts; the workbook remains the complete ledger. Check whether additional detailed rows are wanted when the whole report is reviewed.

Checkpoint: report version 19. Page 45 updated from the 2028 account flow map and Bills details, including Trust-to-Joint support and the complete mapped Bills list.

Checkpoint: report version 20. Pages 47–48 and 50 updated using period-specific account-flow sources and itemized Bills rows. Page 23 is the remaining original page marked NOT UPDATED. Whole-report verification and complete ledger detail remain outstanding.

Checkpoint: report version 21. Page 23 refreshed from the February 2027 account ledger, Bills input details and January payroll estimate. No original page remains marked NOT UPDATED. Whole-report verification remains outstanding; Appendix O is selected ledger extracts, not the complete ledgers.

Checkpoint: report version 22. Page 41 now flags that its scenario summary uses property-tax reserve funding while page 40 displays payment dates. Visual contact sheets were inspected; a full page-by-page figure audit has not been completed.

## Review checkpoint — report version 23, 9 November 2026

- Compared the 50 original pages visually against the design master using side-by-side rendered pages and inspected an overview of the five added ledger extracts. The original page dimensions and broad layouts are retained, including the paired page 3 waterfalls and the account-flow diagrams. Chart data and some internal account-table content were rebuilt; these pages are not pixel-identical to the master.
- Checked representative workbook outputs: 2032 investment total, cash surplus, pension income, 2029 reserve, 2028 HELOC closing, annual 2027 Trust-to-Joint payments, and the 2032 person-by-person healthcare premiums. The report has not had every figure and chart bar individually checked against its workbook source; do not represent the financial audit as complete.
- Corrected page 19 to say July CTP cash is held in Trust Cash and added to page 25 the 2032 per-person premiums and first modeled year with no IRMAA, 2034. Work-stoppage relief is not assumed by the workbook.
- Readability remains a concern on dense account pages 23, 45, 47–48 and 50, whose body text is smaller than the master. Any layout redesign requires Ian's consent. Pages 51–55 are selected ledger extracts, not complete ledgers; whether they have enough detail remains open.
- PDF integrity: some outdated text remains underneath visual overlays on earlier pages. Page 1, for example, visually shows the current reserve contribution but text extraction also retrieves older figures. Search, copy/paste and machine-reading can therefore return stale data. The affected overlay pages must be cleaned without removing their visible content, then visually and numerically rechecked before the report is final. Do not use PDF text extraction alone as evidence of visible values.
- Page 40 shows actual property-tax payment timing while the page 41 timing scenario uses reserve funding; page 41 explicitly notes this. The annual overview includes $100 existing-savings funding, while the separate monthly scenario does not. Keep the different workbook bases explicit.
- Overall status: still a work in progress. The remaining job is a full item-by-item financial audit, cleanup of underlying obsolete PDF text, readability review at print size, and a decision on complete ledger detail. No final report approval implied.

## PDF cleanup and ledger extracts — report version 24

- Removed the covered obsolete text identified on pages 1–2, including the old $5,100 January reserve contribution, old $27,980 reserve draw, old deposit balances and the covered Preferred Deposit reference. The current visible wording and values remain selectable.
- Compared rendered images of all 55 pages with the source at 100%: all pages were identical except for two antialiased pixels on page 2. A scan of text covered by later opaque shapes or images found no further text spans more than half covered. This is a visual and structural check, not proof that every financial figure has been audited.
- Appendix O, pages 51–55, shows monthly extracts for 2028, 2029, 2030, 2031 and 2032. It is not a complete reproduction of those worksheets.
- The extracts show selected Joint receipts and payments and closing balances; selected Bills income, spending and closing balance; selected Trust Cash transfers and balances; and selected UK account amounts. The 2028 page additionally shows the closing HELOC debt; the 2029–2032 pages show CTP receipts, net RMD available for spending, reserve/Trust transfers and UK cash after travel commitments where applicable.
- Omitted from the extracts are the full monthly individual Bills line items; all personal and grocery-account movements and balances; detailed Trust earmark opening balances, contributions, payments, top-ups and closing balances; the detailed 2028 HELOC draws, principal, interest and temporary-borrowing movements; detailed RMD/tax and Trust-interest calculations; annual totals, source notes, movement checks and the other diagnostic rows. Some of these figures appear as averages elsewhere in the report, but their complete month-by-month detail and checks remain in the workbook.
- The original 50 report pages have been updated, but the item-by-item financial and chart audit remains open. Do not mark the report final solely because the hidden-text cleanup is done.

## Figure and chart audit checkpoint — 9 November 2026

Workbook V68, library version 162; report working PDF version 24. These are source comparisons, not an independent audit of the workbook's assumptions or formulas.

- Checked 3,867 displayed table entries against workbook cells, with no mismatches at displayed rounding: pages 7–14, 30–34, 37–42, 51–55, plus specified Bills/account-table items on pages 23, 45, 47, 48 and 50. The check on each account page covers the extracted mapped items, not every figure on that page. Appendix O accounts for 1,296 of the comparisons.
- Page 3 waterfall labels were compared to Cash surplus bridges; the bridge checks are zero. Pages 4–6 waterfall printed annual and monthly values were compared to the Comparison and 2028/2031 waterfall worksheets. Page 17's 5% joint outcome and 2032 percentile callout were compared to the fixed Monte Carlo snapshot. The plotted Monte Carlo paths/bands still require a complete visual data check, as do remaining chart elements and any figures not covered by the detailed table checks.
- Page 39's timing table and page 42's 2027 building-only and 2028 HELOC tables were checked. The different 2027 building-only and full account-ledger closing balances remain explicitly identified. Page 40 uses payment timing, whereas page 41 uses the separate property-tax reserve timing scenario, as described in the report.
- Still outstanding: finish the individual figure checks for pages not included above (especially assumptions, narrative callouts and remaining account figures), verify each chart including the home chart and Monte Carlo bands and survivor paths, and carry out a final page-by-page check before removing the work-in-progress status. No report edits were made during this checkpoint.

## Completed figure and chart audit — 9 November 2026

- Continued the prior checkpoint against workbook version 162. Checked the remaining displayed assumption inputs, benefits and RSUs, starting balances, summary callouts, 2027 and 2028 account tables, the other-account panels and the 2027, 2028, 2029 and 2032 account diagrams. The automated comparisons total more than 4,000 displayed entries, including the earlier detailed schedules and ledger extracts; repeated displays count separately.
- The home-value bar heights were compared with all seven Home and pension value annual projections, and their displayed values and renovation costs were checked. Cash-surplus and income waterfall labels and their directions were compared with the workbook bridge and waterfall sheets. The 5% joint and both survivor Monte Carlo median lines and all four percentile boundaries were compared across the plotted years with the workbook snapshots; differences were within three pixels at the inspection scale. Simulation table percentages and summary results match Simulation comparison.
- Corrected the page 1 statement that pensions and expenses rise uniformly by 2.5% a year: item-specific workbook assumptions apply. The replacement follows the existing position and typography. No financial assumptions or calculations were added to the report.
- The figure/chart audit checks report presentation against the workbook and snapshots; it does not independently validate the workbook's financial assumptions or formulas. The report continues to identify the 2027 monthly scenario versus annual overview differences, and distinguishes the building-only HELOC schedule from the full ledger.
- Appendix O remains selected ledger extracts, not the full ledgers. The dense account pages retain their existing layout and smaller type; any redesign is for Ian to decide. The report retains its work-in-progress label for his review.

## Page 1 callouts and transition reserve — 9 November 2026

- Restored the four upper callouts: transition reserve, end-2031 Trust Cash including earmarks, 2032 investments and home renovation. The 2032 cash surplus and vacation budget appear in two callouts under Our life in retirement, following the V67 arrangement while retaining the current report's content and design.
- The 2027–28 transition paragraph now identifies the transition reserve and shows $12,100 contributed in 2027 plus $18,900 in 2028, reaching $31,000 at the start of 2029. Figures are from the V68 workbook, including Buffer Fund and the account ledgers. On later updates refresh both the annual contributions and the total, not just the monthly figures.
- The revised first page was rendered and checked; remaining report pages retain their existing text and page order. The report remains a work in progress for Ian's review. No decision has been made about restructuring or splitting the report.

## Page samples and review decisions — 9 November 2026

- **Page 1 readability sample approved by Ian:** Page_1_Readability_Sample.pdf, https://chatgpt.com/library?file_id=libfile_56fd9c7655088191b042c6bad2ee0d71&account_id=personal. This approved sample has not yet been incorporated into the main report. Preserve the four upper callouts, both retirement callouts, all material and the clearly explained transition-reserve contribution totals. Recheck figures against the active workbook before final assembly.
- **Pages 2–3 merger withdrawn by Ian:** Pages_2_3_Combined_Sample.pdf, https://chatgpt.com/library?file_id=libfile_389695781e088191bd371313e4aa1fc7&account_id=personal. Ian was looking at an old version and asked to disregard the merger. The sample was not incorporated. Keep the current pages 2 and 3 separate unless Ian later requests otherwise.
- Main report remains Our_Retirement_Plan_V68_WORK_IN_PROGRESS.pdf, https://chatgpt.com/library?file_id=libfile_f75f1315f69081919b3169491f891f56&account_id=personal. Preserve each approved sample separately. Apply the approved changes together at assembly, then update contents, page numbers, workbook mapping and all cross-references and check material completeness and figures. Ian has not approved the broader split or restructuring proposals.

## Approved transition page — 9 November 2026

- Ian approved the latest Transition_to_Retirement_Sample.pdf (Library revision 3): https://chatgpt.com/library?file_id=libfile_86a2156741b88191b17f12dc74b94feb&account_id=personal. Use this as the approved treatment of current report page 7 when assembling the main report; its final position and page number are still to be determined.
- The sample includes the table dividers and the three notes on the 2026 baseline, RMDs, and the July–December 2029 six-month average. Preserve its data, callouts and design. Check all figures against the current workbook at final assembly.
- The original page 7 and other report pages have not yet been replaced or reordered. Page 1's readability sample remains approved. The prior pages 2–3 merger is withdrawn.

## Reorganised working report — 9 November 2026

Ian approved reorganising the existing report now. Keep the approved page 1 and transition samples and all bridges. Do not treat this as approval of the wider proposal to split the document or remove any other material.

- New order: 1 approved page 1; 2 approved transition page (formerly 7); 3–5 the original income bridges (formerly 4–6); 6 the original paired surplus bridges (formerly 3); 7 household budget (formerly 8); 8 2027 spending choices (formerly 9); 9–21 former pages 11–23 in their existing order; 22 the original annual surplus chart (formerly 2); 23 the appendix guide (formerly 24); 24 the 2032 spending choices (formerly 10), moved to the appendix at Ian's direction; 25–55 retain their former page numbers.
- Both original sample decisions remain saved separately. Current printed page numbers and references in the PDF are updated. The appendix guide includes 2032 spending choices on page 24. Recheck page references if the report is restructured further.
- The workbook's Report source map uses the earlier source page numbers: use the old-to-new mapping above when refreshing report pages. The financial master remains unchanged; update that workbook map when the report's structure is agreed rather than assuming its page numbers describe the reorganised document.
- The graphics of the four bridge pages were checked against their originals; the printed chart regions match exactly. The approved transition sample intentionally uses the three notes Ian selected; preserve the underlying tax, RSU and 2026 detail in the workbook and supporting material.

## Approved combined income bridges — 9 November 2026

- Ian approved Side_by_Side_Income_Bridges_Sample.pdf, Library revision 2: https://chatgpt.com/library?file_id=libfile_3c4cc93907d0819199e0b40e8ba613f1&account_id=personal. It combines current report pages 4–5, with notes in two columns beneath their respective bridges. It has not yet been incorporated into the main report.
- Preserve the annual detail tables currently on pages 4–5 in the supporting material when assembling; the sample shows the monthly bridge figures and does not reproduce the annual tables. Recheck workbook figures and page numbering. The sample uses a wider page size than the report; adapt to the report's existing page size and visually verify readability before incorporating it.

## Cash-surplus waterfalls moved — 9 November 2026

- At Ian's direction the paired cash-surplus waterfalls (previous working-report page 6) now follow the investment accounts page: investments are page 11 and waterfalls page 12. The annual cash-surplus chart remains page 22.
- The formerly numbered pages 7–12 are now pages 6–11; subsequent page numbers are unchanged. References affected by the move were adjusted in the PDF. The waterfall chart region was verified visually identical to the prior report.
- The approved combined income-bridges sample remains separate and is not yet incorporated; its original pages remain 4–5 until assembly. The workbook source map still uses pre-reorganisation page references; this note and the previous reorganisation checkpoint record the sequence of mappings.

## Annual surplus chart moved — 9 November 2026

- At Ian's direction the annual cash-surplus chart (previous working-report page 22) now follows the paired surplus waterfalls: investments page 11, waterfalls page 12, annual chart page 13. All three are retained for Ian to review for possible redundancy.
- Previous report pages 13–21 are now pages 14–22; pages 23–55 are unchanged. Updated affected page numbers and references. The annual chart region is visually identical to its prior version. The workbook source map still uses original report page numbers; apply the sequence of mappings in these notes until the structure is agreed.
- The approved combined income bridge sample remains separate, not yet incorporated.

## Approved income bridges incorporated — 9 November 2026

- Incorporated the approved side-by-side 2028–29 and 2031–32 income bridges as page 4 of the main report, with the approved two-column commentary. The chart was rebuilt from workbook waterfall cells at the report's standard page size and visually checked; monthly amounts use the workbook waterfall rows 34–42. The annual bridge details and original versions of the two pages remain in the appendices at pages 55 and 56.
- Previous pages 6–55 are now pages 5–54. Previous pages 4 and 5 are now appendix pages 55 and 56. Updated page labels, cross-references and the appendix guide; the report has 56 pages. The paired cash-surplus waterfalls remain immediately before the annual cash-surplus chart, now pages 11 and 12; investment accounts is page 10.
- Status check against recorded decisions: the approved page 1 and transition page are incorporated, the combined bridge is incorporated, and the cash-surplus pages are grouped after investment accounts. The suggested earlier merger of the surplus pages was withdrawn. No broader splitting or removal has been approved. The workbook's report source map retains its original page references; the sequence of old-to-new mappings here is required when updating until final structure and workbook map are synchronised.

## Report structure after Ian's review — 9 November 2026

- Ian agreed to move former page 9 (survivor annual detail), page 12 (annual surplus chart) and page 16 (living-alone Monte Carlo charts) to the appendix. These are now pages 19, 20 and 21, respectively. The joint Monte Carlo remains in the main report, now page 13, and the 2032 individual comparison remains page 8.
- The illustrative combined-value page remains in the main report as a feel-good overview, following the home page; it is now page 12. Its explanations distinguish pension value from accessible account balances.
- The 2027 account-flow diagram and account budget remain in the main report at pages 16–17: Ian explained these are a major intended outcome for Stacey. The former page 19, before-interest transition summary, was removed from the report as duplicate; its underlying data remains in the workbook.
- The appendix guide, printed numbers and references were updated. This is a 55-page working report, with 17 main pages, an appendix guide on page 18, and supporting pages 19–55. Annual income-bridge detail remains on pages 54–55. The workbook report source map retains the original report's page numbers; update it once the structure has been agreed. Original-to-current mapping remains traceable from successive checkpoints in these notes.

## Combined actions and appendix navigation — 9 November 2026

- Ian approved Combined_Actions_Sample.pdf revision 3; it replaces former main-report pages 14–15 with one page at 14. It retains the monthly transfer table, January extra, annual transfer review, key 2029/July checkpoints, survivor access, RMD, healthcare and account actions. The main report is 16 pages; the account-flow pages are 15–16.
- At Ian's request every supporting section is lettered, A–T. The first four are prioritised to follow the main report: A 2032 spending (18), B living-alone forecast (19), C annual cash-surplus chart (20), D living-alone Monte Carlo (21). E planning assumptions (22), F expense inputs (23–26), G expense detail (27–29), H tax (30), I annual reconciliation (31), J benefits/RSUs (32), K starting accounts (33), L purchasing power (34), M savings commitments (35), N 2029 reserve (36), O 2027 monthly budget (37–38), P HELOC (39), Q contingencies (40), R account flows (41–47), S later-year ledgers (48–52), T detailed income bridges (53–54).
- This list supersedes appendix letters and page numbers in older checkpoints above. The appendix guide and report cross-references were updated; all 20 section headings and 23 automatically identifiable letter-and-page references were checked. The workbook's Report source map still uses the design-master page numbers by design; use the historical page mappings in these notes until a current-report mapping has been added. No financial workbook data or formulas were changed.


## Original and current report pages — 9 November 2026

The validated two-column page crosswalk is maintained in the workbook’s Report source map, columns I–J. It lists the original design-master pages and their locations in the current single V68 PDF, including the five added ledger pages. Keep page locations there when the report changes; do not duplicate the list in these notes. Financial source mappings remain in columns A–G.

### Page-list validation — 9 November 2026

Checked the two-column list above against the 50-page design-master PDF and the current 54-page working PDF, without using the workbook. Confirmed all 50 original pages occur once in the list, the five additional annual ledger extracts point to the correct years, and each appendix letter matches the heading on the destination page. Confirmed both combined income bridges on current page 4 and their original detailed pages 53–54; confirmed the original actions pages 19–20 are combined on current page 14, and original page 21 is absent as recorded. The report remains one PDF. This validates page locations and section labels, not the financial figures or the eventual split.

## V68 checkpoint — 9 November 2026

At Ian's request removed the work-in-progress and draft footer markings on all 54 pages and named the report Our_Retirement_Plan_V68.pdf. Every page now uses the footer “Our Retirement Plan V68”. All page content above the footer was compared with the previous version and is visually unchanged. The report remains a single PDF and the current page list above still applies. No financial figures or workbook mappings were changed; the original-to-current page list remains in these notes.

### Workbook map update — 9 November 2026

The validated page crosswalk was added to Report source map columns I–J. The 50 design-master pages and five added ledger extracts are covered; combined pages show each relevant location. Original source-map cells and all financial data, formulas and cached results were preserved. The 276 source entries identified as New remain source entries and are not asserted to be individual displayed items. The report remains one PDF; revise the crosswalk and references if it is split.

## Version and file naming — 9 November 2026

Ian will review the current V68 plan with Stacey. The current report file is named Retirement_Plan_V68.pdf, matching Retirement_Plan_V68.xlsx. The existing report footer remains “Our Retirement Plan V68”. Any substantive changes from this checkpoint onward belong in V69; keep report and workbook version labels in sync, preserve the V68 checkpoint, and update this process record as needed. Do not infer that any further financial or design changes have been approved.


## Page 16 Bills presentation grouping

Page 16 groups cleaner, gardener, Stacey music lessons and periodic items (Recology, Duolingo, Costco, BBC World News, Fitbit and Amex annual fee) under separate / periodic payments. The reference to car registration points to the existing Trust allocation, avoiding a second charge. The cleaner, gardener and music lessons are monthly workbook expenses; do not describe them as one-offs or add assumed special transfers. Amounts remain sourced from Report Bills details, including D14, D16 and D34 for the three named items; the registration allocation is Expense Inputs B155 and Cash Flow 2027 row 34. This is a presentation grouping only; the Bills account and totals are unchanged.


## V70 page 16 approval

Page 16 groups cleaner, gardener and Stacey music lessons as manually paid from Bills; automated Recology, Duolingo, BBC and Fitbit remain in the other Bills entries. The Trust callout sets the agreed Trust-to-Joint route for property tax, car registration and car servicing. The 2027 Account Ledger rows 143–144 already model property tax and registration through Joint. The servicing earmark (rows 84–87) has no scheduled payment or transfer; do not invent either. January precedes February in the bottom callouts; January transition reserve total is labelled explicitly. V70 workbook retains all V69 calculations and cached results.

Page 12: valuation figures use consistent 17 pt bold typography; values and sources unchanged.

## Trust Cash alignment, V70

The 2027 opening unallocated ledger includes the forecast end-2026 Trust Cash balance less the $500 registration earmark. The 2027–2031 working investment Trust Cash component now links to each year's ledger unallocated cash and transition reserve. The surplus-savings component links to ledger savings; expense earmarks are in Trust Cash but excluded from available investments. Annual existing-balance returns from the tax build are allocated evenly over months in the account ledgers; this is a timing estimate and adds no return assumption. Trust Cash savings B71:B76 check annual available investment balance against the account ledger for 2027–2032. The 2032 investment balance is approximately $2,004,751 after recalculation. The report, source map layout, and Monte Carlo snapshots are not yet refreshed for this alignment; rerun the simulation from current workbook data and audit all affected report figures before treating them as current. Existing fixed Monte Carlo snapshots predate this change.

## Trust Cash returns update: 2029–2031

The 2029–2031 ledger existing-balance return now uses the monthly opening unallocated cash plus transition reserve, with half the month's net movements included, at the existing 3.84% annual rate divided by 12. Annual taxable-interest inputs sum those monthly returns. Surplus-savings interest remains separate within the same Trust Cash account. Formula errors and reconciliation checks passed; independent recalculation reproduced the results. IMPORTANT: interest on Bills surplus transferred during 2032 and the later carryforward is not yet accounted for by the current 2032–2042 annual interest formulas. A direct dependency on the monthly ledger caused a circular recalculation in testing; resolve before describing the return calculation as complete. Report and Monte Carlo snapshots remain stale.

## Unresolved Trust Cash recalculation dependency

A draft 2032 gross-interest correction matched current values under both calculation engines and produced gross return $14,127.99 and incremental tax $4,774.03 in the current joint case, but it was NOT saved to the master. A sensitivity test increasing Trust Cash savings B68 by $1,000 revealed that, in the draft, the 2029 ledger / investment reconciliation diverged by approximately $1,005.80 and the 2032 investment forecast failed to propagate the input change. Both the spreadsheet runtime and an independent LibreOffice recalculation reproduced the divergence. Do not refresh the report or Monte Carlo from this draft or treat the V70 Trust Cash reconciliation as final. Investigate circular dependencies between 2029–2031 ledger monthly returns, annual interest income and taxable cash flows; repair and repeat opening-balance sensitivity, all ledger movement checks and 2027–2032 Trust Cash investment checks before implementing the tested 2032 gross / net formula. Monthly assumed receipt and withdrawal timing must remain explicit and tax must be deducted once.

## Trust Cash loop isolated

The 2029–2031 annual ordinary-interest input currently sums the ledger monthly existing-balance interest, while that monthly interest depends on the ledger's unallocated cash movements and tax-sensitive Joint funding. In a test copy, replacing those annual inputs with the prior-year-balance-based annual formulas and allocating that interest evenly across months removed the $1,005.80 reconciliation mismatch in a +$1,000 opening-balance test. That test is NOT a final fix: it does not yet properly account for the timing of Bills surpluses and unallocated outflows within the year. Do not replace the master with this approximation. The 2032-and-later interest issue and report/Monte Carlo refresh remain open.

## 2032 gross, tax and net interest rows

The 2032 Account Ledger has explicit memo rows 171 gross interest, 172 attributable tax and 173 net retained, each for B:M and annual total N. These link to existing gross and tax rows 64 and 65 and are not additional account movements. No interest assumptions, calculations or forecasts changed. The 2029–2031 circular dependency and 2032 Bills-surplus interest issue remain unresolved; report and Monte Carlo snapshots remain stale. Do not infer that these memo rows complete the interest reconciliation.

## Draft interest sequencing and Medicare follow-up (not applied)

A scratch draft separated gross interest from incremental tax on cumulative interest for the 2027–2031 monthly ledgers, deducted tax once from Trust Cash and credited net amounts; it included the weighted 2032 Bills surplus and carried forward the correct 2033 opening balance. The initial draft passed ledger/investment reconciliation and a $1,000 opening-balance sensitivity, but the draft set Tax & Cash Flow B25 to zero for the baseline tax build. This omits Trust interest from B86, which is used in Medicare MAGI lookbacks. A subsequent attempt to expose full AGI and reconnect Healthcare Components C12:C16 made recalculation run excessively and was not validated. The draft was NOT applied to the master; V70 remains provisional. Next: design and independently validate the full-interest AGI/Medicare links without reintroducing the calculation loop; verify gross, tax, net, tax returns, Medicare MAGI, account movement and investment checks under sensitivity. The 2032 Bills-surplus and subsequent carryforward corrections are also uncommitted.

## Trust Cash interest sequence and Medicare AGI — updated

The prior warnings about the 2029–2031 circular interest/tax dependency and the missing 2032 Bills-surplus interest are superseded by this update. The 2027–2031 account ledgers calculate gross Trust interest first, then cumulative incremental federal/state tax using the workbook tax parameters, then net interest and the account closing balance. Tax on Trust interest is deducted once in Trust Cash rather than again in baseline Joint cash flow. The 2027–2028 ledgers show memo rows 200–202 (gross, tax, net); 2029–2031 use rows 186–188; 2032 uses rows 171–173. The 2029–2031 Trust Cash savings component tracks its gross balance; total interest tax is deducted in ledger unallocated cash and displayed in savings column E as a memo, not deducted again from savings column F. 2032 annual interest includes time-weighted unallocated inflows/outflows; 2033 opening interest balance links to the 2032 investment cash balance. The existing 3.84% return remains unchanged; 2029–2032 monthly timing uses a mid-month estimate, while 2027–2028 use the existing annual timing assumption.

For 2027–2031, Tax & Cash Flow B25 is baseline other income excluding Trust interest; B355 displays total gross Trust interest; B356 displays full AGI including Trust interest; B357 displays baseline federal/state tax plus interest tax. Healthcare Components C12:C16 and the 2028 Tax & Cash Flow B229 lookback reference full AGI B356; prior CTP-only gross interest terms were removed from lookbacks to avoid duplication. Formula and ledger checks passed for current values and a +$1,000 opening balance sensitivity; a separate LibreOffice recalculation matched current key results without formula errors. Monthly tax calculations use year-to-date incremental federal and California tax based on the existing annual tax assumptions. Verify tax sheet report mappings against the baseline/total distinction when refreshing. The report and all fixed Monte Carlo snapshots still require refresh/rerun. The workbook remains a planning model; monthly timing is estimated, and the calculations have not been independently reviewed by a tax professional.

## V70 Monte Carlo refresh following Trust Cash alignment

Reran 10,000 paths per case and survivor scenario with seed 642032 (plus the existing survivor seed offsets), using the current V70 financial workbook. Refreshed MC annual 2027+, Monte Carlo 2032–2042, the working/lower/6% all/5%/0% age-95 snapshots, Simulation comparison, MC 2027 comparison current columns, and Market stress inputs. Legacy comparison columns remain historical. An independent workbook recalculation refreshed the embedded chart caches; verify cached series against the snapshot cells on future refreshes.

The V70 simulation code derives the available Trust Cash annual net movements from the Savings Forecast ledger-linked annual balances, so the existing balance and previously unallocated cash are not added twice. The Trust Cash surplus-savings component remains a separate accounting component inside the same account. Alternative cash-return cases apply their selected cash rate while holding the workbook's annual net cash movements fixed. CTP, expense and pre-2032 cash-flow assumptions remain deterministic except modeled RMDs, as before. The no-shock stress outputs agree with the corresponding base simulation. Survivor scenarios use workbook survivor schedules and the existing rollover and age assumptions. Conditional shocks use Market stress inputs and the workbook IRA mix.

Refresh tools and a provenance manifest are packaged in Retirement_Plan_V70_Monte_Carlo_Tools.zip. The manifest SHA-256 refers to workbook version 9 before snapshot cells were written. The saved report has not been refreshed, by request; earlier report changes and all revised financial values must be reflected in the report before presenting its Monte Carlo page as current.


## Approved page 1 and opening-balance action

The approved page 1 sample is incorporated with slightly increased paragraph spacing: employment and preparation in one box, transition in a second, and 2032-onward retirement at the top of the right column. Page 14 timing and balances states the existing 2027 Account Ledger opening assumptions: Joint B8, Bills B27, UK B37 / Expense Inputs exchange-rate equivalent, and personal / groceries B108, B112, B116. It instructs setting the two US balances, checking UK against £4,500, and establishing automatic transfers before 2027. The underlying Trust Cash changes, updated report financial values, naming, charts and Monte Carlo are explicitly deferred as requested. Page 12 valuation typography and page 16 layout remain in place.

## V70 report refresh checkpoint — Trust Cash and Monte Carlo

- The working copy `Retirement_Plan_V70_report_update_in_progress.pdf` retains the existing report and approved layouts. Page 13 now uses the current V70 workbook's `Simulation comparison`, `MC annual 2027+`, and `Market stress inputs` snapshots. Page 21's survivor charts use `Monte Carlo 5 percent`. Pages 22 and 33 use Trust Cash terminology and describe the opening balance and accumulated surplus as components of the same account.
- This is an **incomplete working copy**, not the updated report. In particular, Trust Cash figures and dependent income, tax, surplus, assets, bridges, survivor comparisons and appendices still require a page-by-page update and verification. Page 9 still contains the previous split-account presentation. Do not assume unchanged pages match the current workbook.
- Source discrepancy resolved in V70 workbook: the 2027 monthly scenario and the 2027–2031 cash-flow overview now reference the account ledger for Trust Cash interest. For 2027–28 the net interest retained in Trust Cash is included in planned savings; gross interest and associated tax are displayed separately. From 2029 onward the overview includes total Trust Cash interest and its tax in cash surplus, consistent with the existing treatment of surplus cash interest in those years. The ledger, investment forecast and Monte Carlo snapshots were unchanged. The report must now be refreshed against the corrected workbook.
- The earlier experimental correction is superseded by the saved workbook. The 2027 monthly scenario reconciliation now accounts for $100 of opening Joint cash used during the year (opening $250, closing $150); the difference is zero to rounding.


## V70 refresh checkpoint after approved page 14

- Approved chronological page 14 is in the main V70 report.
- The working report includes page 14, Monte Carlo pages 13 and 21, Trust Cash names on pages 9, 22 and 33, selected workbook-linked tables on pages 2, 7–9, 19, 30–31, 34–35, 37–38 and 48–49, and selected figures on pages 1, 6, 12, 15–16 and 18. All changes still need full audit against the latest workbook.
- **Not ready for review as a complete report.** Unfinished work includes the waterfall/bridge graphics and their labels and narratives, annual-surplus chart page 20, other account and ledger pages, survivor summaries, cross-checking every figure, and resolving the 2027 monthly appendix display of interest tax. Tables refreshed automatically must be audited for correctness, including totals and labels, before delivery. The V70 report and the working copy both contain old financial figures elsewhere.

## V70 report refresh completed after workbook alignment

This section supersedes the two preceding checkpoint statuses. The main report has the approved chronological page 14 and the updated V70 workbook figures, including the refreshed joint and survivor Monte Carlo snapshots. The current workbook is `Retirement_Plan_V70.xlsx`, and the current report remains `Retirement_Plan_V70.pdf`.

- Income bridges on pages 3–4 and 53–54 use `Comparison`, `2028 to 2029 Waterfall` and `2031 to 2032 Waterfall`. Cash-surplus bridges on page 10 use `Cash surplus bridges`; the annual chart on page 20 uses `Cash flow overview`. These remain waterfalls and an annual bar chart in the existing page layouts. When inputs change, update the bars as well as the labels and adjacent tables.
- Page 9 uses `Report assets`: base and surplus are components of one Trust Cash account; the displayed available amounts exclude expense earmarks. Page 1's end-2031 Trust Cash figure is `2031 Account Ledger!M48`, which includes earmarks. The two measures should not be interchanged.
- The 2027 monthly tax on Trust Cash interest comes from `2027 Monthly Scenario!N94`; the page 37 note explains its treatment. The source for 2029–2031 account-flow interest rows `Report account flows!162,251,340` now links to the complete gross-interest ledger rows 186, not only the surplus component in row 64. These are reporting links and do not change the forecasts or Monte Carlo snapshots.
- Page 35's scheduled-savings subtotal excludes 2027–28 net Trust Cash interest retained, as its accompanying note states; the annual overview on page 2 includes that retained interest in planned savings. Use the relevant source and definition when refreshing either page.
- Automated comparisons checked the complete displayed cash-flow table on page 2, retirement/survivor/assets tables on pages 7–9 and 19, baseline tax table on page 30, 2027 monthly tables on pages 37–38 (property-tax payments on page 37 intentionally come from the ledger rather than the reserve-funding scenario row), and selected 2028–2032 ledger cells on pages 48–52. The cash-surplus bridges reconcile to zero. Reviewed page appearance in contact sheets and rendered the revised charts and ledger pages individually.
- Trust Cash reporting links and the 2027 opening-cash reconciliation were corrected in the workbook; no financial forecast, account balance or simulation snapshot changed as a result. The contingency page remains discussion material outside the forecast.
