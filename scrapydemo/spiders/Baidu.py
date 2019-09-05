import scrapy

from scrapydemo.items import DetailItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = [
        'baidu.com'
    ]

    start_urls = [
        'http://tieba.baidu.com/f?kw=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB&ie=utf-8'
    ]

    def parse(self, response):
        # 分析网页代码
        # quotes  = response.css('.quotes')

        # 遍历数据
        for line in response.xpath('//li[@class=" j_thread_list clearfix"]'):
            # 初始化item对象保存爬取的信息
            item = DetailItem()
            # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
            item['title'] = line.xpath(
                './/div[contains(@class,"threadlist_title pull_left j_th_tit ")]/a/text()').extract()
            item['author'] = line.xpath(
                './/div[contains(@class,"threadlist_author pull_right")]//span[contains(@class,"frs-author-name-wrap")]/a/text()').extract()
            item['reply'] = line.xpath(
                './/div[contains(@class,"col2_left j_threadlist_li_left")]/span/text()').extract()
            yield item
