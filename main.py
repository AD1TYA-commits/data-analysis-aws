import matplotlib
matplotlib.use("Agg")

import csv
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv("data/data.csv")
    album_counts = df["album"].value_counts().head(5)
    
    plt.figure(figsize=(18,6))
    plt.bar(album_counts.index,album_counts.values)
    plt.xlabel("album")
    plt.ylabel("song")
    plt.savefig("static/chart.png")
    return render_template("index.html")

app.run(debug=True)

