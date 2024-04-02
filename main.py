from website import create_app

app = create_app()

if __name__ == '__main__':  # only runs website if main.py is used
    app.run(debug=True)  # everytime a change is made in python code, it will automatically rerun the server
