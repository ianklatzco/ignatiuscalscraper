from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
# from craigslist_sample.items import CraigslistSampleItem

class IgnCalSpider(Spider):
	name = "igcal"
	allowed_domains = ["ignatius.org"]
	start_urls = ["http://www.ignatius.org/calendar.aspx"]


	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.select("//span[@class='BodyText']")
		# I think this is right. I believe it selects all attributes with a class that = BodyText.
		items = []
		for titles in titles:
			item = CraigslistSampleItem()
			item ["title"] = titles.select("a/td()").extract()
			# I'm not sure what to select here^^^
			# What's the a? What's the td()?
			items.append(item)
		return items

#xpath of the a day/p day td elements
# //*[@id="ctl00_cphMainContent_dgCalendar_ctl04_DataList1"]/tbody/tr[1]/td
# //*[@id="ctl00_cphMainContent_dgCalendar_ctl05_DataList1"]/tbody/tr[1]/td