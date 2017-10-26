#! /bin/bash


docker-machine rm -f Char
docker-machine create -d virtualbox Char
eval $(docker-machine env Char)
docker-machine ip Char
