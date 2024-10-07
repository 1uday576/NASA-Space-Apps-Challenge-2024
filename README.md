# NASA-Space-Apps-Challenge-2024

## About Chronicles of Exoplanet Exploration Challenge
Embark on a thrilling journey to revolutionize exoplanet education! The discovery of exoplanets has redefined our understanding of planetary systems, expanding what we know about our place in the universe. From scorching gas giants to potentially habitable rocky worlds, these distant worlds offer a glimpse into the remarkable diversity of planetary configurations. Traditional educational materials about this topic may not be accessible to everyone, particularly those from underserved communities or with limited access to resources. Your challenge is to develop engaging and accessible learning materials that leverage creativity to enlighten students about the wonders of exoplanets.

## High Level Summary

Exoplanet Extract is a website I developed to show graphs based on data on exoplanets from the NASA Exoplanet Archive to either visual the data, highlight trends, or show potential correlation between the data. This addresses the challenge as it can spark discussions and curiosity within students as they attempt to understand and reason with why these graphs look as they do. This develops an extremely important skill that is needed not only in the sciences but can be transferred into other fields as well. That skill is to analyze observations to come to a conclusion, build a reasoning for that conclusion, and diligently examine the procedure itself and your own explanation.


## Project Details
### What the project achieves:
The purpose of the project was very simple, it was to show graphs based on the data provide by the NASA Exoplanet Archive. This can be seen in the project through a very simple website design that has an about us page to inform the user about the purpose of the website followed by a menu bar containing three tabs; Stellar Hosts, Exoplanets, and Discovery Information. Each tab displays 2 to 5 graphs that are related to the header (stellar hosts for stars, etc.) that are statically made through prefiltered data to ensure a accurate and proper graphical personation on data I personally selected. Each of these graphs have been modified such that they are user friendly (more descriptive axis labels, use of color, markers, etc.), have tools to traverse the graph, limit the data on the graph, and even download the graphs as PNG's themselves.

### How does it work and tools used:
I first downloaded the tables from the NASA Exoplanet Archives as CSV files so I can use pandas – an open-source python tool for data analysis and manipulation – to pick specific columns that I would use and to clean that data (no values are removed). For each graph I wanted to create I would create a CSV file just for that graph with the data prepared and ready to use. The tool I used to create the graphs was Plotly which had an excellent library to easily and quickly make graphs, edit to your liking, and even export to an HTML div which was the most important part. To display my graphs to the user I decided to create a simple website as it would keep my graphs need and easily accessible. To do this I used the Django as my backend that would serve the pages to the user and have the code to create the graphs with HTML and CSS used in the front end as I did not need anything fancy. When the website is up and running the user can select between four tabs

+ About – a quick introduction to the website and what its purpose is.

+ Stellar Hosts – the graphs related to the stars that hold these exoplanets.

+ Exoplanets – the graphs related to the exoplanets themselves.

+ Discovery Information – the graphs that show the trend in the discovery of these exoplanets.

When the user is shown with a graph they have the ability to zoom in and out of the graph to get a better look, able to select and deselect data series, and see specific data points on that graph.

