#!/bin/bash
app="movementanalysis"
container="movement_analysis"
docker build --tag ${app} .
docker container run --detach \
 --publish 5050:80 --name ${container} \
 --mount type=bind,source=$PWD,target=/app ${app}
docker cp "./credentials.json" ${container}:/credentials