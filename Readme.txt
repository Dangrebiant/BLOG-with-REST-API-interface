README

This is a blog project with basic API interface added.


API interface created using djangorestframework (http://www.django-rest-framework.org/)
Token authorization is created using djangorestframework-jwt 

___________________________________
Frameworks is used in the project:
 - django 1.9.8
 - djangorestframework 3.4.1
 - djangorestframework-jwt 1.8.0
 
 ___________________________________
Functionality:

 - Creating new user
 - Login, Logout functions
 - Creating new posts (authentication required)
 - Retirieving all posts
 - Retirieving posts created by authenticated user
 - Updating posts created by authenticated user
 - Deleting posts created by authenticated user
 - Standard admin functionality
______________________________________
URL Structure of the project:

    USER INTERFACE
        admin/
        posts/ -  Main page of the blog
	posts/# - Details of the post (/api/posts/6)
	posts/#/edit - Updating the post (/api/posts/1/edit)
        accounts/login/ - Login page.
        accounts/logout/ - Logout session
        accounts/register/ - New user registration
    API INTERFACE
        api/posts/ - List of all posts 
        api/posts/my - List of all posts of current user
        api/posts/# - Details of the post (/api/posts/6)
	api/posts/#/edit - 
        api/users/register - Creating new user
 _____________________________________       
 Functions:

    PAGINATION 
        available for /api/posts/ and /api/posts/my
     
        ?limit=# - limits number of posts to be displayed on the page.
        (Example:  /api/posts/?limit=3    - returns 3 posts per page)
        
        ?offset=# - returns page starting from item.number
        (Example: /api/posts/?limit=2&offset=4 - returns 2 items starting from -5th post) 
     
    TOKEN AUTHORIZATION and CURL ACCESS
	*You may have CURL been installed prior to try the following in terminal:

	POST LIST VIEW (allowed for any):
	Default pagination limit is set by 5.
	Last 5 posts:
		curl http://127.0.0.1:8000/api/posts/
	last 10 posts:
		curl http://127.0.0.1:8000/api/posts/?limit=10
	second page:
		curl http://127.0.0.1:8000/api/posts/?offset=5
	"?limit=#&offset=#" are not working together in curl.
	
	RECEIVING TOKEN:
	curl -X POST -d "username=admin&password=password123" http://127.0.0.1:8000/api/auth/token/

	MY POSTS:
	"<TOKEN>" - to be substituted with token
	curl -H "Authorization: JWT <TOKEN>" http://127.0.0.1:8000/api/posts/my/
	Example:           curl -H "Authorization: JWT seyJhbGciOiJIUz..." http://127.0.0.1:8000/api/posts/my/

	CREATE NEW POST:
	"<TOKEN>" - to be substituted with token
	curl -X POST -H "Authorization: JWT <TOKEN>" -H "Content-Type: application/json" -d"{\"title\":\"YOUR TITLE TO BE PASTED HERE\", \"content\":\"YOUR CONTENT TO BE PASTED HERE\"}" http://127.0.0.1:8000/api/posts/create/?type=post

_________________________________________
References:
	Django - high level Python Web framework  - http://www.djangoproject.com
	Django REST Framework - toolkit for building Web APIs - http://www.django-rest-framework.org/
	REST framework JWT Auth - JSON Web Token Authentication for DjangoRestFramework - getblimp.github.io/django-rest-framework-jwt/



