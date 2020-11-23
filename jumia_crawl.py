import scrapy


class JumiaCrawl(scrapy.Spider):
    name = "jumia"
    start_urls = ["https://www.jumia.co.ke/"]

    def parse(self, response):
        top_selling_items = response.css("div.reco-w")
        links_of_TopSelling = top_selling_items.css("div.itm a::attr(href)").getall()#get all item link that already in top selling items

        black_friday_items = response.css("div.col16 section.card div.row")
        links_of_BlackFriday = black_friday_items.css("a::attr(href)").getall()
        print("|"*50)
        for i in links_of_BlackFriday:
            print(i)
        print("|"*50)








