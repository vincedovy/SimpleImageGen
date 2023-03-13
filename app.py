import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        image_prompt = request.form["image_prompt"]
        response = openai.Image.create(
          prompt=image_prompt,
          n=4,
          size="256x256"
        )
        return render_template("index.html",
            result1=response['data'][0]['url'],
            result2=response['data'][1]['url'],
            result3=response['data'][2]['url'],
            result4=response['data'][3]['url'])

    result = request.args.get("result1")
    return render_template("index.html", result1=result)
