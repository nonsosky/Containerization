#!/usr/bin/env bash

# build image
docker build --tag=api .

#list docker image
docker image ls

#Run flask app
docker run -p 800=5001 api
