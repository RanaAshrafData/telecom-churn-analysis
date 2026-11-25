# Telecom Customer Churn Analysis

Descriptive analysis of which contracts, services, payment methods and tenure bands go with customers leaving, using Python (pandas) and a Tableau dashboard.

## Data
IBM "Telco Customer Churn" sample: 7,043 customers, 21 columns. It is synthetic data for a fictional telco, not real company records.
- Source file: https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv
- Repository (Apache License 2.0): https://github.com/IBM/telco-customer-churn-on-icp4d
- Description: https://www.ibm.com/docs/en/cognos-analytics/12.1.x?topic=samples-telco-customer-churn
- `Telco-Customer-Churn.csv` here is the original file, unmodified, redistributed under Apache 2.0 (see `LICENSE`).

## What I did
- Read `TotalCharges` as a number. 11 rows are blank (customers with tenure 0); they stay missing.
- Churn = 1 when `Churn` is "Yes". Churn rate = churned customers / customers in the group.
- Tenure bands: 0-12, 13-24, 25-48, 49-72 months.
- `churn_analysis.py` prints the rates shown in the dashboard. Run: `pip install pandas` then `python churn_analysis.py` in this folder.
- Live dashboard (Tableau Public): https://public.tableau.com/app/profile/rana.ashraf4039/viz/TelcoCustomerChurn_17956152043970/Telcocustomerchurn
- Tableau: two calculated fields (Tenure Band, Churn Rate) and five bar charts plus two KPI tiles on one dashboard (`tableau_dashboard.png`).

## Results (sample data)
Overall churn 26.5% (1,869 of 7,043). Month-to-month 42.7% vs two-year 2.8%. Tenure 0-12 months 47.4% vs 49-72 months 9.5%. Fiber optic 41.9% vs DSL 19.0%. No tech support 41.6% vs 15.2% with it. Electronic check 45.3%.

## Limits
- Groups overlap, so effects are mixed. Rates are raw group averages; no model or controls.
- Synthetic data: results are not facts about any real company, and they show association, not cause.
- `Telco_Customer_Churn.twbx` is the packaged Tableau workbook downloaded from the published dashboard (7 sheets, dashboard, embedded IBM data). `tableau_dashboard.png` is an image of the dashboard.
