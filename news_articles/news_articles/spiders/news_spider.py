import scrapy
from ..items import NewsArticlesItem

class newsSpider(scrapy.Spider):
    name = 'news'
    start_urls = [
        'https://www.theguardian.com/international',
    ]

    def parse(self, response):
        items = NewsArticlesItem()
        articles = response.css('.fc-item__container').css('div.fc-item__container a').xpath('@href')[0]

        for link in articles:
            abs_url = response.urljoin(link)
            headline = link.css('.dcr-125vfar::text').extract()
            url = link

            items['headline'] = headline
            items['url'] = url

            yield items

        # article_page = urls[0].get()
        # if article_page is not None:
        #     yield response.follow(article_page, callback=self.article_parse(items))
