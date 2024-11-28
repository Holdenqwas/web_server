# Web server

docker build -t web_server:latest .
docker run -d -p 5000:5000 -v /var/www/httpd-cert/admin:/cert --name web_server_container web_server:latest
docker exec -ti web_server_container /bin/bash
docker rm web_server_container
