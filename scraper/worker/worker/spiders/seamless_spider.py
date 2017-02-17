import scrapy
from scrapy_splash import SplashRequest

class SeamlessSpider(scrapy.Spider):
  name = "seamless"
  
  def start_requests(self):
    start_urls = ["https://www.seamless.com/menu/majestic-pizza--calzone-8-cortlandt-st-new-york/308933"]
    for url in start_urls:
      yield SplashRequest(
              url=url,
              callback=self.parse,
              endpoint='render.html',
              args={'wait': 10}
            )

  def parse(self, response):
    page = response.url.split("/")[-2]
    filename = 'quotes-%s.html' % page
    with open(filename, 'wb') as f:
      f.write(response.body)
    self.log('Saved file %s' % filename)
