import os
from django.shortcuts import render
import pandas as pd
import plotly.express as px

#holds all the of the graphs related to stellar
class StellarGraphs:
    #density vs gravity scatter plot
    dt1 = pd.read_csv(os.path.realpath(os.path.join("..", "data", "aggregatedData", "stellar","densityGravity.csv")))
    densityGravity = px.scatter(dt1, x="st_dens", y="st_logg", 
                     labels={
                        "st_dens": "Density (g/cm³)",
                        "st_logg": "Surface Gravity [log10(cm/s²)]"
                    },title="The density vs the gravity of a star.").to_html(full_html = False, include_plotlyjs=False)

    #age vs luminosity scatter
    dt2 = pd.read_csv(os.path.realpath(os.path.join("..", "data", "aggregatedData", "stellar","ageLum.csv")))
    densityAge = px.scatter(dt2, x="st_age", y="st_lum", 
                     labels={
                        "st_age": "Stellar Age [Gyr one billion years]",
                        "st_lum": "Solar Luminosities [log10(Solar)]"
                    },title="The age vs the luminosity of a star.").to_html(full_html = False, include_plotlyjs=False)
    
    #mass vs luminosity
    dt3 = pd.read_csv(os.path.realpath(os.path.join("..", "data", "aggregatedData", "stellar","massLuminosity.csv")))
    massLuminosity = px.scatter(dt3, x="st_mass", y="st_lum", 
                     labels={
                        "st_mass": "Mass (Solar mass)",
                        "st_lum": "Solar Luminosities [log10(Solar)]"
                    },title="The mass vs the luminosity of a star.").to_html(full_html = False, include_plotlyjs=False)
    
    #metallicity ratio pie graph
    dt4 = pd.read_csv(os.path.realpath(os.path.join("..", "data", "aggregatedData", "stellar","metallicityRatio.csv")))
    metaRatio = px.pie(dt4, values="count", names="st_metratio", title="The Metallicity Ratio ([M/H] is general metal content)").update_traces(textposition='inside', textinfo='percent+label').to_html(full_html = False, include_plotlyjs=False)

    #distance from earth histogram
    dt5 = pd.read_csv(os.path.realpath(os.path.join("..", "data", "aggregatedData", "stellar","distanceFromEarth.csv")))
    distanceEarth = px.histogram(dt5, x="sy_dist", 
                                 labels={
                                    "sy_dist": "Distance (parsecs)",
                                    "count":"Count"
                                ""}, title="The number of stars at a certain distance intervals from Earth.").to_html(full_html = False, include_plotlyjs=False)

#holds all the of the graphs related to exoplants
class ExoplantsGraphs:
    #distance from earth histogram
    dt1 = pd.read_csv(os.path.realpath(os.path.join("..", "data", "aggregatedData", "planeterySystems","solutionType.csv")))
    solutionType = px.bar(dt1, x="soltype", y ="count",
                                 labels={
                                    "soltype": "Solution Type",
                                    "count":"Count"
                                }, title="The status of exoplanets in NASA Exoplanet Archives.").to_html(full_html = False, include_plotlyjs=False)
    
    #distance from star to exoplanet histogram
    dt2 = pd.read_csv(os.path.realpath(os.path.join("..", "data", "aggregatedData", "planeterySystems","distStarPlanet.csv")))
    disStarExo = px.histogram(dt2, x="pl_imppar", y="count",
                                 labels={
                                    "count":"Count",
                                    "pl_imppar": "Projected Distance"
                                    }, title="The number of exoplanets at approximent distance from their star.").to_html(full_html = False, include_plotlyjs=False)
    
    #orbital period
    dt3 = pd.read_csv(os.path.realpath(os.path.join("..", "data", "aggregatedData", "planeterySystems","orbitalPeriod.csv")))
    orbitalPeriod = px.histogram(dt3, x="pl_orbper",
                                 labels={
                                    "count":"Count",
                                    "pl_orbper": "Orbital Period (days)"
                                    }, title="The number of exoplanets orbiting their star.").to_html(full_html = False, include_plotlyjs=False)
    
    #distance from earth histogram
    dt4 = pd.read_csv(os.path.realpath(os.path.join("..", "data", "aggregatedData", "planeterySystems","distEarth.csv")))
    distanceEarth = px.histogram(dt4, x="sy_dist", 
                                 labels={
                                    "sy_dist": "Distance (parsecs)",
                                    "count":"Count"
                                ""}, title="The number of exoplanets at a certain distance intervals from Earth.").to_html(full_html = False, include_plotlyjs=False)

#holds all of the discovery info graphs
class DiscoveryInfoGraphs:
    #distance from earth histogram
    dt1 = pd.read_csv(os.path.realpath(os.path.join("..", "data", "aggregatedData", "discoveryInfo","discoveryTrend.csv")))
    solutionType = px.line(dt1, x="disc_year", y="count", labels={
                                                                "disc_year": "Year of Discovery",
                                                                "count": "Count",
                                                                "discoverymethod": "Discovery Method"
                                                            },color="discoverymethod", title="The number of exoplants each method discovered over time.").to_html(full_html = False, include_plotlyjs=False)
    
    #distance from earth histogram
    dt2 = pd.read_csv(os.path.realpath(os.path.join("..", "data", "aggregatedData", "discoveryInfo","discoveryFacility.csv")))
    facility = px.line(dt2, x="disc_year", y="count", labels={
                                                                "disc_year": "Year of Discovery",
                                                                "count": "Count",
                                                                "disc_facility": "Facility Name"
                                                            },color="disc_facility", title="The number of exoplants each facility discovered over time.").to_html(full_html = False, include_plotlyjs=False)

# Create your views here.
def index(request):
    return render(request, 'graphs/homePage.html')

#the stellar host page
def stellarHost(request):
    context = {
        "fig1": StellarGraphs.densityGravity,
        "fig2": StellarGraphs.densityAge,
        "fig3": StellarGraphs.massLuminosity,
        "fig4": StellarGraphs.metaRatio,
        "fig5": StellarGraphs.distanceEarth
    }

    return render(request, "graphs/stellarHostsPage.html", context)

#the exoplant page
def exoplants(request):
    context = {
        "fig1": ExoplantsGraphs.solutionType,
        "fig2": ExoplantsGraphs.disStarExo,
        "fig3": ExoplantsGraphs.orbitalPeriod,
        "fig4": ExoplantsGraphs.distanceEarth
    }

    return render(request, "graphs/stellarHostsPage.html", context)

#the exoplant page
def discoveryInfo(request):
    context = {
        "fig1": DiscoveryInfoGraphs.solutionType,
        "fig2": DiscoveryInfoGraphs.facility,
    }

    return render(request, "graphs/discoveryInfo.html", context)