import plotly.express as px 
import plotly.figure_factory as ff 
import csv 
import pandas as pd 
df = pd.read("data.csv")

fig = ff.create_distplot([df["Avg rating"].tolist()], ["Avg rating"], show_hist = False)
fig.show()