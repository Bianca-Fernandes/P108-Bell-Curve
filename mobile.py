import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv") 
a = df["Avg Rating"].tolist()
fig = ff.create_distplot([a], ["Avg Rating"])
fig.show()