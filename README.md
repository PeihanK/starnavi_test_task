Starnavi Test Task

This project is a basic API that allows users to register, log in, manage posts, manage comments, and interact with 
automated replies. Additionally, it includes features like profanity check and analytics for comment activity.

Features Implemented:
User Registration:

1 Users can register by providing a username, email, and password. There is also a password confirmation field.
Usernames must be alphanumeric or contain an underscore _.
Password validation is in place to ensure strong security.
The registered users are saved with hashed passwords.
User Login:

2 Users can log in using their email and password.
Upon successful login, users receive JWT tokens (access_token and refresh_token), which are stored as HTTP-only cookies.
Invalid credentials or disabled accounts result in appropriate error messages.
Post Management API:

3 Users can create, view, and delete posts.
Each post belongs to a user and is stored with relevant details.
Comment Management API:

4 Users can add comments to posts.
Comments are associated with posts and users.
Comments can be retrieved for individual posts.
Profanity and Abuse Check:

5 All posts and comments are checked for profanity or abusive language upon creation.
If any abusive or profane content is detected, the post or comment is blocked and not stored.
Analytics API:

6 An API endpoint /api/comments-daily-breakdown has been implemented to retrieve analytics for the number of 
comments created in a specified date range.
The analytics return the total number of comments as well as the number of blocked comments, aggregated by day.

7 Automated Replies on Comments:
Users can enable automatic replies on comments for their posts.
The automatic reply is triggered after a delay specified by the user.
The reply content is relevant to both the post and the comment, ensuring that it is meaningful.


1 Clone the repository:

git clone https://github.com/your-username/starnavi_test.git

2 Navigate into the project directory:

cd starnavi_test

3 Create and activate a virtual environment:

python -m venv .venv

Activate the virtual environment:

Win: .venv\Scripts\activate

Mac/Linux: source .venv/bin/activate

4 Install dependencies from requirements.txt:

pip install -r requirements.txt

5 Apply database migrations:

python manage.py migrate

6 Run the development server:

python manage.py runserver

The server will now be accessible at http://127.0.0.1:8000.


