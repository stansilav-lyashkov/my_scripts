import requests
from bs4 import BeautifulSoup

def zp_take(money):
    list_zp = []
    for mones in money:
        prs = mones.get_text()
        list_zp.append(str(prs))

    return list_zp


def parser(url): #https://tambov.hh.ru/search/vacancy?clusters=true&enable_snippets=true&text=python&L_save_area=true&area=1&from=clusr_area&showClusters=false
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "accept": "*/*"}
    global DATA,list
    DATA = []
    list = []

    session = requests.session()
    r = session.get(url,headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content,"html.parser")
        divs = soup.find_all("div", attrs={"data-qa":"vacancy-serp__vacancy",})



        for div in divs:

            title = div.find("a", attrs={"data-qa":"vacancy-serp__vacancy-title"}).text
            href = div.find("a", attrs={"data-qa":"vacancy-serp__vacancy-title"})["href"]
            #print("Вакансия -",title," ссылка - ",href)
            #try:
            money = soup.select("div.vacancy-serp-item__sidebar")
            list = zp_take(money)
            elem = list[divs.index(div)]
            DATA.append(

                {"vacancy": title,
                 "salary":elem ,
                 "url": href}
            )

            #except AttributeError:
            #money = "Зп не указана"
            for i in DATA:
                print("Вакансия: " + i["vacancy"] + "  Ссылка: " + i[
                    "url"] + "\n" + "\n")
parser("https://tambov.hh.ru/search/vacancy?clusters=true&enable_snippets=true&text=python&L_save_area=true&area=1&from=clusr_area&showClusters=false")