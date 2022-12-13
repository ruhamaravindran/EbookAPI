Project name : Ebook_Project
App name : Ebook_App

REQUIREMENTS : Python 3.8 , Django 3.2


####INSTALLATION####

Install using pip

pip install djangorestframework

Add 'rest_framework' to your INSTALLED_APPS setting: 

INSTALLED_APPS = [
...
'rest_framework',
]


####PROCESS####

* Created model Auther,Genre,Ebook
* After creation do makemigrations and migrate
* Created serializers.py file in the App and  created EbookSerializer for the Ebook model.
* Created a class EbookAPIView to get and post the book details

#GET METHOD
   We can return all the objects, only if it is authenticated.
#POST METHOD
   We can create new book if it is valid and it will return the status HTTP_200_CREATED 
   else it will return HTTP_400_BAD_REQUEST.

* EbookAPIView is called in urls.py using the path localhost:8000/ebooks/
Test using localhost:8000/ebooks/.Here it will not return the details if authentication is not done.
So we register using the path localhost:8000/register/ (POST Method).After sending datas a token will be generated with 200 status.
Now if we generate the Ebooks using localhost:8000/ebooks/ (GET Method) ,we can see all the datas.


####READ,UPDATE,DELETE Ebook Details###

Using the path details, path('details/<int:id>/',EbookDetails.as_view()) we can read,update,delete Ebooks.

In EbookDetails class a particular object is get using its unique id.

 If we use get method, the object corresponding to the id will be returned.

 If we use put method, then we can update that object details.

 If we use delete method that object will be deleted.

 If the object does not exist,it will return HTTP_404_NOT FOUND.


To run the project : python manage.py runserver

