import pandas as pd 
import csv 
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")

fig= ff.create_distplot([df["Weight(Pounds)"].tolist()], ["weights"])
fig.show()