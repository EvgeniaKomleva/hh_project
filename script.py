import scrapy
import get_url
import os


class BlogSpider(scrapy.Spider):
    name = 'spider'
    url = get_url.url
    start_urls = get_url.url
    def parse(self, response):
        for resumes in response.css('.resume-search-item__content'):
            link = response.css('a.resume-search-item__name')
            title = resumes.css('::text').get()
            href = resumes.css('::attr(href)').get()
            last_work_plase = resumes.css('.resume-search-item__company-name::text').get()
            yield {
                'title': title,
                'href': href,
                'last_work_place': last_work_plase,
            }

        for next_page in response.css('a.bloko-button'):
            yield response.follow(next_page, self.parse)

