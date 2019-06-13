from flask import Flask
from flask_restful import Api
from flask_socketio import SocketIO, emit


def create_app(conf=None):
    app = Flask(__name__)
    if conf is not None:
        app.config.from_pyfile(conf)
    
    api = Api(app)
    from app.api.home import HomeAPI
    api.add_resource(HomeAPI, HomeAPI.URI)

    sio = SocketIO(app)
    
    @sio.on("connect")
    def connect():
        print("연결되었음")
        print("connected")

    @sio.on("disconnect")
    def disconnect():
        print("disconnected")

    @sio.on("ping")
    def on_ping():
        print("ping")
        emit("pong")

    @sio.on("hi")
    def on_hi():
        print("hi")
        emit("hello")

    return app, sio

