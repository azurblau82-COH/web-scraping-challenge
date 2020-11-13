from bs4 import BeautifulSoup
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape ():
    mars_dict={}

    #section 1
    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    result = soup.find('div', class_="content_title")

    news_title = result.a.text
    news_title=news_title.strip('\n')

    mars_dict['news_title']=news_title

    news_p = soup.find('div', class_='rollover_description_inner').text
    news_p=news_p.strip('\n')
    # news_p

    mars_dict['news_p']=news_p

    #section 2

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find('div', class_='carousel_container')
    link = result.find('a', class_='fancybox')

    image_url = link['data-fancybox-href']
    home = "https://www.jpl.nasa.gov"

    featured_image_url = home + image_url

    mars_dict['featured_image_url']=featured_image_url

    browser.quit()

    #section 3
    mars_fact_url = 'https://space-facts.com/mars/'

    tables = pd.read_html(mars_fact_url)
    mars_table = tables[0]
    mars_table.columns=['Description','Mars']
    mars_table_index=mars_table.set_index('Description')
    mars_table_html = mars_table_index.to_html()
    mars_table_html_clean = mars_table_html.replace('\n','')
    mars_table_html_clean1 = mars_table_html_clean.replace('text-align: right','text-align: left')
    mars_table_html_clean2 = mars_table_html_clean1.replace('table border="1" class="dataframe"','table class="table table-striped table-bordered table-sm"')
    
    
    mars_dict['table']=mars_table_html_clean2

    #section 4
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_hemi_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemi_url)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find('div', class_='collapsible')
    hemispheres = results.find_all('h3')

    names = []
    for x in hemispheres:
        y=x.text
        z=y.strip('Enhanced')
        names.append(z)

    description = results.find_all('div', class_='description')
    links=[]

    for x in description:
        link = x.find('a')['href']
        url = "https://astrogeology.usgs.gov"
        full_link = url + link
        links.append(full_link)
    # In[26]:


    full_img = []

    for x in links:
        
        url = x
        browser.visit(url)    
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        result = soup.find('div', class_='downloads')
        img_url = result.find('a')['href']
        full_img_url = img_url
        full_img.append(full_img_url)
    #full_img

    #zip it up to put in dict
    zipit = zip(names, full_img)
    hemisphere_image_url=[]
    for x ,y in zipit:
        diction={}
        diction['title']=x
        diction['img_url']=y
        hemisphere_image_url.append(diction)
    #hemisphere_image_url
    
    browser.quit()

    mars_dict['hemisphere']=hemisphere_image_url

    return (mars_dict)
