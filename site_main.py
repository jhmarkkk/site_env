from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', title='Homepage', active_nav='home_nav')

@app.route("/about")
def about():
    return render_template('about.html', title='About', active_nav='about_nav')

if __name__ == '__main__':
    app.run()