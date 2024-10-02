Book scraper for the website https://books.toscrape.com/ and saving in MongoDB<br />
Contents:<br />
books_scraper folder with the spider in it<br />
books_db.books json file which was exported from mongodb compass which has all the books scraped by me<br />

How does it work:<br />
A scrapy project called books_scraper<br />
A spider called books_spider who searches for books in the website<br />
It goes through books css file in the websites and takes out their title, price and rating 
and makes it as an item and this item it inserts to the MongoDB<br />

The MongoDB is initialised at the start and where it is located (mongodb://localhost:27017/)<br />
we create a database there mine is called books_db where we stores all the books<br />


How to run the project:<br />
simply open the project and insert the following command in the termilal:<br />
scrapy crawl books<br />

after it´s done connect to the database where it is located (I use for instance MongoDBCompass)<br />
and then you can see the books <br />
