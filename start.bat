set app="twitter"
set container="twitter"
set workingdir=%cd%
docker build --tag %app% .
docker container run --detach  --publish 5050:80 --name %container% --mount type=bind,source="%workingdir%",target=/app %app%
docker cp "./credentials.json" %container%:/credentials
pause
