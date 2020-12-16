# coralbot

This is a Scrapy-splash project to scrape images from coralnet.ucsd.edu

This project is only meant for educational purposes.

# Requirements

to work with this you need to install all libs from requirements.txt

    pip install -r requirements.txt

also you need to have preinstalled **docker** and run next commands

#### Linux
    $ sudo docker pull scrapinghub/splash
    $ sudo docker run -it -p 8050:8050 --rm scrapinghub/splash
    
#### Windows
    docker pull scrapinghub/splash
    docker run -it -p 8050:8050 --rm scrapinghub/splash

after that everything should work. You can start crawling with

    scrapy crawl coralnet-css
    
###***Good Luck***