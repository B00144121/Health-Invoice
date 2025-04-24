ClinicCare - Patient Invoice Management System

ClinicCare id my django based web application used for managing patients, services, invoices, and payments.


## How to Run the Project (locally)


Clone the repository from github

git clone https://github.com/B00144121/Health-Invoice.git

cd ClinicCare

python -m venv venv

python manage.py migrate

python manage.py runserver then go to http://127.0.0.1:8000/

To load data for testing python manage.py loaddata fixtures/patients.json
python manage.py loaddata fixtures/services.json
python manage.py loaddata fixtures/invoices.json
python manage.py loaddata fixtures/items.json
python manage.py loaddata fixtures/payments.json

python manage.py run server
python manage.py test

