import scrapy
from ..items import ProductItem

taken_urls = []

class ProductsSpider(scrapy.Spider):
    name = 'product_spider'
    allowed_domains = ['coolblue.be']
    
    def start_requests(self):
        urls = [
            'https://www.coolblue.be/nl/ons-assortiment', # Starting page
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_main_page)


    def parse_main_page(self, response):
        
        nav_links = response.css('li.category-navigation--item a::attr("href")') # Collect all the urls from each category

        for nav_link in nav_links:
            nav_link = response.urljoin(nav_link.extract())
            yield scrapy.Request(url=nav_link, callback=self.parse_intermediary_page)

    def parse_intermediary_page(self, response):
        try:
            
            intermediary_page = response.css('a.visual-entrance-card.text-align-center.js-visual-entrance-card')
            product_div = response.css('.product.js-product')
            
            next_url = response.css('li.pagination__item.pagination__item--arrow:last-child a.pagination__link.js-pagination-item::attr("href")')
                            
            if next_url: # Check if there is a next page
                next_url = response.urljoin(next_url[0].extract())
                yield scrapy.Request(url=next_url, callback=self.parse_intermediary_page)

            if intermediary_page: 
                
                '''

                Checks if the page has a similar structure to this: https://www.coolblue.be/nl/screenprotectors/screenprotectors-voor-mobiele-telefoons/voor-apple
                If it does it will collect each url from each type in order to get to the products page

                '''

                try:
                    links = response.css('a.visual-entrance-card.text-align-center.js-visual-entrance-card::attr("href")')
                    for link in links:
                        link = response.urljoin(link.extract())
                        yield scrapy.Request(url=link, callback=self.parse_intermediary_page) 
                except Exception as error:
                    self.logger.error('Error checking intermediary page: ' + str(error), response.url)
            elif product_div:

                '''

                Checks if the page has a similar structure to this: https://www.coolblue.be/nl/screenprotectors/screenprotectors-voor-mobiele-telefoons/voor-apple-iphone-xr
                It will collect the data inside each (product_div) [Product Price, Product Promotional Price, URL]

                '''

                try:
                    
                    
                    products = product_div
                    for product in products:
                        product_price = product.css('span.sales-price__former::text').extract_first()

                        if product_price: # If there is no promotional price, the product will be skipped

                            product_promotional_price = product.css('.sales-price__current::text').extract_first().replace('-', '00') + '€'
                            product_url = response.urljoin(product.css('a.product__title.js-product-title::attr("href")').extract_first())
                            product_price = product_price.replace('-', '00').replace('Nieuwprijs', '').replace(' ', '') + '€'
                            
                            if product_url not in taken_urls: # If url is not in (taken_urls) list, it means it is not a duplicate and can be stored
                                
                                taken_urls.append(product_url)
                                item = ProductItem()
                                item['url'] = product_url
                                item['promotional_price'] = product_promotional_price
                                item['price'] = product_price.replace('-', '00').replace('Nieuwprijs', '').replace(' ', '')
                                yield item

                            else:

                                continue

                except Exception as error:
                    self.logger.error('Error in checking product page: ' + str(error), response.url)

        except Exception as error:
            self.logger.error('Error in finding divs page: ' + str(error), response.url)


            
        
