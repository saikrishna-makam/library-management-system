# Library Management System
Simple Flask REST API for Library Management System

## The resources served by the API are
* [User](#User)
* [Book](#Book)

## User
HTTP methods implemented by User resource
* GET - Fetch all users or single user if id is specified.
* POST - Add new user in the system
* PUT - Update the already present user with new properties
* DELETE - Remove the specified user

## Book
HTTP methods implemented by User resource
* GET - Fetch all books or single book if id is specified.
* POST - Add new book in the system
* PUT - Update the already present book with new properties
* DELETE - Remove the specified book

## Accessing the API
### For User 
* Use http://hostname/users with GET and POST HTTP method to fetch or add users in system.
* Use http://hostname/user/{int:id} with GET, PUT and DELETE method to fetch, update or delete specified user in system.

### For Book
* Use http://hostname/books with GET and POST HTTP method to fetch or add books in system.
* Use http://hostname/book/{int:id} with GET, PUT and DELETE method to fetch, update or delete specified book in system.
