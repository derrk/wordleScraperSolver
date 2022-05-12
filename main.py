import requests
from bs4 import BeautifulSoup

#res = requests.get("https://medium.com/@owenyin/here-lies-wordle-2021-2027-full-answer-list-52017ee99e86")
def getPage(url):
	res = requests.get(url)
	#print
	if res.status_code == 200:
		return res.content

# read in html file of possible wordle answers
def getHtmlPage(fileName):
	
	with open(fileName) as f:
		data = f.read()

		return data

def getWords(html):
	
	soup = BeautifulSoup(html, "html.parser")

	paragraphs = soup.find_all('p')

	results = []
	
	for par in paragraphs:
		if 'CIGAR' in par.text:
			words = str(par)
			words = words[:-4]
			words = words.split("<br/>")
			
			parts = words[0].split('>')
			words[0] = parts[-1]
			for word in words:
				#print(word[-5:])
				results.append(word[-5:])

	results = list(set(results))
	return results
	


if __name__=='__main__':

	html = getHtmlPage("mediumPage.html")
	words = getWords(html)
	words = sorted(words)
	#print(words)
	badLetters = ['W','E','A','T','O','C','K','Y','R','P']
	#loop through all the words
	for word in words:
		goodWord = True
		#
		for letter in word:
			if letter in badLetters:
				goodWord = False
	if goodWord and word[0] == 'S' and 'U' in word[1:]:
		print(word)

	#paragraphs = soup.find_all('p')


	
