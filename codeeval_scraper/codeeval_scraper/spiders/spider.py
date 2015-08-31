from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from codeeval_scraper.items import CodeevalScraperItem


base_url = "https://www.codeeval.com/open_challenges/"

start_urls = []

class CodeSpider(Spider):

    name = "codeeval_scraper"
    allowed_domains = ["www.codeeval.com"]

    start_urls = start_urls

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        table_easy = hxs.xpath('//*[@id="example"]/tbody/')
        table_med = hxs.xpath('//*[@id="example2"]/tbody/')
        table_hard = hxs.xpath('//*[@id="example3"]/tbody/')

        items = []
        for row in rows:
                item = CodeevalScraperItem()
                item['level'] = row.xpath("").extract()
                item['name'] = row.xpath("").extract()
                item['passed'] = row.xpath("").extract()
                items.append(item)
        return items


# xpath easy //*[@id="main"]/div[1]/div[4]/div/div[1]/ul/li[2]/div[2]/div[2]
# xpath mod  //*[@id="main"]/div[1]/div[4]/div/div[1]/ul/li[3]/div[2]/div[2]
# xpath mod 1st item //*[@id="example2"]/tbody/tr[2]

# xpath hard //*[@id="main"]/div[1]/div[4]/div/div[1]/ul/li[4]/div[2]/div[2]

# xpath hard table //*[@id="example3"]

# xpath easy table 1st row //*[@id="example"]/tbody/tr[1]
# xpath medium table 1st row //*[@id="example2"]/tbody/tr[1]
# xpath hard table 1st row //*[@id="example3"]/tbody/tr[1]




req_cookies = {'django_language': 'en',
               'sessionid': '981b3d44cfcd72413380f974c7e75c67',
                'mp_super_properties': '%7B%22all%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A//github.com/%22%2C%22%24initial_referring_domain%22%3A%20%22github.com%22%7D%2C%22events%22%3A%20%7B%7D%2C%22funnels%22%3A%20%7B%7D%7D'
}