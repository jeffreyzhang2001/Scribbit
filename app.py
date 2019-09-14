import os, re
from flask import *
from ocr import ocr
#from entity_seperation import seperate_entities

# INITIALIZATION -----------------------------------------------------------------------------------------------
UPLOAD_FOLDER = 'uploads'
FILE_NAME = ''
ocrtext = ''
#parts = ['topic', 'section', 'olist', 'ulist']

syntax = {
	'#': 'title',
	'##': 'subtitle',
	'-': 'upoint',
	')': 'opoint',
	'*': 'def'
}
rsyntax = dict((b,a) for (a,b) in syntax.items())

seps = ''.join([sep for sep in syntax.keys()])

app = Flask(__name__, static_url_path='/static')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# FUNCTIONS -----------------------------------------------------------------------------------------------
@app.route('/upload', methods = ['POST'])
def upload():
	global FILE_NAME
	if request.method == 'POST':
		f = request.files['file']
		f.save(os.path.join(UPLOAD_FOLDER, f.filename))
		FILE_NAME = f.filename
	return redirect(url_for('display'))

def label(text):
	global syntax, seps
	labelled = []

	titlesecs = re.split(r'^#\s', text)[1:]

	print(titlesecs)

	for titlesec in titlesecs:
		title = titlesec.split('\n')[0]
		subtitlesecs = re.split(r'##\s', titlesec)[1:]

		print(subtitlesecs)

		temp = {
			'text': title,
			'tag': 'title',
			'body': []
		}

		for subtitlesec in subtitlesecs: 
			subtitle = subtitlesec.split('\n')[0]

			temp2 = {
				'text': subtitle,
				'tag': 'subtitle',
				'body': []
				}

			items = subtitlesec.split('\n')[1:]

			for item in items:
				if item != '':
					splitted = item.split(' ')
					first = splitted[0]
					if first.endswith(')'):
						first = first[-1]

					temp3 = {
						'text': ' '.join(splitted[1:]),
						'tag': syntax[first],
					}

					temp2['body'].append(temp3)

			temp['body'].append(temp2)

		labelled.append(temp)

	print(labelled)

	return labelled


# ROUTES -----------------------------------------------------------------------------------------------
@app.route('/')
def index():
	return render_template('/index.html')

@app.route('/display')
def display():
	global UPLOAD_FOLDER, FILE_NAME, ocrtext
	ocrtext = ocr(FILE_NAME)

	info = label(ocrtext)

	return render_template('display.html')#, ocrtext = ocrtext)

@app.route('/about')
def about():
	return render_template('about.html')

# -----------------------------------------------------------------------------------------------

if __name__ == '__main__':
	app.run(debug=True)