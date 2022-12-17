#################################
#Задача:
#Необходимо написать программу, которая будет считывать файл с ссылками в каждой строке. далее программа должна получить по каждой ссылки чистый текст стихотворения. Каждый стих должен быть в отдельном файле, причем первой строкой должно идти наименование стихотворения, второй строкой автор, третья строка  - это пустая строка,  четвертая строка - начинается стихотворение. Название выходных файлов должно идти так: stih_00001.txt, stih_00002.txt, stih_00003.txt и т.д.
#Пример входного файла: input.txt
#Пример выходного файла: stih_00001.txt
import requests
from bs4 import BeautifulSoup
import re


def get(filename, l):
    i = open(filename, "r", encoding="utf-8")
    urls = i.read().split("\n")

    for u in urls:
        l+=1
        o = open(f"stih_00{l}.txt", "w")
        src=requests.get(u).text
        soup=BeautifulSoup(src)
        poema = soup.find("section",class_="content").find_all("p")
        aftor = soup.find("section",class_="content").find(class_="tema-stih")
        name = soup.find("section",class_="content").find("h1")
        o.write("\t"+"\t"+"\t"+name.text)
        o.write(aftor.text)
        o.write("\n")
        for p in poema:
            o.write(p.text+"\n")


def getstih(url, indf):
    resp = requests.get(url)
    alltext = resp.text


    url = "https://stihibase.ru/author/f/fet/mama_gljan_ka_iz_okoshka/"

    response = requests.get(url)

    # Шаг1 получает состояние  .status_code
    print(response.status_code)

    # Шаг2 получает содержимое
    restext = response.text
    # print(restext)

    # Шаг3 сохраняем в файл
    f = open('output.txt', 'w', encoding='utf-8')
    f.write(restext)
    f.close()

    # Шаг5 Регулярка
    match = re.findall(r'<article[\S\s]*article>', restext)
    print(match[0])
    restext = match[0]
    match = re.findall(r'<p.*?>.*</p>', match[0])
    print(match)

    # Очищаем и выводим в конечный файл
    resstih = ""
    for m in match:
        c = m.replace("<p>", "")
        d = c.replace("</p>", "")
        e = d.replace('<p class="strofa">', "")
        resstih = resstih + e + "\n"
        print(e)

    f = open('stih000'+str(indf)+'.txt', 'w', encoding='utf-8')
    f.write(resstih)
    f.close()



def getre(filename, indf):
    f = open(filename)
    mas = f.read().split("\n")
    for url in mas:
        print(" ")
        if url != "":
            indf += 1
            getstih(url, indf)
    f.close()
