# To extract the youtube trailer link of a movie

import urllib3
from bs4 import BeautifulSoup
import re
from mechanize import Browser
import json
import requests
from bs4 import BeautifulSoup
from requests import get
import pandas as pd
from urllib.parse import urlparse
import httplib2
import urllib.request
import sqlite3
import re
import sys


def if_webpage_exists(url):

	requested_web_page = requests.get(url)

	if (requested_web_page.status_code == 200):
		return 1
	return 0


def extract_data(url):

	with urllib.request.urlopen(url) as response:
		contents = response.read()

	return contents 
 

### To extract the movie trailer page on youtube
def get_movie_trailer_page(movie):

	movie_dup = movie.replace(' ', '+')

	youtube_link = "https://www.youtube.com/"
	movie_url = youtube_link + "results?search_query=" + movie_dup

	return movie_url


### To extract the movie trailer
def extract_movie_trailer_link(movie):

	movie_link_to_be_parsed = get_movie_trailer_page(movie)

	data = extract_data(movie_link_to_be_parsed)
	soup = BeautifulSoup(data, features="html5lib")

	for link in soup.find_all('a'):
		if ('/watch?v=' in link.get('href')):
			return "https://www.youtube.com" + link.get('href')


#print(extract_movie_trailer_link(sys.argv[1]))


def main():

	movie = input("Please enter the movie of your choice: \n")
	result = extract_movie_trailer_link(movie)

	print('\n' + result)


main()