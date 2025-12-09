docker network create -d bridge tplb
docker build -t im-nginx-lb ./tp-a/
mkdir -p shared1 shared2
echo "<h1>Hello 1</h1>" > shared1/index.html
echo "<h1>Hello 2</h1>" > shared2/index.html

docker run -d \
	--name nginx1 \
	--rm \
	--network tplb \
	-p 81:80 \
	-v "$(pwd)/shared1:/usr/share/nginx/html" \
	nginx:latest

if [ $? != 0 ]
then
	echo "erreur, fini"
	exit 1
fi

docker run -d --name nginx2 --rm --network tplb -p 82:80 -v "$(pwd)/shared2:/usr/share/nginx/html" nginx


docker run -d --name nginx-lb --network tplb -p 83:80 im-nginx-lb



