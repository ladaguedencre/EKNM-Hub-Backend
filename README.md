# EKNM Hub

## Introduction

EKNM Hub is a private web service used by EKNM organization for various projects. This repository is a backend of a publicly available website. It's not meant for copying or reusing as a whole, but some code parts or architectural decisions may be useful.

More details about EKNM, as well as this code running, are available at [eknm.in](https://eknm.in)
 
## Running backend

This project uses Flask framework and can be run simply by `python3 main.py` command.

Alternatively docker can be used:  
`docker build -t hub-backend .`  
`docker run -dp 127.0.0.1:PORT:5003 hub-backend`

## More details

Visit [frontend repo page](https://github.com/ladaguedencre/EKNM-Hub) to read more about this project
