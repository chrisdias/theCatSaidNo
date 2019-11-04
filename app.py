from flask import Flask, render_template, send_from_directory
import os
import sys

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route("/")
def home():
    
    # myPlatform = sys.platform
    
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)


