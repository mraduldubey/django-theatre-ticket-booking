# django-theatre-ticket-booking
Django based web app which implements ticket booking for multiple screen theatre(s).

## Working Screenshots
- Overview

![Overview](overview.gif?raw=true "Overview")

- Authentication

![Authentication](authentication.gif?raw=true "Authentication")

- Booking

![Booking](booking-1.gif?raw=true "Booking")

## Installation Pre-requisites:
To install following dependencies:

- django
- crispy-forms
- allauth
- stripe

Use:
```
sudo pip install -r requirements.txt
```

## Usage:
- Clone the repo
```
git clone https://github.com/mraduldubey/django-theatre-ticket-booking
```
- Install Pre-Requisites
```
sudo pip install -r requirements.txt
```
- Change to /project directory
```
cd project
```
- Run this command
```
python manage.py runserver
```
- Open a browser and go to 127.0.0.1:8000

## Important Notes:

- Always ensure that DB has appropriate entries before you try to book tickets. Case in point, make sure you have added Seats for a show for the movie Today (system time).
If not, go to: ```127.0.0.1:8000/admin``` to add the seats and try again.

- Features like Contact-Us and the Autoreply will work only when you have configured email settings of the admin in **project/ecommerce/settings.py**:
```
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'replace with email of the admin here'
EMAIL_HOST_PASSWORD = 'passwordxxxforxxxxthexxxxemail'
EMAIL_PORT = '587'
```  
- For Autoreply functionality configure similar settings in **contact/autoreply.py**:
```
def autoreply(toaddr):
	"""Send reply to contact submission."""

	fromaddr = "replace with email of admin here."
	the_pwd = "passwordxxxforxxxxthexxxxemail"
  ...
  ```

## Authors

* **Mradul Dubey** - *django-theatre-ticket-booking* - [MradulDubey](https://github.com/mraduldubey)

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE License - see the [LICENSE.md](LICENSE?raw=true "LICENSE") file for details.
