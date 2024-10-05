import pandas as pd
import plotly.express as px
pd.options.mode.copy_on_write = True 

#create the files that will hold the cleaned data for the stellar host graphs
stars = pd.read_csv("data/originalDowload/stellarHosts.csv", sep=',', skiprows=30)

#density vs gravity graph
densityGravity = stars[["st_dens", "st_logg"]]
densityGravity.dropna(subset=["st_dens", "st_logg"], inplace=True) #drop all rows that have no value from any column

densityGravity.to_csv("data/aggregatedData/stellar/densityGravity.csv")

#density vs age graph
densityAge = stars[["st_dens", "st_age"]]
densityAge.dropna(subset=["st_dens", "st_age"], inplace=True) #drop all rows that have no value from any column

densityAge.to_csv("data/aggregatedData/stellar/densityAge.csv")

#mass vs luminosity
massLuminosity = stars[["st_mass", "st_lum"]]
massLuminosity.dropna(subset=["st_mass", "st_lum"], inplace=True)#drop all rows that have no value from any column
massLuminosity.to_csv("data/aggregatedData/stellar/massLuminosity.csv")

#stellar metallicity ratio
metallicityRatio = stars["st_metratio"]
metallicityRatio.dropna(inplace=True)
metallicityRatio.to_csv("data/aggregatedData/stellar/metallicityRatio.csv")

#distance from earth
distanceFromEarth = stars["sy_dist"]
distanceFromEarth.dropna(inplace=True)
distanceFromEarth.to_csv("data/aggregatedData/stellar/distanceFromEarth.csv")

#create the files that will hold the cleaned data for the planetary systems (exoplants)
exoplants = pd.read_csv("data/originalDowload/planetarySystems.csv", sep=',', skiprows=31)

#solution type
solutionType = exoplants["soltype"]
solutionType.dropna(inplace=True)
solutionType.to_csv("data/aggregatedData/planeterySystems/solutionType.csv")

#distance from star to planet
distStarPlanet = exoplants["pl_imppar"]
distStarPlanet.dropna(inplace=True)
distStarPlanet.to_csv("data/aggregatedData/planeterySystems/distStarPlanet.csv")

#orbital period
orbitalPeriod = exoplants["pl_orbper"]
orbitalPeriod.dropna(inplace=True)
orbitalPeriod.to_csv("data/aggregatedData/planeterySystems/orbitalPeriod.csv")

#distance from earth
distEarth = exoplants["sy_dist"]
distEarth.dropna(inplace=True)
distEarth.to_csv("data/aggregatedData/planeterySystems/distEarth.csv")

#create the files that will hold the cleaned data for the discovery info
discovery = pd.read_csv("data/originalDowload/planetarySystems.csv", sep=',', skiprows=31)

#the discrovery method trend
discoveryTrend = discovery[["disc_year", "discoverymethod"]]
discoveryTrend.dropna(inplace=True)
discoveryTrend.to_csv("data/aggregatedData/discoveryInfo/discoveryTrend.csv")

#the discrovery facility trend
discoveryFacility = discovery[["disc_year", "disc_facility"]]
discoveryFacility.dropna(inplace=True)
discoveryFacility.to_csv("data/aggregatedData/discoveryInfo/discoveryFacility.csv")

# scatter1 = stars[["st_rad", "st_mass"]]
# scatter1.dropna(subset=["st_rad", "st_mass"], inplace=True)
# print(scatter1)

# fig = px.scatter(scatter1, x="st_mass", y="st_rad", title="The mass vs the radius of a star.")
# fig.show()

# scatter2 = stars[["st_mass", "st_logg"]]
# scatter2.dropna(subset=["st_mass", "st_logg"], inplace=True)
# fig = px.scatter(scatter2, x="st_mass", y="st_logg", title="The mass vs the surface gravity of a star.")
# fig.show()