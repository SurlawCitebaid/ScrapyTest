import scrapy
import json


class SurfBoardSpider(scrapy.Spider):
    name = "surfboard"
    start_urls = ["https://www.surfboardempire.com.au/products.json?page=1"]
    #Just to keep track of what page is being scraped
    pageCounter = 1

    def parse(self, response):
        #Loads loads the response as JSON
        productData = json.loads(response.text)

        #check if the products array is not empty, if it is empty then we have got all products
        if(productData['products']):
            #loop through each product object
            for product in productData['products']:

                #yield the scraped data
                yield {
                    'Sku_name': product['title'],
                    'Product_id': product['id'],
                    'Brand': product['vendor'],
                    'Product_url': 'https://surfboardempire.com.au/products/' + str(product['handle'])
                }

            self.pageCounter += 1
            #Scrape the next page
            yield response.follow("https://www.surfboardempire.com.au/products.json?page=" + str(self.pageCounter), callback=self.parse)


