# Test Answers

## 1.
pycharm has the option on project creation to create an virtual environment mine was called 'ScrapyTest'
pycharm also auto activates the env running the activate file
once activated the following commands were run:

pip install scrapy==2.4

pip install shub

pip install scrapy-crawlera

pip install google-cloud-storage

pip install scrapy-sessions

this should have been it I was having issues with dependencies for scrapy, so I needed to install the bellow dependecies with a specific version:

pip install Twisted==21.2.0

pip install pyOpenSSL==22.0.0

pip install parsel==1.7.0


Then set up the scrapy project with:

scrapy startproject shopgrokscraper

## 2.

### Spider File
https://github.com/SurlawCitebaid/ScrapyTest/blob/492fca0cc8af08b32374ccb2d040566dc4490903/shopgrokscraper/shopgrokscraper/spiders/tackworldspider.py

Json Output of the Spider:
https://github.com/SurlawCitebaid/ScrapyTest/blob/492fca0cc8af08b32374ccb2d040566dc4490903/shopgrokscraper/tackleworlddata.json

## 3.

### Spider File
https://github.com/SurlawCitebaid/ScrapyTest/blob/492fca0cc8af08b32374ccb2d040566dc4490903/shopgrokscraper/shopgrokscraper/spiders/surfboardspider.py

Json Output of the Spider:
https://github.com/SurlawCitebaid/ScrapyTest/blob/492fca0cc8af08b32374ccb2d040566dc4490903/shopgrokscraper/surfboardempiredata.json 

## 4.
https://github.com/SurlawCitebaid/ScrapyTest/blob/492fca0cc8af08b32374ccb2d040566dc4490903/shopgrokscraper/regextest.py
