from django.shortcuts import render
import pandas as pd
import plotly.express as px

# Create your views here.
def index(request):
    return render(request, 'graphs/homePage.html')