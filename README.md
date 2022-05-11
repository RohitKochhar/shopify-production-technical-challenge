# Shopify Production Technical Challenge

- [Shopify Production Technical Challenge](#shopify-production-technical-challenge)
  - [Task](#task)
  - [Solution Overview](#solution-overview)

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
- Ability to create “shipments” and assign inventory to the shipment, and adjust inventory appropriately
- Ability to generate a report on inventory levels over time, like: most in-stock or out-of-stock last month
- Allow for any city in the world to be used as a storage location

## Solution Overview

To meet the above requirements, I implemented a containerized Django application using a tool I developed called (Django Unchained)[https://github.com/RohitKochhar/django-unchained]. The reason I used Django was to develop a scalable and powerful inventory system using Python for more universal readability and development. 

This repository consists of the following file structure:
```
├── app (Contains mostly pre-configured Django configurations, largely unchanged from pre-built Django skeleton app)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py (Mostly used as a command line tool to interface Django with, with commands such as runserver, migrate, etc)
└── tracker (The real meat and value of this app, all developed features are created within this sub-directory)
    ├── __init__.py
    ├── apps.py (Pre-built by Django when a new sub-app is initialized to connect app to database)
    ├── models.py (File containing models that define database object schema)
    ├── templates (Folder containing html templates)
    │   └── tracker 
    │       └── index.html (html file loaded by http://localhost:8000/tracker)
    ├── tests.py (File containing unit tests)
    ├── urls.py (File containing routes between functions found in views.py and http urls)
    └── views.py (Function definition to be used by the app)
```
