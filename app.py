import os, re, json
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
	'*': 'def',
	'=>': 'eq'
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

	joined = ' '.join(text.split('\n'))

	titlesecs = re.split(r'(^|\s)#\s', text)[2:]

	print(titlesecs)

	for titlesec in titlesecs:
		title = titlesec.split('\n')[0]
		subtitlesecs = re.split(r'\s##\s', titlesec)[1:]

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

			inOList = False
			inUList = False

			for item in items:			
				if item != '':
					splitted = item.split(' ')
					first = splitted[0]
					if first.endswith(')'):
						first = ')'

					try:
						tag = syntax[first]
					except:
						tag = 'other'

					# list grouping
					if tag == 'opoint':
						if inUList == True:
							temp2['body'].append(temp3)
							inUList = False

						if inOList == False:
							tagtype = 'olist'
							
							temp3 = {
								'tag': tagtype,
								'body': [{
									'text': item,
									'tag': tag
								}]
							}
							inOList = True
						else:
							temp4 = {
								'text': item,
								'tag': tag
							}
							temp3['body'].append(temp4)
					elif tag == 'upoint':
						if inOList == True:
							temp2['body'].append(temp3)
							inOList = False

						if inUList == False:
							tagtype = 'ulist'

							temp3 = {
								'tag': tagtype,
								'body': [{
									'text': item,
									'tag': tag
								}]
							}
							inUList = True
						else:
							temp4 = {
								'text': item,
								'tag': tag
							}
							temp3['body'].append(temp4)
					else:
						if inUList == True:
							temp2['body'].append(temp3)
							inUList = False
						elif inOList == True:
							temp2['body'].append(temp3)
							inOList = False

						temp3 = {
							'text': ' '.join(splitted[1:]),
							'tag': tag
						}
						inOList = False
						inUList = False
					
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

	# f = open('test.txt', 'w+')
	# f.write(ocrtext)
	# f.close()

	# TESTING ---------
	h = open('test.txt', 'r')
	notes = h.read()

	# info = label(ocrtext)
	info = label(notes)

	with open('test.json', 'w+') as g:
		json.dump(info, g)

	return render_template('display.html', ocrtext = info)

@app.route('/about')
def about():
	return render_template('about.html')

# -----------------------------------------------------------------------------------------------

if __name__ == '__main__':
	app.run(debug=True)