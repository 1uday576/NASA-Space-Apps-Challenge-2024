import pandas as pd
import plotly.express as px

dt = pd.read_csv("data/aggregatedData/discoveryInfo/discoveryTrend.csv")

print(dt.sort_values(by="disc_year"))
