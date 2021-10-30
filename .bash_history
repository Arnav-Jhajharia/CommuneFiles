sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
git clone https://github.com/Commune-Social/Commune.git
ls
cd Commune/
ls
rm Frontend/
rm -rf Frontend/
ls
rm README.md 
ls
cd ..
l
ls
cd Commune/
ls
cd 
cd B
ls
ccd Commune/
ls
cd Commune/
ls
cd Backend/
ls
cd Commune/
ls
find . -maxdepth 1 -exec mv {} .. \;
ls
cd ..
ls
cd Commune/
ls
cd Commune/
ls
cd ..
ls
cd ..
ls
rm -rf venv
ls
cd C
cd .
ls
cd ..
ls
cd C
cd Backend/
ls
cd Commune/
ls
cd Commune/
ls
find . -maxdepth 1 -exec mv {} .. \;
ls
cd ..
ls
rm -rf Commune
ls
cd ..
ls
cd ..
ls
cd ..
ls
cd Commune/
ls
cd Backend/
find . -maxdepth 1 -exec mv {} .. \;
ls
cd ..
ls
rm -rf Backend
ls
virtualenv env
source myprojectenv/bin/activate
source env/bin/activate
pip3 installl  install django gunicorn psycopg2-binary
pip3 install django gunicorn psycopg2-bi
ls
vim Commune/settings.py
virtualenv envfd
ls
rm -rf envfd
ls
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
sudo ufw status
sudo ufw enable
sudo ufw allow 8000
sudo ufw allow 22
sudo ufw allow 80
gunicorn --bind 0.0.0.0:8000 Commune.wsgi
deactivate
sudo nano /etc/systemd/system/gunicorn.socket
sudo vim /etc/systemd/system/gunicorn.socket
sudo nano /etc/systemd/system/gunicorn.service
sudo vim /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn.socket
file /run/gunicorn.sock
sudo systemctl status gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo nano /etc/nginx/sites-available/myproject
sudo vim /etc/nginx/sites-available/Commune
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo ln -s /etc/nginx/sites-available/Commune /etc/nginx/sites-enabled
sudo nginx -t
cd ..
ls
cd ..
ls
cd ..
ls
cd ..
ls
cd etc
ls
cd nginx
ls
cd sites-available/
sl
ls
cd ..
ls
cd sites-enabled/
rm -rf myproject 
sudo rm myproject 
sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo vim Commune 
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx
ls
cd ..
sl
cd ..
ls
cd ..
sl
ls
cd home
ls
cd ubutnut
ls
cd ubuntu/
l
cd Commune
ls
cd main
lsl
ls
cd templates
ls
vim register.html
sudo apt-get install python3-certbot-nginx
sudo certbot --nginx -d example.com -d www.example.com
sudo certbot --nginx -d www.commune.org.in -d commune.org.in
sudo certbot renew --dry-run
sudo systemctl restart nginx
systemctl restart nginx
sudo systemctl restart nginx
sudo nginx -t
sudo vim etc/nginx/nginx.conf
sudo vim /etc/nginx/nginx.conf
sudo vim /etc/nginx/sites-enabled
sudo vim /etc/nginx/sites-enabled/Commune
sudo ufw status
sudo ufw enable 443
sudo ufw alow 443
sudo ufw allow 443
sudo systemctl restart nginx
sudo ufe disable
sudo ufw disable
