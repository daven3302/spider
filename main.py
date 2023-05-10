import requests as rq
from bs4 import BeautifulSoup as bs


def href_to_url(s: str):
    s = "https:" + s
    return s


website_former = "https://www.104.com.tw/company/search/?jobsource=checkc&utm_source=104main&utm_medium=search_area&emp=3&page="
website_last = "&sw=2&=1012000000,1005000000,1006000000"
website_result = "info-job.text-break.mb-2"
page_num = 100

file = open("result.csv", "w")
for i in range(page_num):
    website_104 = website_former + str(i+1) + website_last
    website_rq = rq.get(website_104)
    website_soup = bs(website_rq.text, 'html.parser')
    website_sel = website_soup.select("div."+website_result + " a")
    for j in website_sel:
        if (j.text[0] == ' '):
            continue
        file.write(j.text)
        file.write(",")
        file.write(href_to_url(j["href"]))
        file.write("\n")

        # company = href_to_url(j["href"])
        # company_rq = rq.get(company)
        # company_rq = rq.get(
        # "https://www.104.com.tw/company/1a2x6bjdks?jobsource=checkc")
        # company_soup = bs(company_rq.text, 'html.parser')
        # company_website = company_soup.select(
        # "div.col.pl-1.p-0.intro-table__data a")
        # for k in company_website:
        # print(k['data-gtm-content'], k["href"])
        # company_employee_num = company_soup.select(
        # "p.t3.mb-0")
        # for k in company_employee_num:
        # print(k.text)
        # print(company_employee_num[6].text)
        # break
    # break


file.close()
