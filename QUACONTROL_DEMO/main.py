from app import server
from flask import render_template


@server.route("/")
def load_home():
    return render_template('home.html')

if __name__ == '__main__':
    server.run(host="127.0.0.1", port=2222, debug=True)