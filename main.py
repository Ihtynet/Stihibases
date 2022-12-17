import requests
from bs4 import BeautifulSoup

def get_links(adr):
    resp_a = requests.get(adr)
    alltext_a = resp_a.text
    soup = BeautifulSoup(alltext_a, "html.parser")
    res = soup.find_all("a")
    return res

##################################
nomfile = 1
f = open("output"+str(nomfile)+".txt", "w")

mas_links_a_a = get_links("https://stihibase.ru/author/")
kol_a = 0
kol_s = 0

mas_links_a = []
for links_a1 in mas_links_a_a:
    links_a = links_a1.get("href")
    if "/author/" in links_a and links_a.count("/") == 4 and links_a not in mas_links_a:
        kol_a += 1
        mas_links_a.append(links_a)
        print(kol_a, links_a)

        mas_links_s_a = get_links("https://stihibase.ru" + links_a)


        for links_s1 in mas_links_s_a:
            links_s = links_s1.get("href")
            if links_s.count("/") == 5:
                kol_s += 1
                if kol_s % 500 == 0:
                    nomfile += 1;
                    f.close()
                    f = open("output"+str(nomfile)+".txt", "w")
                print(kol_s, links_s)

                f.write(links_s + "\n")
f.close()
f = open("output.txt", "r")
mas = f.readlines()
print(len(mas))
#???????????