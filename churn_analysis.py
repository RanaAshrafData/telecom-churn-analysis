# Prints the churn rates shown in the Tableau dashboard, to check the numbers.
import pandas as pd
d=pd.read_csv('Telco-Customer-Churn.csv')
d['TotalCharges']=pd.to_numeric(d['TotalCharges'],errors='coerce')
d['c']=(d.Churn=='Yes').astype(int)
d['band']=pd.cut(d.tenure,[-1,12,24,48,72],labels=['0-12','13-24','25-48','49-72'])
def r(col): return d.groupby(col,observed=True).c.mean()*100
print(d.c.mean()*100, d.MonthlyCharges.mean(), d.TotalCharges.isna().sum())
for c in ['Contract','band','InternetService','PaymentMethod','TechSupport','OnlineSecurity']: print(r(c).round(1).to_dict())
seg=d[(d.Contract=='Month-to-month')&(d.InternetService=='Fiber optic')&(d.tenure<=12)]
print(len(seg),seg.c.mean()*100)
