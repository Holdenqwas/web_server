# Web server

docker build -t web_server:latest .
docker run -d -p 5000:5000 --name web_server_container web_server:v1

docker rm web_server_container
