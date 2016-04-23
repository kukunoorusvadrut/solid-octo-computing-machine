from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    # 10fastfingers.com
# typing.lk
# typing.com/games
# typingclub.com
# import the magic random picker

# list of things to pick from
typing_options = ['abc', 'def', 'ghi']

# find a way to pick something
typing_choice = typing_options[1]

# a way to tell the user what to do
print typing_choice

if __name__ == "__main__":
    # go get the PORT from the environment
    port = os.environ.get("PORT")
    # run the app with the port and bind to any ip
    app.run(
      "0.0.0.0"
    , port
    )
