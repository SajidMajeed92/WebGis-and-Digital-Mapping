import folium
import os
import json

# Create map object
m = folium.Map(location=[30.3753, 69.3451], zoom_start=6)

# Global tooltip
tooltip = 'Click For More Info'

# Create custom marker icon
logoIcon = folium.features.CustomIcon('data/logo.png', icon_size=(50, 50))


# Vega data
vis = os.path.join('data', 'vis.json')

# Create markers
folium.Marker([24.8607, 67.0011],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(m),

folium.Marker([25.379167, 68.368333],
              popup='<strong>Location Two</strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),

folium.Marker([24.915806, 67.093152],
              popup='<strong>Location Three</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='purple')).add_to(m),

folium.Marker([24.952101, 67.127094],
              popup='<strong>Location Four</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='green', icon='leaf')).add_to(m),

folium.Marker([24.946437,67.1330186],
              popup='<strong>IST Karachi Location</strong>',
              tooltip=tooltip,
              icon=logoIcon).add_to(m),


folium.Marker([26.946437,68.1330186],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=550, height=300))).add_to(m)


# Generate a map using Folium
m.save('map.html')