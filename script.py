import scrapy
import requests
import get_url


class BlogSpider(scrapy.Spider):
    name = 'spider'
    url = get_url.url
    start_urls = get_url.url#['https://hh.ru/search/resume?clusters=True&area=1&specialization=1&order_by=relevance&search_period=30&logic=normal&pos=position%2Cworkplace_position&exp_period=last_year&exp_company_size=any&exp_industry=any&no_magic=False&st=resumeSearch&text=&fromSearch=true']
    def parse(self, response):
        for resumes in response.css('.resume-search-item__content'):
            link = response.css('a.resume-search-item__name')
            title = resumes.css('::text').get()
            href = resumes.css('::attr(href)').get()
            last_work_plase = resumes.css('.resume-search-item__company-name::text').get()
            yield {
                'title': title,
                'href': href,
                'last_work_plase': last_work_plase,
            }

        for next_page in response.css('a.bloko-button'):
            yield response.follow(next_page, self.parse)