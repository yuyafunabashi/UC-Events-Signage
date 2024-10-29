# Dockerized Flask Web App for Union Church piSignage

## Overview
A dockerized web app based on Python using Flask and MongoDB
The app features:
- A main page for the Signage
- An admin page to add and delete events (TODO: Add better CRUD functionality)
- A Settings page to customize Header, font, color, spacing, sizing, e.t.c (INCOMPLETE)

## Requirements
- Docker
- Docker Compose

## Setup Instructions
1. Clone the Repo
```
git clone git@github.com:yuyafunabashi/UC-Events-Signage.git
cd UC-Events-Signage.git
```

2. Run Docker Compose
```
docker compose up --build
```

## Default Ports
Web App: `5000`

Mongo DB: `27017`

## Application Overview
### Page for piSignage
URL: `/`

### Admin Page
URL: `/admin`

### Settings Page
URL: `/settings`
