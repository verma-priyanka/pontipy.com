from flask import Flask, render_template
from pontiPy import *


df = pd.read_csv('sampledata/coastal_1995_2000.csv', index_col=0)
df_change = pontiPy_Change(df)

print(df_change.exchange(1, Total=False))
