import numpy as np
import pandas as pd
import plotly
import plotly.offline as offline
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

#import csv file
quake = pd.read_csv('/Users/garrettmorris/Desktop/database_stuff/earthquakes.csv')
airports = pd.read_csv('/Users/garrettmorris/Desktop/database_stuff/airports.csv', error_bad_lines=False)
ufos = pd.read_csv('/Users/garrettmorris/Desktop/database_stuff/ufo_sightings.csv', error_bad_lines=False)

#get mapbox token
mapbox_access_token = open("/Users/garrettmorris/Desktop/database_stuff/A07/mapbox_token2.txt").read()

mapbox_style = "mapbox://styles/garrett4311/ck1s78co60uht1crol6lxs6fr"

# #set the geo spatial data
data = [go.Scattermapbox(
            lat= quake['latitude'] ,
            lon= quake['longitude'],
            customdata = quake['earthquake_id'],
            mode='markers',
            marker=dict(
                size= 4,
                color = 'orange',
                opacity = .8,
            ),
          )]
data2 = [go.Scattermapbox(
            lat= ufos['latitude'] ,
            lon= ufos['longitude'],
            customdata = ufos['datetime'],
            mode='markers',
            marker=dict(
                size= 4,
                color = 'blue',
                opacity = .8,
            ),
          )]
data3 = [go.Scattermapbox(
            lat= airports[' latitude'] ,
            lon= airports[' longitude'],
            #customdata = airports['airport id'],
            mode='markers',
            marker=dict(
                size= 4,
                color = 'green',
                opacity = .8,
            ),
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
                    title = "Armageddon")

fig = dict (data=data+data2+data3, layout=layout)
plotly.offline.plot(fig, image_filename='test')
