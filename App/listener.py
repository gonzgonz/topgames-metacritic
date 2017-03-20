from flask import Flask, abort
from topgames import topgames
import json

app = Flask(__name__)

# Define the first method to retrieve the gamelist of top PS4 Games
@app.route('/games', methods=['GET'])
def allgames():

   # Call our topgames function to get the gamelist of the 'Top PS4 games by Metascore'
    gamelist = topgames()

   # Build response and set the right mimetype header
    response = app.response_class(
        response = json.dumps(gamelist, indent = 2),
        status = 200,
        mimetype = 'application/json'
    )

    # Return our pretty printed JSON response
    return response


# Define the second method to retrieve only the given Game Title as <game_title>
@app.route('/games/<game_title>', methods=['GET'])
def singlegame(game_title):

    gamelist = topgames()

    # Grab only the object we called
    game = [ g for g in gamelist if g['title'] == game_title ]

    # Do some error handling
    if game == []:
        abort(404)
    else:
        game = game[0]
    
    # Build response and set the right mimetype header
    response = app.response_class(
        response = json.dumps(game, indent = 2),
        status = 200,
        mimetype = 'application/json'
    )

    # Return our pretty printed JSON response
    return response


# Run the webapp on port 8888
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
        port=8888,
    )
