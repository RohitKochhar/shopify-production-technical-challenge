# Shopify Production Technical Challenge

- [Shopify Production Technical Challenge](#shopify-production-technical-challenge)
  - [Usage](#usage)
    - [replit](#replit)
    - [Docker](#docker)
  - [Task](#task)
  - [Solution Overview](#solution-overview)
    - [models.py](#modelspy)
    - [urls.py](#urlspy)
    - [views.py](#viewspy)

## Usage

### replit

The replit for this repository can be found here: https://replit.com/@RohitKochhar/shopify-production-technical-challenge#.replit

Using replit, this app can be launched by doing the following:

1. Press the run button. Sometimes the run button doesn't seem to trigger the `bash run.sh` script to launch the app. If this is the case, simply enter `bash run.sh` in the repl.it shell directly.
2. Navigating to [https://shopify-production-challenge.rohitkochhar.repl.co/tracker/ ](https://shopify-production-technical-challenge.rohitkochhar.repl.co/tracker/)in another tab.

**Note that the in-repl browser will not load the correct url, as it will be missing the /tracker/ suffix.**

### Docker

Using Docker to run this app is much easier, simply run:

```
docker build -t production_challenge .
docker run -p 0.0.0.0:8000:8000 -t production_challenge
```

and navigate to http://localhost:8000/tracker


## Task

Build an inventory tracking web application for a logistics company. We are looking for a web application that meets the requirements listed below:

- Basic CRUD Functionality. You should be able to:
  - Create inventory items
  - Edit Them
  - Delete Them
  - View a list of them
- Additional requirements:
  - Each inventory item should be associated with a city where the item is stored
  - There are only 5 possible cities used for storage, which can be hard-coded into the application
  - The list of items in the inventory must include the city and a simple textual description of the current weather

Along with the above requirements, one of the following features must also be implemented:
- Push a button export product data to a CSV
- Allow image uploads AND store image with generated thumbnails
- When deleting, allow deletion comments and undeletion
- Filtering based on fields/inventory count/tags/other metadata
- Ability to assign/remove inventory items to a named group/collection
- Ability to create warehouses/locations and assign inventory to specific locations
- Ability to create ???shipments??? and assign inventory to the shipment, and adjust inventory appropriately
- Ability to generate a report on inventory levels over time, like: most in-stock or out-of-stock last month
- Allow for any city in the world to be used as a storage location

## Solution Overview

To meet the above requirements, I implemented a containerized Django application using a tool I developed called [Django Unchained](https://github.com/RohitKochhar/django-unchained). The reason I used Django was to develop a scalable and powerful inventory system using Python for more universal readability and development. 

This repository consists of the following file structure:
```
????????? app (Contains mostly pre-configured Django configurations, largely unchanged from pre-built Django skeleton app)
???   ????????? __init__.py
???   ????????? asgi.py
???   ????????? settings.py
???   ????????? urls.py
???   ????????? wsgi.py
????????? manage.py (Mostly used as a command line tool to interface Django with, with commands such as runserver, migrate, etc)
????????? tracker (The real meat and value of this app, all developed features are created within this sub-directory)
    ????????? __init__.py
    ????????? apps.py (Pre-built by Django when a new sub-app is initialized to connect app to database)
    ????????? models.py (File containing models that define database object schema)
    ????????? templates (Folder containing html templates)
    ???   ????????? tracker 
    ???       ????????? index.html (html file loaded by http://localhost:8000/tracker)
    ????????? tests.py (File containing unit tests)
    ????????? urls.py (File containing routes between functions found in views.py and http urls)
    ????????? views.py (Function definition to be used by the app)
```

### models.py
- In  this file, I implement 2 classes:
  - **Item**
    - This is a simple class inheriting from the base Django Model to ensure easy and flexible integration into the application and its database.
    - Any relevent metrics, characteristics or parameters for the tracked items can be implemented here as class variables.
    - This class also contains a class method `setWeather` which uses the OpenWeather Geocoding API to return the latitude and longitude from the given location string, which can then be used to retrieve the weather information, which is formatted into a textual description as required by the project brief.
  - **ItemManager**
    - This is a simple class inheriting from the base Django Manager class.
    - This class is responsible for the management of all **Item** instances, and controls their creation. The creation is implemented by this class in place of overriding the `__init__` class method to ensure the flexible integration of the base Django Model is not comprimised.
  
### urls.py
- This small file acts as the bridge between our HTTP requests generated by the HTML views and their corresponding functions implemented in `views.py`
- Each item in `urlpatterns` maps a HTTP action name to a function and request URL to pass any required parameters.

### views.py
- This file contains the majority of the functionality of the app.
- As mentioned above, HTTP requests generated by the HTML views are passed through `urls.py` and associated with a function defined in this file. 
- Besides for HTTP request handlers, there are functions within this app that route the web traffic to a specific HTML page, while providing said page with relevent context to display.