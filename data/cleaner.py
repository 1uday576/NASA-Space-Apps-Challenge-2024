import pandas as pd
import plotly.express as px
pd.options.mode.copy_on_write = True 
stars = pd.read_csv("data/originalDowload/stellarHosts.csv", sep=',', skiprows=30)

scatter1 = stars[["st_rad", "st_mass"]]
scatter1.dropna(subset=["st_rad", "st_mass"], inplace=True)
print(scatter1)

fig = px.scatter(scatter1, x="st_mass", y="st_rad", title="The mass vs the radius of a star.")
fig.show()

scatter2 = stars[["st_mass", "st_logg"]]
scatter2.dropna(subset=["st_mass", "st_logg"], inplace=True)
fig = px.scatter(scatter2, x="st_mass", y="st_logg", title="The mass vs the surface gravity of a star.")
fig.show()