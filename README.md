# Smart City web application

## Table of contents
- [Smart City web application](#smart-city-web-application)
  - [Table of contents](#table-of-contents)
  - [General info](#general-info)
  - [Screenshots](#screenshots)
  - [Technologies](#technologies)
  - [Setup](#setup)
  - [Code Examples](#code-examples)
  - [Features](#features)
  - [Status](#status)
  - [Inspiration](#inspiration)
  - [Contact](#contact)

## General info
This project was developed using Python/Django and consists in a system to manage smart cities. It integrates the concept of Internet of Things and Machine Learning to fully automate devices and services in cities.

## Screenshots
![Example screenshot](./img/screenshot.png)

## Technologies
* Python 3.8.6
* Django 3.1.4

## Setup
<!--Describe how to install / setup your local environement / add link to demo version.-->
This consists in a regulat Django project, so to run the server:
```
python manage.py runserver
```

## Code Examples
<!--Show examples of usage:
`put-your-code-here`-->
Up to now only the tests are fully functional. You can run them using

```
python manage.py test iot.tests
```

To keep the same database for every test:
```
python manage.py test iot.tests --keepdb
```

To run one specific test:
```
python manage.py test iot.tests.SensorTestCase
```

## Features
The system currently has the following working features
* Create/update a city
* Create/update a device
* Create/update a resident/ visitor

To-do list:
* Create/update events
* Process transactions
* Authentication services

Where Machine Learning goes in?
* Face recognition system
* Biometric recognition system
* Audio transcription
* Image transcription (not sure exactly how this will work)
* and probably more...
  
## Status
Project is: _in progress_,<!-- _finished_, _no longer continue_ and why?-->

## Inspiration

## Contact
Created by [@euanrussano](https://e-sophia.netlify.app) - feel free to contact me!