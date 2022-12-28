from bs4 import BeautifulSoup
import time
import requests
from playsound import playsound



i=0
while True:
	url = requests.get('https://jeemain.nta.nic.in/')
	print(url.content)
	soup = BeautifulSoup(url.text, 'html.parser')

	soup = str(soup.prettify())
	# tags=soup.find()sub
	# print(soup)
	# soup = str(soup)
	# f=open('html.txt','w',encoding="utf-8")
	# f.write(soup.split('\n')[440])
	# f.close()
	# print(soup.find("div", {"class": "slides"}))
	# print(soup.split('\n')[441])
	txt = str(soup.split('\n')[440])
	print(f'\n                                              {txt}')
	if txt.strip() !="NATIONAL TESTING AGENCY JEE – 2022 (Session 2) – PROVISIONAL FINAL KEY B.E/B.Tech.(Paper I)":
		f=0
		while f < 4:
			f=f+1
		playsound('buzzer.mp3')
	else:
		i=i+5
		print(f'hfffffffff {i}')
		playsound("beep_beep.mp3")

	time.sleep(300)
