from flask import Flask, redirect, url_for, request, render_template
from apyori import apriori
import pandas as pd
from apryori import Apryori

app = Flask(__name__)
        

@app.route('/upload',methods = ['POST', 'GET'])
def locomachine():
    if request.method == "POST":
        data = request.files["file"]
        df = pd.read_csv(data)
        return Apryori(df)
    


@app.route('/preload',methods = ['POST', 'GET'])
def preload():
    if request.method == "POST":
        dataset = request.form["predata"]
        if dataset == '1000':
            df=pd.read_csv("Datasets\\1000-out1.csv", header=None)
        elif dataset == '5000':
            df=pd.read_csv("Datasets\\5000-out1.csv", header=None)
        elif dataset == '20000':
            df=pd.read_csv("Datasets\\20000-out1.csv", header=None)
        elif dataset == '75000':
            df=pd.read_csv("Datasets\\75000-out1.csv", header=None)
    return Apryori(df)

if __name__ == '__main__':
   app.run(debug = False)