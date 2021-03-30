import os
import requests
from lxml import html

desktop_path = f"{os.environ['USERPROFILE']}\\Desktop"
tel_numbers = []
websites = []
stages = []
categories = []

# xanutneri urlner@ vercnuma naxoroq tvac hxumnerov filic u qcuma listi mej
page_urls = []
with open(f"{desktop_path}\\requests_after.txt", "r") as file:
    for url in file.readlines():
        page_urls.append(url)

# copy arac u xar@ dasavorvac hxumneric darcnuma normal hxumnerov file irar tak dasavorvac
"""
text_array_after = []

with open(f"{desktop_path}\\requests_before.txt", "r") as file:
    text_array_before = file.readlines()
    for index in range(1, len(text_array_before)):
        text_array_after.append(text_array_before[index].split()[1])

with open(f"{desktop_path}\\requests_after.txt", "w+") as file:
    for text_part in text_array_after:
        file.write(f"{text_part}\n")
"""

# hxumneri vrayov hertov ancnuma u amen mi hxumov bacvac ejic vercnuma
# heraxosi hamar@, kayqi hascen, categorian

for url_index in range(len(page_urls)):
    page = requests.get(page_urls[url_index])
    tree = html.fromstring(page.content)
    print(f"{url_index} --- {page_urls[url_index]}")

    tel_number_ls = tree.xpath('//div[@class="info-block"]/div[@class="site"]/p/text()')
    website_ls = tree.xpath('//div[@class="info-block"]/div[@class="site"]/a/text()')
    stage_ls = tree.xpath('//div[@class="info-block"]/div[@class="map"]/p/text()')
    categories_ls = tree.xpath('//div[@class="info-block"]/div[@class="tag"]/'
                           'div[@class="table"]/div[@class="table-cell"]/div[@class="items"]/a/span/text()')

    if len(tel_number_ls) != 0: tel_numbers.append(tree.xpath('//div[@class="info-block"]/div[@class="site"]/p/text()')[0].strip())
    else: tel_numbers.append("-")
    if len(website_ls) >= 2: websites.append(tree.xpath('//div[@class="info-block"]/div[@class="site"]/a/text()')[1].strip())
    else: websites.append("-")

    stage = tree.xpath('//div[@class="info-block"]/div[@class="map"]/p/text()')[0].strip()
    categorie = tree.xpath('//div[@class="info-block"]/div[@class="tag"]/'
                           'div[@class="table"]/div[@class="table-cell"]/div[@class="items"]/a/span/text()')[0].strip()
    stages.append(stage)
    categories.append(categorie)

with open(f"{desktop_path}\\data.txt", "a+", encoding="utf-8") as database:
    for index in range(len(tel_numbers)):
        database.write(f"{tel_numbers[index]}&&&{websites[index]}&&&{stages[index]}&&&{categories[index]}\n")