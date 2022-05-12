# --------------------------------------------------------
# File Name: tracker/models.py
#
# File Description: This file contains classes representing
#                   database models
# 
# --------------------------------------------------------

# Imports ------------------------------------------------
# Package imports
from django.db import models
import requests

# Global Variables ---------------------------------------
HALIFAX     = "HALIFAX"
TORONTO     = "TORONTO"
VANCOUVER   = "VANCOUVER"
WATERLOO    = "WATERLOO"
MONTREAL    = "MONTREAL"

CITY_CHOICES = (
    (HALIFAX, "Halifax"),
    (TORONTO, "Toronto"),
    (VANCOUVER, "Vancouver"),
    (WATERLOO, "Waterloo"),
    (MONTREAL, "Montreal"),
)

# Class definitions --------------------------------------
# --------------------------------------------------------
# Class Name: ItemManager
#
# Class Description: Manages all instances of Item to create
#                    edit or delete items
# 
# --------------------------------------------------------
class ItemManager(models.Manager):
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    # Function Name: createItem
    # 
    # Function Description: Takes info from form to return created
    #                       item model
    # 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    def createItem(self, s_Name, s_Location, i_InventoryCount, d_DateAdded):
        o_Item = self.create(s_Name=s_Name, s_Location=s_Location, i_InventoryCount=i_InventoryCount, d_DateAdded=d_DateAdded)
        o_Item.setWeather()
        return o_Item

# --------------------------------------------------------
# Class Name: Item
#
# Class Description: Object to model the items being 
#                    tracked in by the system 
# 
# --------------------------------------------------------
class Item(models.Model):
    s_Name      = models.CharField(max_length=200)
    s_Location  = models.CharField(  max_length=50, 
                                     choices=CITY_CHOICES,
                                     default="HALIFAX" 
    )
    s_Weather   = models.CharField(max_length=200, default="ERROR")
    d_DateAdded = models.DateTimeField('date added')
    i_InventoryCount = models.PositiveIntegerField(default=0)
    
    def setWeather(self):
        # Note: Typically, I'd make this secret, but since the app 
        #       should run via replit, I am hard-coding it in here
        #       instead
        API_KEY = "b98aab9c600862c47057fa07cb6aeec6"
        # Geocode the city name to get the coordinates
        s_GeocodeAPICall = f"http://api.openweathermap.org/geo/1.0/direct?q={self.s_Location}&limit=5&appid={API_KEY}"
        o_Response = requests.get(s_GeocodeAPICall)
        s_Lat   = o_Response.json()[0]["lat"]
        s_Long  = o_Response.json()[0]["lon"]
        # Generate weather API call from lat and long
        s_WeatherAPICall = f"https://api.openweathermap.org/data/2.5/weather?lat={s_Lat}&lon={s_Long}&appid={API_KEY}"
        o_Response = requests.get(s_WeatherAPICall)
        d_Weather = o_Response.json()['weather'][0]
        d_Main    = o_Response.json()['main']
        # Generate textual description with result
        self.s_Weather = f"Feels like {round(d_Main['feels_like'] - 273, 2)} degrees, with {d_Weather['description']}"

    objects = ItemManager()
