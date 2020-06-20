## REST Workshop WestSideCoders
Hey there, this is the code used in WestSideCoders' 2020 workshop 'Introduction to the REST architectural style with Flask &amp; Python'.

The code is built off of Flask's quick start manual: https://flask.palletsprojects.com/en/1.1.x/quickstart/.

# Some Definitions
## What is REST?
REST stands for Represenataional State Transfer. It is an a design pattern that treats any object on a server as resources that can be updated, deleted, retrieved. or created. In this way, it standardizes communication between servers.

## What is a REST API?
In essence, it is a HTTP driven API. The GET request is used to retrieve information, the POST request is used to create a resource, the PUT/PATCH request is used to update/patch a resource, and the DELETE request is used to delete a resource. Response payloads are usually in XML, HTML, or JSON.

## What is Flask?
Flask is a light-weight web framework written in Python that we will be using to create a very simple REST API. Flask is considered 'light-weight' or a 'microservice' because the core framework gives us an easy way to define endpoints, handling requests, and building HTTP responses. It is easily extendable, and in this workshop we will be using Flask Restful which is an extension on top of Flask with added support for building REST APIs. This will show you the difference  in manageability of using core Flask and Flask Restful.



