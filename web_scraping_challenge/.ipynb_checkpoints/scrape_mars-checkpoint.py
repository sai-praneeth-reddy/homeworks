# Dependencies

import pandas as pd

from bs4 import BeautifulSoup

from splinter import Browser

import requests

import time

import warnings

warnings.filterwarnings('ignore')


def init_browser():
    
    # Location of chrome driver, Windows user must update the pathe
    
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    browser = init_browser()


    ## 1. NASA MARS NEWS ##

    #URL of page to be scraped

    url = 'https://mars.nasa.gov/news/'

    browser.visit(url)

    time.sleep(3)

    html = browser.html

    #Create BeautifulSoup object; parse with 'html.parser'

    soup = BeautifulSoup(html, 'html.parser')

    #Extract the Relevant information

    Mars = soup.find('li',class_="slide")

    news_title = Mars.find('div',class_="bottom_gradient").text

    news_p = Mars.find('div', class_="rollover_description_inner").text


    ## 2. JPL MARS SPACE IMAGES ##

    #URL of page to be scraped

    url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(url_image)

    #Get the url for Full Size Image

    browser.click_link_by_partial_text('FULL IMAGE')

    browser.click_link_by_partial_text('more info')

    html_image = browser.html

    #Create BeautifulSoup object; parse with 'html.parser'

    soup_image = BeautifulSoup(html_image, 'html.parser')

    #Extract the Relevant information

    Image = soup_image.find('meta', property="og:image")

    featured_image_url = Image['content'] 

    ## 3. Mars Weather ##

    #URL of page to be scraped

    url_weather = 'https://twitter.com/marswxreport?lang=en'

    browser.visit(url_weather)

    time.sleep(3)

    html_weather = browser.html

    # Create BeautifulSoup object; parse with 'html.parser'

    soup_weather = BeautifulSoup(html_weather, 'html.parser')

    mars_weather = soup_weather.find_all('div', class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0")[0].text


    ## 4.  MARS FACTS ##

    #URL of page to be scraped

    url_facts = 'https://space-facts.com/mars/'

    browser.visit(url_facts)

    html_facts = browser.html

    #Extract the table

    tables = pd.read_html(url_facts)

    Facts = tables[0]

    Facts.columns = ['Variable Name', 'Value']


    ## 5. MARS HEMISPHERE ##

    url_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(url_hemi)

    html_hemi = browser.html

    # Extract the results

    url_list = []

    hemisphere_image_urls = []

    soup_hemi = BeautifulSoup(html_hemi, 'html.parser')

    results = soup_hemi.find_all("div", class_="item")

    for result in results:
    
        url_partial = result.find('a')['href']
    
        final_url = f'https://astrogeology.usgs.gov{url_partial}'
    
        url_list.append(final_url)
    
    for url in url_list:
    
        browser.visit(url)
        
        html = browser.html

        soup = BeautifulSoup(html, 'html.parser')
    
        #Extract Image URL
    
        results1 = soup.find_all('a', target="_blank")

        Image = results1[3]['href']
    
    
        # Extract the title
    
        results2 = soup.find('title').text
    
        head = results2.rsplit(' ', 6)[0]
    
    
        # Append to the list
    
        hemisphere_image_urls.append({"title":head, "img_url":Image})


    ## STORE IT IN DICTIONARY ##

    mars_vars = {"news_title": news_title, "news_p": news_p, "featured_image_url": featured_image_url,
    "mars_weather": mars_weather, "facts": Facts, "hemisphere_image_urls": hemisphere_image_urls}

    # quit browser after scraping

    browser.quit()

    return mars_vars

if __name__ == '__main__':
    
    scrape()






