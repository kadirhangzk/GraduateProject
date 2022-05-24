from multiprocessing import context
from turtle import color
from django.http.response import HttpResponse
from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt, mpld3
import seaborn as sns
import os
import base64, urllib
from io import BytesIO
import io




def index(request):
    data = pd.read_csv (r'C:\Users\trapn\Desktop\earthquake.csv')
    ##data = data.head(10)
    data.city.value_counts().plot(kind = "bar", color = "red", figsize = (30,10) , fontsize = 20)
    plt.xlabel("City", fontsize= 18 ,color="blue")
    plt.ylabel("Frequency", fontsize = 18, color = "blue")
    context = {"data" : plt.savefig("blog/static/img/frequency.png")}

    return render(request, "blog/index.html", context)


def countries(request):
    data2 = pd.read_csv (r'C:\Users\trapn\Desktop\earthquake.csv')
    data2.country.value_counts().plot(kind = "bar", color = "red", figsize = (30,10) , fontsize = 20)
    plt.xlabel("City", fontsize= 18 ,color="blue")
    plt.ylabel("Frequency", fontsize = 18, color = "blue")
    context = {"data2" : plt.savefig("blog/static/img/countries.png")}

    return render(request, "blog/countries.html", context)

def years(request):
    data3 = pd.read_csv (r'C:\Users\trapn\Desktop\earthquake.csv')
    def yeardate(x):
        return x[0:4]
    data3["yeardate"] = data3.date.apply(yeardate)
    #We must change object to integer.
    data3['yeardate'] = data3.yeardate.astype(int)
    data3.yeardate.plot(kind = "hist" , color = "red" , edgecolor="black", bins = 100 , figsize = (12,12) , label = "Earthquakes frequency")
    plt.legend(loc = "upper right")
    plt.xlabel("Years")
    context = {"data3" : plt.savefig("blog/static/img/years.png")}

    return render(request, "blog/years.html", context)

def dataset(request):
    data4 = pd.read_csv (r'C:\Users\trapn\Desktop\earthquake.csv')
    filter = data4.head(10)
    context = {"data4" : filter.to_html()}

    return render(request, "blog/dataset.html", context)

def correlation(request):
    data5 = pd.read_csv (r'C:\Users\trapn\Desktop\earthquake.csv')
    plt.figure(figsize=(15,15))
    sns.heatmap(data5.corr(), annot = True, fmt= ".1f", linewidths = .3)
    context = {"data5" : plt.savefig("blog/static/img/correlation.png")}

    return render(request, "blog/correlation.html", context)


def biggest(request):
    data6 = pd.read_csv (r'C:\Users\trapn\Desktop\earthquake.csv')
    data6.xm.max()
    filtering = data6.country == "turkey"
    filtering2 = data6.xm == 7.9
    context = {"data6" : data6[filtering & filtering2].to_html}

    return render(request, "blog/biggest.html", context)
