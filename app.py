import os
import cv2
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
	# getting the width and height from both input fields
 	width = int(request.form['width'])
 	height = int(request.form['height'])

 	# getting the uploaded image
 	image_file = request.files['file']

 	# securing image file
 	filename = secure_filename(image_file.filename)

 	# saving the uploaded image file
 	image_file.save(os.path.join('static/', filename))

 	# opening the image file
 	image = Image.open(image_file)

 	# resizing the uploaded image
 	image.thumbnail((width, height))

 	# saving the resized image into the static folder
 	image.save(os.path.join('static/', filename))

 	# returning the resized image to the webpage
 	return render_template('upload.html', filename=filename)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))

if __name__ == '__main__':
    app.run(debug=True)