import os
from flask import *
from ocr import ocr
#from entity_seperation import seperate_entities

# INITIALIZATION
UPLOAD_FOLDER = 'uploads'
FILE_NAME = ''

app = Flask(__name__, static_url_path='/static')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# FUNCTIONS
@app.route('/upload', methods = ['POST'])
def upload():
	global FILE_NAME
	if request.method == 'POST':
		f = request.files['file']
		f.save(os.path.join(UPLOAD_FOLDER, f.filename))
		FILE_NAME = f.filename
	return redirect(url_for('display'))

# ROUTES
@app.route('/')
def index():
	return render_template('/index.html')

@app.route('/display')
def display():
	global UPLOAD_FOLDER, FILE_NAME
	#output = ocr(FILE_NAME)

	return render_template('display.html')#, output = output)

if __name__ == '__main__':
	app.run(debug=True)