# --------------------------------------------------------
# File Name: tracker/views.py
#
# File Description: Maintains the functions which handle 
#                   the HTTP requests
# 
# --------------------------------------------------------

# Imports ------------------------------------------------
# Package imports
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse, Http404
import os
# Local imports
from .models import Item, CITY_CHOICES

# Functions ----------------------------------------------
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Function Name: index
# 
# Function Description: Loads the main index page 
# 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def index(request):
    # Retrieve all the items in order of the date they were added
    a_LatestItemList    = Item.objects.order_by('-d_DateAdded')

    # Define the context to hand to the HTML template
    context = {
        'a_LatestItemList': a_LatestItemList,
        't_CityList': CITY_CHOICES,
    }

    # Render the index html page with context data
    return render(request, 'tracker/index.html', context)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Function Name: create
# 
# Function Description: Creates an item and adds to db 
# 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def create(request):
    # Get name and location from the html form
    s_Name      = request.POST["s_Name"]
    s_Location  = request.POST.getlist("s_Location")[0]
    i_InventoryCount = int(request.POST["i_InventoryCount"])
    # Create a new object based on the information
    o_CreatedItem = Item.objects.createItem(s_Name, s_Location, i_InventoryCount, datetime.now())
    # Save the item in the database
    o_CreatedItem.save()
    # messages.add_message(request, messages.INFO, 'Hello world.')
    return index(request)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Function Name: edit
# 
# Function Description: Edit specific item 
# 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def edit(request, pk):
    # Get the item in question
    o_Item = get_object_or_404(Item, pk=pk)

    # Create the context item
    context = {
        "o_Item": o_Item,
        "a_Cities": o_Item.s_Location,
        "t_CityList": CITY_CHOICES,
    }
    # Render the edit page with the specific context
    return render(request, 'tracker/edit.html', context)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Function Name: update
# 
# Function Description: Update item from form
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def update(request, pk):
    # Get the updated values from HTML form
    s_Name      = request.POST["s_Name"]
    s_Location  = request.POST.getlist("s_Location")[0]
    i_InventoryCount = int(request.POST["i_InventoryCount"])
    # Load the item
    o_Item = get_object_or_404(Item, pk=pk)
    # Rewrite the item data
    o_Item.s_Name       = s_Name
    o_Item.s_Location   = s_Location
    o_Item.i_InventoryCount = i_InventoryCount
    o_Item.setWeather()
    o_Item.save() 
    # Reload the index
    return index(request)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Function Name: delete
# 
# Function Description: Delete specific item 
# 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def delete(request, pk):
    # Retrieve the object, if not found return 404
    o_Item = get_object_or_404(Item, pk=pk)
    # Delete the item
    o_Item.delete()
    # Reload the index page
    return index(request)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Function Name: export
# 
# Function Description: Exports all product data to csv
# 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def export(request):
    a_LatestItemList    = Item.objects.order_by("-d_DateAdded")
    s_CSVOutput = "Item Name, Item Location, Inventory Count,"
    for o_Item in a_LatestItemList:
        s_CSVOutput += f"\n{o_Item.s_Name},{o_Item.s_Location},{o_Item.i_InventoryCount},"
    print(s_CSVOutput)
    
    return index(request)