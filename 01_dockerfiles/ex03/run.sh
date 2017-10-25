#! /bin/bash

docker-machine ip Char
echo "set bdd type with SQLite3 "
echo "set localhost with the ipadress of Char"
echo "give all informations in admin account setting"
docker run -it -p 3000:3000 gogs
