import requests
import string

try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

class GizoogleTranslator:
	def translate(self, inputText):
		try:
			response = requests.post("http://www.gizoogle.net/textilizer.php", data={'translatetext': inputText})
		except:
			return inputText
		translateInput = string.replace(response.text, 'height:250px;"/>', 'height:250px;">',1)
		parsed_html = BeautifulSoup(translateInput, 'html.parser')
		return parsed_html.body.find('textarea', attrs={'name':'translatetext'}).text
	
	def raiseException():
		return 'Sorry. Could not git you, biatch. Betta try some other time. I be busy.'