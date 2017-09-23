import requests
url = 'https://github.com/kennethreitz/requests/'
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("https://www.fanfiction.net/s/10004326/1/The-Very-Best")
#get html from url above

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content, "html.parser")
result= soup.find("div", {"id": "storytext"})
print(result.prettify())
#parse contents with beautifulsoup and print only the text under "storytext" id
