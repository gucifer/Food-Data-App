# Food-Data-App
This project is made with React(Frontend) and Flask(Backend). It uses the sponacular API and Tasty API from buzzfeed.

## Instructions to run the app

1. Go to the sponacular Directory and start the sponacular server.

### `flask run ./sponacular_api/app.py`

2. Go to the Tasty Directory and start the tasty server.

### `flask run ./tasty_backend/app.py`

The above two servers are responsible for interacting with two APIs and reformat the data into a simpler format so that it is easier to use for the react app.

Before starting the Frontend React Server, You need to replace all the sample replies reply{}.json and reply variables in react with GET requests from the server. Once you have done that:\
\
3. In order to start the frontend App,go to the project directory and run:

### `npm start`
