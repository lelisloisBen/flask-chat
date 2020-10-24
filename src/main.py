from flask import Flask, request, jsonify, render_template, make_response, redirect
import os
from flask_cors import CORS
from utils import APIException
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app)

# app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'

CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sessions():
    return render_template('session.html')

@socketio.on("message")
def handleMessage(data):
    emit("new_message",data,broadcast=True)


if __name__ == "__main__":
    socketio.run(app, debug=True, port=5004)

# def messageReceived(methods=['GET', 'POST']):
#     print('message was received!!!')

# @socketio.on('my_event')
# def handle_my_custom_event(json, methods=['GET', 'POST']):
#     print('received my_event: ' + str(json))
#     socketio.emit('my_response', json, callback=messageReceived)




# @app.route('/')
# def hello_world():
#     return "<div style='text-align: center; background-color: orange'><h1>Backend running...</h1><br/><h3>Welcome back samir</h3><img src='https://media.gettyimages.com/photos/woman-sitting-by-washing-machine-picture-id117852649?s=2048x2048' width='80%' /></div>"


# this only runs if `$ python src/main.py` is executed
# if __name__ == '__main__':
#     PORT = int(os.environ.get('PORT', 3000))
#     app.run(host='0.0.0.0', port=PORT, debug=False)