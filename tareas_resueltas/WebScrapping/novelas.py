from lxml.html import parse
from lxml.etree import tostring
from lxml import etree as et

import urllib.request
from novela import Novel
from sqlite import SqliteStorage

URL_BASE = "https://www.readwn.com/"
CORTE_NOVELAS = 100
CORTE_CAPITULOS = 10 

def inspect_chapter(chapter_url):
    response = urllib.request.urlopen(chapter_url)
    chapter_page = parse(response)
    chapter_text = " ".join(chapter_page.xpath("//div[@class = 'chapter-content']")[0].itertext()).strip()
    return chapter_text

def inspect_novel(novel_url):
    response = urllib.request.urlopen(novel_url)
    novel_page = parse(response)
    novel_title = novel_page.xpath("//h1[@class = 'novel-title text2row']")[0].text
    novel_author = novel_page.xpath("//span[@itemprop = 'author']")[0].text

    novel_categories = []
    for novel_category_item in novel_page.xpath("//div[@class = 'categories']/ul")[0]:
        novel_categories.append(novel_category_item.find("a").text)

    novel_summary = " ".join(novel_page.xpath("//div[@class = 'summary']/div")[0].itertext()).strip()

    novel_text = ""
    chapter_items = novel_page.xpath("//ul[@class = 'chapter-list']/*")
    chapter_counter = 0
    for chapter_item in chapter_items:
        if chapter_counter == CORTE_CAPITULOS: break
        novel_text += " " + inspect_chapter(URL_BASE + chapter_item.find("a").get("href"))
        chapter_counter += 1
    
    return Novel(novel_url, novel_title, novel_author, " ".join(novel_categories), novel_summary, novel_text)

def inspect_site(site_url):
    #cambio de user agent
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    #descarga y parseo de la pagina.
    response = urllib.request.urlopen(site_url)
    doc = parse(response)

    novel_counter = 0
    novels = []
    novel_items = doc.xpath("//li[@class = 'novel-item']/a/@href")

    with SqliteStorage(r"novelas.db") as sqliteStorage:
        for novel_item in novel_items:
            if novel_counter == CORTE_NOVELAS: break
            sqliteStorage.add_novel(inspect_novel(URL_BASE + novel_item))
            novel_counter += 1


def main():
    inspect_site("https://www.readwn.com/list/all/all-onclick-0.html")

main()