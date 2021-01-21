#!/bin/bash

docker stop $(docker ps -q --filter ancestor=mopga )
docker build . -t mopga --no-cache
docker run -t -p 8000:8000 mopga:latest &>/dev/null &