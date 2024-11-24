# Web server

docker build -t web_server:latest .
docker run -d -p 5000:5000 -v /var/www/httpd-cert/admin:/cert --name web_server_container web_server:latest
docker exec -v /var/www/httpd-cert/admin:/cert -ti  --name web_server_container web_server:latest /bin/bash
docker rm web_server_container
docker exec -ti container_name /bin/bash