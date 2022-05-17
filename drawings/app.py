import os
import uuid

import numpy as np
import cv2

from flask import Flask, jsonify, render_template, request


app = Flask(__name__)
app.secret_key = "my_little_pony"
app.debug = False
app._static_folder = os.path.abspath("templates/static/")
static_images_png = "templates/static/images/"


def create_csv(text):
    unique_id = str(uuid.uuid4())
    with open(get_file_name_csv(unique_id), "a") as file:
        file.write(text[1:-1] + "\n")
    return unique_id

def create_png(unique_id):
    text = get_file_content(get_file_name_csv(unique_id))
    data = [float(i) for i in text.strip('[]').split(',')]
    data = np.reshape(data, (300, 300))
    cv2.imwrite(get_file_name_png(unique_id), data)


def get_file_name_csv(unique_id):
    return f"images_csv/{unique_id}.csv"

def get_file_name_png(unique_id):
    return f"{static_images_png}{unique_id}.png"

def get_file_content(filename):
    with open(filename, "r") as file:
        return file.read()


@app.route("/", methods=["GET"])
def index():
    title = "Create the input image"
    return render_template("layouts/index.html",
        title=title)


@app.route("/results/", methods=["GET"])
def results():
    title = "Results"
    link_start = "http://127.0.0.1:5000/static/images/"
    images_links = [link_start + f for f in os.listdir(static_images_png) if os.path.isfile(os.path.join(static_images_png, f))]
    return render_template("layouts/results.html",
        title=title,
        links=images_links)


@app.route("/results/<unique_id>", methods=["GET"])
def result_for_uuid(unique_id):
    title = "Result"
    create_png(unique_id)
    return render_template("layouts/result.html",
        title=title,
        imgdata=f"static/images/{unique_id}.png")


@app.route("/postmethod", methods=["POST"])
def post_javascript_data():
    js_data = request.form["canvas_data"]
    unique_id = create_csv(js_data)
    params = {"unique_id": unique_id}
    return jsonify(params)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
