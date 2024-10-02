Book scraper for the website https://books.toscrape.com/ and saving in MongoDB

How does it work:
A spider called books_spider who searches for books in the website
It goes through books css file in the websites and takes out their title, price and rating 
and makes it as an item and this item it inserts to the MongoDB

The MongoDB is initialised at the start and where it is located (mongodb://localhost:27017/)
we create a database there mine is called books_db where we stores all the books


How to run the project:
simply open the project and insert the following command in the termilal:
scrapy crawl books

after it´s done connect to the database where it is located (I use for instance MongoDBCompass)
and then you can see the books 
