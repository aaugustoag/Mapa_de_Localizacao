import folium
from folium.plugins import LocateControl
import requests
import geopandas as gpds

ende = gpds.tools.geocode(["sabará, mg", "rua ouro branco, 384"])
print (ende[0])

mapa = folium.Map([-16.46, -54.70],
                  zoom_start=5,
                  control_scale=True)

LocateControl(auto_start=True,
              keepCurrentZoomLvel=True,
              drawMarker=True,
              ).add_to(mapa)

folium.Marker(
    location=[45.3311, -121.7113],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="green"),
).add_to(mapa)

mapa.save("mapa.html")