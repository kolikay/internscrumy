===================
jeremiahchukwuscrumy
===================

jeremiahchukwuscrumy is a simple Django app to assign goals. For each goal users can add it as a weelky goal or daily goal.

Detailed documentation is in the "docs" directory.

Quick start
------------

1. Add "jeremiahchukwuscrumy" to your INSTALLED APPS setting like this::


    INSTALLED_APPS =[
        ...
        'jeremiahchukwuscrumy',
    ]

2. Include the  jeremiahchukwuscrumy URLconf in your project urls.py like this::
    path('jeremiahchukwuscrumy', include('jeremiahchukwuscrumy.urls')),

3. Run `python manage.py migrate` to create the jeremiahchukwuscrumy models.
4. Start the development server and visit http://127.0.0.1:8000/admin/ to create a jeremiahchukwuscrumy(you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/jeremiahchukwuscrumy/ to see webpage.
6. Admin Login Credentials are(username = "louis", password="DJANGO_123")