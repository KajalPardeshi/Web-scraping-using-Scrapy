import scrapy


class ImdbSpiderSpider(scrapy.Spider):
    name = "imdb_spider"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

    def start_requests(self):
        # Pass the custom user agent in the headers of the request
        for url in self.start_urls:
            yield scrapy.Request(url, headers={'User-Agent': self.user_agent}, callback=self.parse)


    def parse(self, response):
        imdb4 = response.css('main div div section div div div ul li')
        for imdb5 in imdb4:
            yield {
                'title': imdb5.css('div div div div a h3 ::text').getall(),
                'year': imdb5.css('div div span ::text').getall(),
                'ratings': imdb5.css('div div div span div span::text').getall()

            }
