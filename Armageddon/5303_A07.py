from datetime import datetime
import numpy as np
import pandas as pd
import plotly
import plotly.offline as offline
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, plot
#init_notebook_mode(connected=True)

#import csv file
quake = pd.read_csv('C:/Users/Garrett/Python-Armageddon-Project/Armageddon/Datasets/earthquakes1970-2014.csv')
#quake = pd.read_csv('/Users/garrettmorris/Desktop/database_stuff/earthquakes.csv')
volcano = pd.read_csv('C:/Users/Garrett/Python-Armageddon-Project/Armageddon/Datasets/volcanoes-worldwide.csv')
#airports = pd.read_csv('/Users/garrettmorris/Desktop/database_stuff/airports.csv', error_bad_lines=False)
ufos = pd.read_csv('C:/Users/Garrett/Python-Armageddon-Project/Armageddon/Datasets/UFO-sightings.csv', sep=r'\s*,\s*', engine='python')
# dtype={
#     "datetime" : str, "city": str, "state": str, "country": str, "shape": str, "duration (seconds)": str, "duration (hours/min)" : str, "comments": str, "date posted": str, "latitude": float, "longitude": float
# })
#datetime,city,state,country,shape,duration (seconds),duration (hours/min),comments,date posted,latitude,longitude
#ufos = pd.read_csv('/Users/garrettmorris/Desktop/database_stuff/ufo_sightings.csv', error_bad_lines=False)

# get mapbox token
# mapbox_access_token = open("/Users/garrettmorris/Desktop/database_stuff/A07/mapbox_token2.txt").read()
mapbox_access_token = "pk.eyJ1IjoiZ2FycmV0dDQzMTEiLCJhIjoiY2t4eXpocTJ5Nm5uYzJubzRwYjcxdWQ0NiJ9.BCXazv5KMTA4_Kuromx2_Q"

# mapbox_style = "mapbox://styles/garrett4311/ck1s78co60uht1crol6lxs6fr"
mapbox_style = "mapbox://styles/mapbox/navigation-night-v1"

# #set the geo spatial data
data = [go.Scattermapbox(
            lat= quake['Latitude'] ,
            lon= quake['Longitude'],
            customdata = quake['EventID'],
            mode='markers',
            marker=dict(
                size= 5,
                color = 'sandybrown',
                opacity = .8,
            ),
            name='Earthquakes'
          )]
data2 = [go.Scattermapbox(
            lat= ufos['latitude'] ,
            lon= ufos['longitude'] ,
            customdata = ufos['datetime'],
            mode='markers',
            marker=dict(
                size= 5,
                color = 'lime',
                opacity = .8,
            ),
            name='UFOs'
          )]
data3 = [go.Scattermapbox(
            lat= volcano['Latitude'] ,
            lon= volcano['Longitude'],
            #customdata = airports['airport id'],
            mode='markers',
            marker=dict(
                size= 5,
                color = 'red',
                opacity = .8,
            ),
            name='Volcanoes'
          )]
#set the layout to plot
layout = go.Layout(autosize=True,
                   mapbox= dict(accesstoken= mapbox_access_token,
                        bearing=0,
                        pitch=0,
                        zoom=5,
                        center= dict(lat=0,lon=0),
                        style=mapbox_style),
                    width=1500,
                    height=1080,
                    title = "Armageddon 2022")

fig = dict (data=data+data2+data3, layout=layout)
plotly.offline.plot(fig, image_filename='test')
