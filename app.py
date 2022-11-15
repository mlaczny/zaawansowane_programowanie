# importing flask
from flask import Flask, render_template

# importing pandas module
import pandas as pd


app = Flask(__name__)

# route to html page - "table"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies')
def movies():
# reading the data in the csv file
    df = pd.read_csv('movies.csv')
    df.to_csv('movies.csv', index=None)
    data = pd.read_csv('movies.csv')
    return render_template('csv_table.html', tables=[data.to_html()], titles=[''])

@app.route('/links')
def links():
    df = pd.read_csv('links.csv')
    df.to_csv('links.csv', index=None)
    data = pd.read_csv('links.csv')
    return render_template('csv_table.html', tables=[data.to_html()], titles=[''])

@app.route('/ratings')
def ratings():
    df = pd.read_csv('ratings.csv')
    df.to_csv('ratings.csv', index=None)
    data = pd.read_csv('ratings.csv')
    return render_template('csv_table.html', tables=[data.to_html()], titles=[''])

@app.route('/tags')
def tags():
    df = pd.read_csv('tags.csv')
    df.to_csv('tags.csv', index=None)
    data = pd.read_csv('tags.csv')
    return render_template('csv_table.html', tables=[data.to_html()], titles=[''])

if __name__ == "__main__":
    app.run(host="localhost", port=int("5001"))