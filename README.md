# Frontend Development for Backend Developers

## Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Structure](#structure)

## Introduction
This is the starting point for our basic web application. It contains a Django project with a fairly standard structure.

## Installation
First, make a new project directory, create a new virtual environment, and activate the virtual environment
```bash
mkdir -p ~/Projects/ciaoworld
cd ~/Projects/ciaoworld
python3 -m venv venv
source venv/bin/activate
```
Next, pull down this project from GitHub to the current directory and switch to the Level-0 branch
```bash
git clone https://github.com/RobertTownley/Frontend-Dev-for-Backend-Devs.git .
git checkout -b Level-0
git pull origin Level-0
```
Upgrade pip and install the required pip dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Our Project
Level 0 starts off as a fairly standard Django project. A few exceptions to this:
- The project declares a non-app-specific static files directory called `assets` at the project root. This is where
  we'll store things like images and fonts that aren't specific to any one application in the `INSTALLED_APPS` setting.
- Similarly, CSS is stored in a directory called "stylesheets". While neither of these steps are strictly necessary
  right now, getting used to the idea of decoupling static assets from Django applications will make subsequent steps
  easier to follow.
- Page templates are stored in a directory called `templates` at the project root rather than within individual
  applications, for similar reasons to above.

Other than those exceptions, this is a pretty basic Django app:
- There are three views referenced in `ciaoworld/urls.py`: `/home`, `/menu`, and `/contact`
- A versioned Django Rest Framework API, as well as the Django admin, are also declared in `ciaoworld/urls.py` 
- There's a custom application called `menu` containing a `Menu` model, plus an admin and a serializer for that model.

## Structure
This repository contains several branches marked "Level 1", "Level 2", etc. Level 0 starts with a basic Django
application: the website for an Italian restaurant, __Ciao World__. Other levels begin to add new features and utilities
to the application.
Level-1: Adding NPM for static asset dependency management
Level-2: Adding BrowserSync for iterative development 
Level-3: Adding SCSS for CSS transpiling
Level-4: Adding webpack for build process management
Level-5: Adding a Vue component
Level-6: Rebuilding the website frontend with React 
