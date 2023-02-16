from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    data = response.json()
    return render_template("index.html", blog=data)

@app.route('/<int:num>')
def about_blog(num):
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    data = response.json()
    return render_template("post.html", blog=data, number=num)

if __name__ == "__main__":
    app.run(debug=True)
