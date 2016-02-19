#newlinkedbot
import argparse, os, time
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_until_visible_then_click(browser,element):
    element = WebDriverWait(browser,5,poll_frequency=.2).until(
        EC.visibility_of(element))
    element.click()

def ViewBot(browser,keywords,number):
	count = 0
	page_num = 1
	links = []
	time.sleep(random.uniform(1.5, 3.7))
	while True:
		if(number and count>=number):
			break
		url = 'https://www.linkedin.com/vsearch/p?orig=FCTD&rsid=4049415991455723736683&keywords={}&trk=vsrp_people_sel&trkInfo=VSRPsearchId%3A4049415991455723718955,VSRPcmpt%3Atrans_nav&openFacets=N,G,CC&f_G=gb%3A0&f_N=S&page_num={}&pt=people'.format(keywords,page_num)
		browser.get(url)
		time.sleep(random.uniform(2.5, 4.7))
		buttons = browser.find_elements_by_link_text("Connect")
		num_buttons = len(buttons)
		if num_buttons == 0:
			break
		index = 0
		while True:
			wait_until_visible_then_click(browser,buttons[index])
			time.sleep(random.uniform(0.5, 1.1))
			if(browser.current_url != url):
				browser.get(url)
				buttons = browser.find_elements_by_link_text("Connect")
			else:
				count+=1
				if(number and count>=number):
					break
			index+=1
			if(index>=len(buttons)):
				break
		page_num += 1
		if num_buttons < 10:
			break

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("email", help="linkedin email")
	parser.add_argument("password", help="linkedin password")
	parser.add_argument("keywords", help="linkedin keywords")
	parser.add_argument("number", help="linkedin number")
	args = parser.parse_args()
	keywords = args.keywords.replace(" ", "%20")
	print(keywords)
	number = None
	if int(args.number)>0:
		number = int(args.number)

	browser = webdriver.Chrome()
	browser.get("https://www.linkedin.com/uas/login")

	emailElement = browser.find_element_by_id('session_key-login')
	emailElement.send_keys(args.email)
	passElement = browser.find_element_by_id('session_password-login')
	passElement.send_keys(args.password)
	passElement.submit()

	os.system('cls')
	print "[+] Success! Logged In, Bot Starting!"
	ViewBot(browser,keywords,number)
	browser.close()

if __name__ == "__main__":
	Main()