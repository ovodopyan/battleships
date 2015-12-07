import json

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from battleship import Battleground

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# 1. visit website
#     - get authentication cookie
# 2. create agme
#     - redirect to game creation page with unique link
#     - give link to another player
# 3. play the game


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game/')
def game_create():
    return render_template('game.html')

# @app.route('/game/')
# def index():
#     return render_template('game.html')


@socketio.on('battlegrounds_load')
def battleground_load(data):
    # print "attack field at position {0} by {1}".format(
    #     data.get('position'),
    #     data.get('player_token')
    # )
    player_id = data.get('player')

    b = Battleground()
    fields = b.generate_ships()

    emit('battlegrounds_load_response', json.dumps({'data': fields, 'player_id': player_id}))


if __name__ == '__main__':
    socketio.run(app, debug=True)
