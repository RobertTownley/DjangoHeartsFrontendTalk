# Frontend Development for Backend Developers

## Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Structure](#structure)

## Introduction
Until recently, I wrote frontend code like a backend developer. Javascript and jQuery were synonomous. CSS and JS
dependencies were either linked from CDNs or downloaded and shoved into static asset directories. Sub-optimal
architectural decisions, compromises, simplifications, and hacks found their way into my web applications as I worked
around holes in my skill set. I tried to address these deficiencies by repeatedly smacking my head against React
tutorials, but things took a long time to click.

Looking back on this, I think it's because I was (correctly) reluctant to give up the entirety of my workflow as a
backend developer. I'd spent years learning the Python web development ecosystem, and was looking for a more incremental
approach to modernizing my frontend skills than just swapping out pip for npm.

I designed this resource for a specific niche of people: Django developers looking to integrate a host of new and useful
tools into their web applications. I've written it with a former version of myself in mind, but hope that others will
find it useful.

## Requirements
To follow along, I'd recommend that you have moderate familiarity with Django projects.

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
