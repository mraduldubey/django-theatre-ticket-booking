# django_ecommerce
<p><b> A Django-based backend of an eCommerce web app. It packs all the basic features of a basic eCommerce website i.e. Login, SignUp, Customer Payments, Refunds, Social network integration etc with dynamic web pages having Bootstrap & jQuery support.</b></p>
<h2>Visit it Online</h2>
<a href ="http://mradul.pythonanywhere.com/">mD ecommerce webapp</a>
<h2>To run on Local Machine</h2>
<ul>
<li> Install Python and Django, preferably in a virtualenv</li>
<li> Copy the static folder and save it just outside this repository</li>
<li>Change to directory and run following commands</li>
<li>python manage.py makemigrations</li>
<li>python manage.py migrate</li>
<li> python manahe.py collectstatic</li>
<li> python manage.py runserver</li>
<li> Open browser and go to:http://127.0.0.1:8000/ </li>
</ul>

<h2>Current Features</h2>
<ul>
<li>User SignUp/Login</li>
<li>A fully functional user contact form  on "Contact" page. It notifies the admin of the submission via email(having the user's name,email and message). Also, the submission triggers an autoreply to the user from the admin's gmail account.</li>
<li>Dynamic wepages</li>
<li>Customer Payments through the Donate button on HomePage.</li>
<li>Customer payment recieving in admin's stripe account</li>
<li>Support Bootstrap and jQuery using configured static directory outside of the app repository(for e.g. in virtualenv folder outside of the app repo in my local machine).</li>
<li>Uses both function and class based views.</li>
</ul>

<h2>Upcoming Features</h2>
<ul>
<li>Search Functionality.</li>
</ul>
