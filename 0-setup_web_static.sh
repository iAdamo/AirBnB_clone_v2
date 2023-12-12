#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
if ! nginx -v; then
    sudo apt -y update
    sudo apt install -y nginx
fi

# Create the folder /data/web_static/releases/ if it doesn’t already exist
sudo mkdir -p "/data/web_static/releases/test"

# Create the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p "/data/web_static/shared/"

# Create a fake HTML file /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    <h1>Adam is almost a Full Stack Software Engineer</h1>
  </body>
</html>" | sudo tee "/data/web_static/releases/test/index.html" > /dev/null

# a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
search='location / {'
replace='location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\n\t&'
file_path='/etc/nginx/sites-available/default'

sudo sed -i "s|$search|$replace|" "$file_path"

# Restart nginx
sudo service nginx restart
