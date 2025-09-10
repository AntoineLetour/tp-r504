docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker image prune
docker container prune
docker network prune
docker volume prune
