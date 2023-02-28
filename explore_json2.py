import json

infile = open('eq_data_30_day_m1.json','r')      #reading from file
outfile = open('readable_eq_data.json','w')     #creating new output file

eq_data = json.load(infile)                 #json.load() formats the object 'eq_data' as the type of 'infile' contents, dictionary here 

json.dump(eq_data, outfile, indent=5)   #indent=5 argument tells dump() to format the data using the data's structure

#print the type of object and no. of earthquakes (28-feb class)
print(f"The data type is : {type(eq_data)}")

list = eq_data['features']  #the value of 'key =features' is a list


print(f"The no. of earthquakes: {len(list)}")

#create a list of mags, lats, lons
mags, lats, lons, hover_texts = [], [], [], []

for eq in list:         #list is 'list of dictionaries' we will iterate through a dict
    if eq['properties']['mag']>5:   #to get only mag>5 data appended and printed on map
        mag = eq['properties']['mag']
        lon = eq['geometry']['coordinates'][0]
        lat = eq['geometry']['coordinates'][1]
        title = eq['properties']['title']     #to get titles when we hover on the dots on graph

        mags.append(mag)
        lats.append(lat)
        lons.append(lon)
        hover_texts.append(title)


print(mags[:10])        #will print 10 values (index 0-9)
print(lats[:10])
print(lons[:10])

#using plotly
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#data = Scattergeo(lon=lons,lat=lats)    #menthod to create a map view

#below menthod is to create a map view with more data against each plot

data = [{'type':'scattergeo', 
         'lon':lons, 
         'lat':lats,
         'text':hover_texts, 
         'marker':
            {'size': [5*mag for mag in mags],
             'color': mags,
             'colorscale':'Viridis',
             'reversescale':True,
             'colorbar':{'title':'Magnitude'}
             }
        }]    #mag is a iterator here, mags is our list

my_layout = Layout(title="Global Earthquakes")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='global_earthquakes.html')










