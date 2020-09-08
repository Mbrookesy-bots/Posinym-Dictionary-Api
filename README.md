# Posinym-Dictionary-Api

This API is to interact with the Posinym Twitter Bot.

## Trying the API.

### With the Bot

STILL A WORK IN PROGRESS

### Without the Bot

Remember to import your database as `dictionary.sqlite` or use the database dump provided in the repo.

You can run the API locally using the following commands within your command line.

- `export FLASK_APP=routes.py` - this will set the environment variable `FLASK_APP` to where the api will run from.

- `flask run` - make sure you run this within the src folder and it should run the api, the command line should also have the localhost url to hit.

#### Current endpoints locally

- **GET**    `/dictionary` - Get all dictionary entries
- **POST**   `/dictionary` - Create a new entry via json
- **GET**    `/dictionary/<id>` - Get a word by id
- **PUT**    `/dictionary/<id>` - Update a word by id
- **DELETE** `/dictionary/<id>` - Delete a word by id
