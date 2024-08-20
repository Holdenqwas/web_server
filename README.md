# Web server

docker build -t web_server:v1 .
docker run -d --name web_server_container web_server:v1

docker rm web_server_container
