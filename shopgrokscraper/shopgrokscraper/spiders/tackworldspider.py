import scrapy

class TackleWorldSpider(scrapy.Spider):
    name = "tackleworld"
    start_urls = ["https://tackleworldadelaide.com.au/"]
    categoryLinks = []

    def parse(self, response):
        #Loop through the navigation bar
        for navItem in response.xpath('//ul[contains(@class, "navPages-list--categories")]/li[@class="navPages-item"]'):

            #Get the sub menu items in each nav item
            subMenuItems = navItem.xpath('ul/li[@class="navPage-subMenu-item"]')
            #Check if there are sub menu items if not append the category link
            if not subMenuItems:
                self.categoryLinks.append(navItem.xpath('div/a|a').attrib['href'])
                continue

            for subMenuItem in subMenuItems:

                # Get the sub menu children in each sub menu item
                subMenuChildren = subMenuItem.xpath('div/ul/li[@class="navPage-childList-item"]')
                # #Check if there are sub menu children if not append the category link
                if not subMenuChildren:
                    self.categoryLinks.append(subMenuItem.xpath('div/a|a').attrib['href'])
                    continue

                #loop through the sub menu children and append the category link
                for subMenuChild in subMenuChildren:
                    self.categoryLinks.append(subMenuChild.xpath('a').attrib['href'])

        #Scrape the data for each category link
        for categoryLink in self.categoryLinks:
            yield scrapy.Request(categoryLink, callback=self.parseCategoryPage, meta={'categoryLink': categoryLink})

    #get all the product data from the category page
    def parseCategoryPage(self,response):
        categoryLink = response.meta['categoryLink']
        products = response.xpath('//li[@class="product"]')

        for product in products:
            yield {
                'Sku_name': product.xpath('.//h4[@class="card-title"]/a/text()').get(),
                'Image_url': product.xpath('.//img[@class="card-image"]/@src').get(),
                'Price_now': product.xpath('.//span[@class="price"]/text()').get(),
                'Price_was': product.xpath('.//span[contains(@class, "price--rrp")]/text()').get(),
                'Product_url': product.xpath('.//h4[@class="card-title"]/a/@href').get(),
            }

        # Follow the next page link within the current category if there are more products for a category
        nextPage = response.xpath('//li[contains(@class,"pagination__item--next")]/a[@class="pagination__link"]/@href').get()
        if nextPage is not None:
            print("nextPage:" + str(nextPage))
            yield response.follow(nextPage, callback=self.parseCategoryPage, meta={'categoryLink': categoryLink})







