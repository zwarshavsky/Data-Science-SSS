# Data-Science-SSS
Flask app that receives song id from the backend and returns the song suggestions
or the visual data from the ML teams database and functions

deployed on heroku at:
http://spotify-song-suggestor.herokuapp.com/

Root page provides basic instructions:

http://spotify-song-suggestor.herokuapp.com/request/<id> (id is song id)
will return 10 suggestions

http://spotify-song-suggestor.herokuapp.com/visual/<id>
will return visual data in base64 format

ut.py holds a simple unittest for the request page
