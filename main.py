import os
#import magic
import urllib.request
from app import app
global filename
from flask import Flask, flash, request, redirect, render_template,Response,jsonify, make_response
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	print('In upload form')
	print('filename=',filename)
	return '5'

@app.route('/', methods=['POST'])
def upload_file():
	print('in upload file')
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			print('File successfully uploaded')
			print('In upload form')
			print('filename=',filename)
			return '20'
			#return redirect('/')
			#return make_response('10')
			#res = make_response('10')
			#res.headers['message'] = 'NOt Okay!'
			#return res
		else:
			print('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
			return redirect(request.url)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)
