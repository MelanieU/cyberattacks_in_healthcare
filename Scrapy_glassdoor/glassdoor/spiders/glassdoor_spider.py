from scrapy import Spider, Request
from glassdoor.items import GlassdoorItem
import re

class GlassdoorSpider(Spider):
	name = 'glassdoor_spider'

	allowed_urls = ['https://www.glassdoor.com/']
	start_urls = ['https://www.glassdoor.com/']

	def parse(self, response):

		result_urls = ["https://www.glassdoor.com/Overview/Working-at-City-of-Farmington-NM-EI_IE665372.11,32.htm",
						"https://www.glassdoor.com/Overview/Working-at-AHCA-EI_IE41744.11,15.htm",
						"https://www.glassdoor.com/Overview/Working-at-South-East-Alaska-Regional-Health-Consortium-EI_IE634972.11,55.htm",
						"https://www.glassdoor.com/Overview/Working-at-Onco360-EI_IE964733.11,18.htm",
						"https://www.glassdoor.com/Overview/Working-at-Adams-Health-Network-EI_IE884998.11,31.htm",
						"https://www.glassdoor.com/Overview/Working-at-Hancock-Regional-Hospital-EI_IE121713.11,36.htm",
						"https://www.glassdoor.com/Overview/Working-at-Singing-River-Health-System-EI_IE672078.11,38.htm",
						"https://www.glassdoor.com/Overview/Working-at-Partners-HealthCare-EI_IE6284.11,30.htm",
						"https://www.glassdoor.com/Overview/Working-at-Smith-Dental-EI_IE1724350.11,23.htm",
						"https://www.glassdoor.com/Overview/Working-at-Decatur-County-General-Hospital-EI_IE1632723.11,42.htm",
						"https://www.glassdoor.com/Overview/Working-at-University-of-Virginia-Health-System-EI_IE19755.11,47.htm",
						"https://www.glassdoor.com/Overview/Working-at-FastHealth-EI_IE1351010.11,21.htm",
						"https://www.glassdoor.com/Overview/Working-at-greyhealth-group-EI_IE17361.11,27.htm",
						"https://www.glassdoor.com/Overview/Working-at-Primary-Health-Care-EI_IE702406.11,30.htm",
						"https://www.glassdoor.com/Overview/Working-at-St-Peter-s-Hospital-EI_IE306840.11,30.htm",
						"https://www.glassdoor.com/Overview/Working-at-ATI-Physical-Therapy-EI_IE299225.11,31.htm",
						"https://www.glassdoor.com/Overview/Working-at-Finger-Lakes-Health-EI_IE853044.11,30.htm",
						"https://www.glassdoor.com/Overview/Working-at-CareFirst-BlueCross-BlueShield-EI_IE269607.11,41.htm",
						"https://www.glassdoor.com/Overview/Working-at-Guardian-Pharmacy-EI_IE342332.11,28.htm",
						"https://www.glassdoor.com/Overview/Working-at-Texas-Health-Resources-EI_IE7647.11,33.htm",
						"https://www.glassdoor.com/Overview/Working-at-UnityPoint-Health-EI_IE18460.11,28.htm",
						"https://www.glassdoor.com/Overview/Working-at-Center-for-Orthopaedic-Specialists-EI_IE1184436.11,45.htm",
						"https://www.glassdoor.com/Overview/Working-at-Sangamo-Therapeutics-EI_IE11523.11,31.htm",
						"https://www.glassdoor.com/Overview/Working-at-Billings-Clinic-EI_IE17438.11,26.htm",
						"https://www.glassdoor.com/Overview/Working-at-The-Oregon-Clinic-EI_IE264257.11,28.htm",
						"https://www.glassdoor.com/Overview/Working-at-LifeBridge-Health-EI_IE21518.11,28.htm",
						"https://www.glassdoor.com/Overview/Working-at-Allied-Physicians-Group-EI_IE1159475.11,34.htm",
						"https://www.glassdoor.com/Overview/Working-at-Aultman-Health-Foundation-EI_IE18927.11,36.htm",
						"https://www.glassdoor.com/Overview/Working-at-MyHeritage-EI_IE765167.11,21.htm",
						"https://www.glassdoor.com/Overview/Working-at-RISE-WI-EI_IE1947812.11,18.htm",
						"https://www.glassdoor.com/Overview/Working-at-Elmcroft-Senior-Living-EI_IE651530.11,33.htm",
						"https://www.glassdoor.com/Overview/Working-at-HealthEquity-Inc-EI_IE199470.11,27.htm",
						"https://www.glassdoor.com/Overview/Working-at-Med-Associates-EI_IE653608.11,25.htm",
						"https://www.glassdoor.com/Overview/Working-at-Black-River-Medical-Center-EI_IE1833449.11,37.htm",
						"https://www.glassdoor.com/Overview/Working-at-CarePartners-EI_IE453635.11,23.htm",
						"https://www.glassdoor.com/Overview/Working-at-Humana-EI_IE340.11,17.htm",
						"https://www.glassdoor.com/Overview/Working-at-Emory-Healthcare-EI_IE19564.11,27.htm",
						"https://www.glassdoor.com/Overview/Working-at-Barts-Health-NHS-Trust-EI_IE694160.11,33.htm",
						"https://www.glassdoor.com/Overview/Working-at-University-of-Maryland-School-of-Medicine-EI_IE507044.11,52.htm",
						"https://www.glassdoor.com/Overview/Working-at-Sentara-Healthcare-EI_IE4681.11,29.htm",
						"https://www.glassdoor.com/Overview/Working-at-Campbell-County-Memorial-Hospital-EI_IE121465.11,44.htm",
						"https://www.glassdoor.com/Overview/Working-at-Verity-Health-System-EI_IE1199906.11,31.htm",
						"https://www.glassdoor.com/Overview/Working-at-NHS-EI_IE12873.11,14.htm",
						"https://www.glassdoor.com/Overview/Working-at-Citizens-Memorial-Healthcare-EI_IE261939.11,39.htm",
						"https://www.glassdoor.com/Overview/Working-at-Lexington-Medical-Center-EI_IE19688.11,35.htm",
						"https://www.glassdoor.com/Overview/Working-at-Family-Service-EI_IE145040.11,25.htm",
						"https://www.glassdoor.com/Overview/Working-at-Metropolitan-Urological-Specialists-EI_IE1012379.11,46.htm",
						"https://www.glassdoor.com/Overview/Working-at-ABCD-Pediatrics-EI_IE1588325.11,26.htm",
						"https://www.glassdoor.com/Overview/Working-at-Greenway-Health-EI_IE17401.11,26.htm",
						"https://www.glassdoor.com/Overview/Working-at-Diamond-Institute-for-Infertil-EI_IE280481.11,41.htm",
						"https://www.glassdoor.com/Overview/Working-at-Prairie-Mountain-Health-EI_IE1093978.11,34.htm",
						"https://www.glassdoor.com/Overview/Working-at-FastHealth-EI_IE1351010.11,21.htm",
						"https://www.glassdoor.com/Overview/Working-at-Cleveland-Medical-EI_IE30168.11,28.htm",
						"https://www.glassdoor.com/Overview/Working-at-Centers-for-Medicare-and-Medicaid-Services-EI_IE13285.11,53.htm",
						"https://www.glassdoor.com/Overview/Working-at-The-University-of-Vermont-Medical-Center-EI_IE920836.11,51.htm",
						"https://www.glassdoor.com/Overview/Working-at-Associates-in-Plastic-Surgery-EI_IE1173658.11,40.htm",
						"https://www.glassdoor.com/Overview/Working-at-Kaleida-Health-EI_IE19488.11,25.htm",
						"https://www.glassdoor.com/Overview/Working-at-Surgical-Dermatology-and-Laser-Center-EI_IE1614647.11,48.htm",
						"https://www.glassdoor.com/Overview/Working-at-Pacific-Alliance-Medical-Center-EI_IE2037451.11,42.htm",
						"https://www.glassdoor.com/Overview/Working-at-Medical-Oncology-Hematology-Consultants-EI_IE1465366.11,50.htm",
						"https://www.glassdoor.com/Overview/Working-at-Hand-Rehabilitation-Specialists-EI_IE706598.11,42.htm",
						"https://www.glassdoor.com/Overview/Working-at-Community-Memorial-Health-System-EI_IE457569.11,43.htm",
						"https://www.glassdoor.com/Overview/Working-at-Children-s-Hospital-Colorado-EI_IE18618.11,39.htm",
						"https://www.glassdoor.com/Overview/Working-at-Augusta-Medical-Center-EI_IE121434.11,33.htm",
						"https://www.glassdoor.com/Overview/Working-at-Morehead-Memorial-Hospital-EI_IE27535.11,37.htm",
						"https://www.glassdoor.com/Overview/Working-at-RiverMend-Health-EI_IE795594.11,27.htm",
						"https://www.glassdoor.com/Overview/Working-at-Namaste-Home-Health-and-Hospice-EI_IE445072.11,42.htm",
						"https://www.glassdoor.com/Overview/Working-at-Chase-Brexton-Health-Care-EI_IE355869.11,36.htm",
						"https://www.glassdoor.com/Overview/Working-at-FirstHealth-of-the-Carolinas-EI_IE18976.11,39.htm",
						"https://www.glassdoor.com/Overview/Working-at-Catholic-Charities-USA-EI_IE23851.11,33.htm",
						"https://www.glassdoor.com/Overview/Working-at-Susquehanna-Health-EI_IE193360.11,29.htm",
						"https://www.glassdoor.com/Overview/Working-at-Baptist-Health-Kentucky-EI_IE17966.11,34.htm",
						"https://www.glassdoor.com/Overview/Working-at-CCRM-Management-Company-EI_IE618005.11,34.htm",
						"https://www.glassdoor.com/Overview/Working-at-Henry-Ford-Health-System-EI_IE4660.11,35.htm",
						"https://www.glassdoor.com/Overview/Working-at-Sinai-Health-System-EI_IE27975.11,30.htm",
						"https://www.glassdoor.com/Overview/Working-at-Midland-Memorial-Hospital-EI_IE121567.11,36.htm",
						"https://www.glassdoor.com/Overview/Working-at-MEDHOST-EI_IE355524.11,18.htm",
						"https://www.glassdoor.com/Reviews/colorado-mental-health-institute-reviews-SRCH_KE0,32.htm"]

		for url in result_urls:
			yield Request(url=url, callback=self.parse_result_page)


	def parse_result_page(self, response):

		rows = response.xpath('//*[@id="EmpBasicInfo"]/div[1]')

		for row in rows:
			title = row.xpath('./header/h2/text()').extract()

			size = row.xpath('./div/div[3]/span/text()').extract()

			company = row.xpath('./div/div[5]/span/text()').extract()

			industry = row.xpath('./div/div[6]/span/text()').extract()

			revenue = row.xpath('./div/div[7]/span/text()').extract() 


			item = GlassdoorItem()

			item['title'] = title
			item['size'] = size
			item['company'] = company
			item['industry'] = industry
			item['revenue'] = revenue

			yield(item)



