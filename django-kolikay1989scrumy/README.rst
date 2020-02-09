===================
kolikay1989scrumy
===================

kolikay1989scrumy is a simple Django app to assign goals. For each goal users can add it as a weelky goal or daily goal.,
different users are grouped into differentgroup to perform diffrent functions.

Detailed documentation is in the "docs" directory.

Quick start
------------

1. Add "kolikay1989scrumy" to your INSTALLED APPS setting like this::


    INSTALLED_APPS =[
        ...
        'kolikay1989scrumy',
    ]

2. Include the  kolikay1989scrumy URLconf in your project urls.py like this::
    path('kolikay1989scrumy', include('kolikay1989scrumy.urls')),

3. Run `python manage.py migrate` to create the kolikay1989scrumy models.
4. Start the development server and visit http://127.0.0.1:8000/admin/ to create a jeremiahchukwuscrumy(you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/kolikay1989scrumy/ to see webpage.
6. Admin Login Credentials are(username = "louis", password="DJANGO_123")