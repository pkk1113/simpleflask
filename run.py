from app import create_app



app, sio = create_app()


if __name__ == "__main__":
    sio.run(app, host="0.0.0.0", port=5000)

