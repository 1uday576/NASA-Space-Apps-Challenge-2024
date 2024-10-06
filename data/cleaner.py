import pandas as pd
pd.options.mode.copy_on_write = True 

#create the files that will hold the cleaned data for the stellar host graphs
stars = pd.read_csv("data/originalDowload/stellarHosts.csv", sep=',', skiprows=30)

#density vs gravity graph
densityGravity = stars[["st_dens", "st_logg"]]
densityGravity.dropna(subset=["st_dens", "st_logg"], inplace=True) #drop all rows that have no value from any column

densityGravity.to_csv("data/aggregatedData/stellar/densityGravity.csv")

#age vs luminosity
ageLum = stars[["st_age", "st_lum"]]
ageLum.dropna(subset=["st_age", "st_lum"], inplace=True) #drop all rows that have no value from any column

ageLum.to_csv("data/aggregatedData/stellar/ageLum.csv")

#mass vs luminosity
massLuminosity = stars[["st_mass", "st_lum"]]
massLuminosity.dropna(subset=["st_mass", "st_lum"], inplace=True)#drop all rows that have no value from any column
massLuminosity.to_csv("data/aggregatedData/stellar/massLuminosity.csv")

#stellar metallicity ratio
metallicityRatio = stars["st_metratio"]
metallicityRatio.dropna(inplace=True)
metallicityRatio = metallicityRatio.value_counts() #creates a table of how many times each unique value shows up in the Series
metallicityRatio.to_csv("data/aggregatedData/stellar/metallicityRatio.csv")

#distance from earth
distanceFromEarth = stars["sy_dist"]
distanceFromEarth.dropna(inplace=True)
distanceFromEarth = distanceFromEarth.value_counts() #creates a table of how many times each unique value shows up in the Series
distanceFromEarth.to_csv("data/aggregatedData/stellar/distanceFromEarth.csv")

#create the files that will hold the cleaned data for the planetary systems (exoplants)
exoplants = pd.read_csv("data/originalDowload/planetarySystems.csv", sep=',', skiprows=31)

#solution type
solutionType = exoplants["soltype"]
solutionType.dropna(inplace=True)
solutionType = solutionType.value_counts()
solutionType.to_csv("data/aggregatedData/planeterySystems/solutionType.csv")

#distance from star to planet
distStarPlanet = exoplants
distStarPlanet.dropna(inplace=True)
distStarPlanet = distStarPlanet["pl_imppar"]
distStarPlanet = distStarPlanet.value_counts()
distStarPlanet.to_csv("data/aggregatedData/planeterySystems/distStarPlanet.csv")

#orbital period
orbitalPeriod = exoplants
orbitalPeriod.dropna(inplace=True)
orbitalPeriod = orbitalPeriod[orbitalPeriod.pl_imppar.astype(int) < 1000]
orbitalPeriod = orbitalPeriod["pl_orbper"]
orbitalPeriod = orbitalPeriod.value_counts()
orbitalPeriod.to_csv("data/aggregatedData/planeterySystems/orbitalPeriod.csv")

#distance from earth
distEarth = exoplants["sy_dist"]
distEarth.dropna(inplace=True)
distEarth = distEarth.value_counts()
distEarth.to_csv("data/aggregatedData/planeterySystems/distEarth.csv")

#create the files that will hold the cleaned data for the discovery info
discovery = pd.read_csv("data/originalDowload/planetarySystems.csv", sep=',', skiprows=31)

#the discrovery method trend
discoveryTrend = discovery[["disc_year", "discoverymethod"]]
discoveryTrend.dropna(inplace=True)
discoveryTrend = discoveryTrend.value_counts()
discoveryTrend.to_csv("data/aggregatedData/discoveryInfo/discoveryTrend.csv")
discoveryTrend = pd.read_csv("data/aggregatedData/discoveryInfo/discoveryTrend.csv")
discoveryTrend.sort_values(by="disc_year", inplace=True)
discoveryTrend.to_csv("data/aggregatedData/discoveryInfo/discoveryTrend.csv")

#the discrovery facility trend
discoveryFacility = discovery[["disc_year", "disc_facility"]]
discoveryFacility.dropna(inplace=True)
discoveryFacility = discoveryFacility.value_counts()
discoveryFacility.to_csv("data/aggregatedData/discoveryInfo/discoveryFacility.csv")
discoveryFacility = pd.read_csv("data/aggregatedData/discoveryInfo/discoveryFacility.csv")
discoveryFacility.sort_values(by="disc_year", inplace=True)
discoveryFacility.to_csv("data/aggregatedData/discoveryInfo/discoveryFacility.csv")