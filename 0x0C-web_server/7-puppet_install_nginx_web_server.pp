# Installs a Nginx server

exec {'install':
  provider => shell,
  command  => 'sudo apt-get update; sudo apt-get install -y nginx; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/Nyakuji permanent;/" /etc/nginx/sites-enabled/default; echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html; sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\n\terror_page 404 \/404.html;\n\tlocation = \/404.html {\n\t\troot \/var\/www\/html;\n\t\tinternal;\n\t}/" /etc/nginx/sites-enabled/default; sudo service nginx restart',
}
