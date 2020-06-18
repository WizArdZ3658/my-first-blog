# My Blog
My blog website

## Features :-
 * Users can register on the website by filling up a form and activate it by clicking on the activation link sent to
 the user's e-mail address.
 * After signup users can post blogs, like/dislike posts, post comments, etc.
 * Upvote/downvote system in the comment section.
 * Users can use markdown or may use tools from top panel to make blog look more beautiful and presentable. Auto preview
  is also enabled. 
 * Implemented REST API so that users and other applications can use the data (perform CRUD).
 * Implemented pagination for better readability.

 
## Working with the API
 * The API is not public.
 * Create an account first and generate JWT token and pass the token as Authorization header.
 * Check below for example
 
(use HTTPie for the example)

  http POST http://wingman7.pythonanywhere.com/api-token-auth/  username=user password=pass

  http http://wingman7.pythonanywhere.com/api/posts/ "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6IndpbmdtYW43IiwiZXhwIjoxNTkwOTM1MDE3LCJlbWFpbCI6InAuc29tbmF0aDI1OTlAZ21haWwuY29tIn0.jzPIEL02oFnQJI1OjkabhL9Yz4AjC7ClkqMESvY8XsE"

 ## New features to be added :-
 * Improve the backend logic (*need to refine the "approval" system)
 * Will soon develop a desktop application using QT where the users can perform CRUD operations using it.
 
 ## Technology Stack
 ##### Languages :-
Python, HTML, CSS, SQL, Javascript, Git

##### Frameworks, Libraries and Tools:-
AJAX, Bootstrap, Django, PyCharm, JWT, Django REST framework, Django Crispy Forms, Django Pagedown, Django Markdown Deux,
JQuery, Marked.js, SMTP

##### Databases:-
SQLite

##### Environment:-
Windows(my PC), Linux(Deployment server)
