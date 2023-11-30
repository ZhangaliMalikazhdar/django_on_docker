# django
tested on Ubuntu22.04
1) python3.10 (create virtualenv then activate)
2) postgres15 or newer

sudo -i -u postgres psql

create user admin with encrypted password '123';

CREATE DATABASE postgres_db OWNER admin;

GRANT ALL PRIVILEGES on DATABASE postgres_db to admin;

python manage.py makemigrations

python manage.py migrate

pip install -r requirements.txt

#add data

python fill_data.py

#remove data

python empty_db.py

#list orgs

http://127.0.0.1:8000/

#api

http://127.0.0.1:8000/api/organizations/

http://127.0.0.1:8000/api/sanctions/
