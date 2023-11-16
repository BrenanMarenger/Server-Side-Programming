from flask import *
import re
import urllib
from difflib import get_close_matches
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
	return render_template('wordSearch.html')

@app.route("/search", methods=['POST', 'GET'])
def index():
	searchWord = request.get_json()
	print(searchWord)
	link = "https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"
	wordFile = urllib.request.urlopen(link)
	words = wordFile.read()
	wordString = words.decode("utf-8")
	matches = re.findall(".*" + searchWord + ".*", wordString)
	closeMatches = get_close_matches(searchWord, matches, 10, 1)
	topWords = []
	counter = 0
	for w in matches:
		topWords.append(w)
		counter = counter + 1
		if counter > 9:
			break
	result = ','.join(topWords)
	print(result)
	return jsonify(result)

if __name__ == '__main__':
   app.run('0.0.0.0',  port=8089, debug = True)
