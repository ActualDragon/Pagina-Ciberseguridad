set app="movementanalysis2"
set container="movement_analysis2"
set workingdir=%cd%
docker build --tag %app% .
docker container run --detach  --publish 5060:80 --name %container% --mount type=bind,source="%workingdir%",target=/app %app%
docker cp "./credentials.json" %container%:/credentials
pause
