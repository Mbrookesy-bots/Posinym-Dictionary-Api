# [COMPLETE] Posinym-Dictionary-Api CURRENTLY NOT LIVE

This API is to interact with the Posinym Twitter Bot.

## Trying the API.

### With the Bot

Simply @Posinym the bot with a sentence on twitter and it will respond back with an automatic antonym reply.

![alt-text](https://i.imgur.com/Ki6ww1z.png "example reply")

### Without the Bot

Remember to import your database as `dictionary.sqlite` or use the database dump provided in the repo.

You can run the API locally using the following commands within your command line.

- `export FLASK_APP=routes.py` - this will set the environment variable `FLASK_APP` to where the api will run from.

- `flask run` - make sure you run this within the src folder and it should run the api, the command line should also have the localhost url to hit.

#### Endpoints locally

- **GET**    `/dictionary` - Get word details using the word query parameter. 
Will return the same word back if the word given does not currently exist in the database e.g.

/dictionary?word=happy outputs:
`{
  "antonym": "sad",
  "word": "happy"
}`

/dictionary?word=the outputs:
`{
  "antonym": "the"
}`
