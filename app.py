import matplotlib
matplotlib.use("Agg")

import boto3
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask,render_template

app = Flask(__name__)
s3 = boto3.client("s3")

@app.route("/")
def index():
    
    obj = s3.get_object(Bucket= "<your-bucket-name>",Key="<csv file_name>")
    with open("/tmp/data.csv","wb") as f:
        f.write(obj["Body"].read())
    df = pd.read_csv("/tmp/data.csv")

    album_counts = df["album"].value_counts().head(5)
    
    plt.figure(figsize=(18,6))
    plt.bar(album_counts.index,album_counts.values)
    plt.xlabel("album")
    plt.ylabel("song")
    plt.savefig("static/chart.png")
    plt.close()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
