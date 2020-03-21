import requests
from bs4 import BeautifulSoup
import vk_api
from vk_api.longpoll import VkLongPoll,VkEventType
import random


def create_what(what):
    #what = ""
    #BASE_URL = "https://tambov.hh.ru/search/vacancy?clusters=true&enable_snippets=true&text="+what+"&L_save_area=true&area=1&from=clusr_area&showClusters=false"
    global BASE_URL
    BASE_URL = "https://tambov.hh.ru/search/vacancy?clusters=true&enable_snippets=true&text="+what+"&L_save_area=true&area=1&from=clusr_area&showClusters=false"
    return BASE_URL


headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
           "accept":"*/*"}


#Функция для получения списка ЗП
def zp_take(money):
    list_zp = []
    for mones in money:
        prs = mones.get_text()
        list_zp.append(str(prs))

    return list_zp


def parser(url,headers):
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




    else:
        print("Error")



token = "076db0065472159cd53a7ce2e9f8ec974eb205dbf3e3b96644c1fbf7383b55c4708281f255c89b94f3ed9"

    # Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

    # Работа с сообщениями
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send',

              {'user_id': user_id,  # TODO Сделать рефакторинг, чтобы было легче работать с собщениями
               # TODO сделать более грамотное распределение обязанностей
               'message': message,
               "random_id": random.randint(1, 1000000)

               })


for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            request = event.text


            if request == "Начать":
                write_msg(event.user_id, "Добрый день,я помогу вам найти любые вакансии на портале HH.ru")

            if request[0] != "!":
                write_msg(event.user_id,"Для того чтобы начать поиск просто напиши любимую профессию, но перед ней "
                                        "поставь вопросительный знак[!], чтобы я понял) "
                                        "Пример: !учитель")

            if request[0] == "!":


                parser(create_what(request), headers)


                message_list = []

                for i in DATA:
                    message_list.append("Вакансия: " + i["vacancy"]  + "  Ссылка: " + i[
                        "url"] + "\n" + "\n")
                for p in message_list:
                    vk.method('messages.send',

                              {'user_id': event.user_id,  # TODO Сделать рефакторинг, чтобы было легче работать с собщениями
                               # TODO сделать более грамотное распределение обязанностей
                               'message': p,
                               "random_id": random.randint(1, 1000000)

                               })
