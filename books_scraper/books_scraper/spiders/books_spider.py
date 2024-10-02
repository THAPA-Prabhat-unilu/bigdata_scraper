import scrapy
from pymongo import MongoClient

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['http://books.toscrape.com/']

    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client['books_db']
        self.collection = self.db['books']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            title = book.css('h3 a::attr(title)').get()
            price = book.css('p.price_color::text').get()
            rating = book.css('p::attr(class)').get().split()[-1]

           
            item = {
                'title': title,
                'price': price,
                'rating': rating,
            }
            self.collection.insert_one(item)
            yield item
        
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def close(self, reason):
        self.client.close()
