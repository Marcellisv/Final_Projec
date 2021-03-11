# import necessary libraries
from flask import Flask, render_template
import os


# create instance of Flask app
app = Flask(__name__)

# Create route that renders index.html template
@app.route("/")
def index(): 

    # Return template and data
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)