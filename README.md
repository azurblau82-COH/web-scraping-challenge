# web-scraping-challenge

Scrape 1 - News Headline
Simple requests / soup code
For some reason the html pulled is not exactly the same as what i'm seeing on the site. The first headline it pulls appears to be dates.
Could'nt make the '/n' go away so I used a .strip('/n')

Scrape 2 
The link to a full size image, actually doesn't really give you a high res image, so I used the one on the site

Scrape 3
Scraping the table, then do some cleaning up

Scrape 4
Tricky, you have to get 4 individual links to new pages to pull the img from. Two step process with for-loops, then pull it back together

scrape_mars.py
I may have made a few more adjustments with respect to the jupyter file
Other than that, basically put it in a def() and create a dictionary to deposit all the scrapes in

app.py
mostly followed code from lesson examples to make the Mongo and Flask bits work
prettied it up the html styling a bit with bootstrap classes

Added two screenshots of how the website looks, the 'scrape new data' works (you can see the chromedriver open/close a  window twice, pretty cool!)
