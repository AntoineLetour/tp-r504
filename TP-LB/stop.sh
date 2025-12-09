docker stop nginx-lb nginx1 nginx2 2>/dev/null
docker rm nginx-lb nginx1 nginx2 2>/dev/null
docker network rm tplb 2>/dev/null