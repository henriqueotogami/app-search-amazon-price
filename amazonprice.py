import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_3?keywords=sony+a7&qid=1561393494&s=gateway&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)

    title = soup.find(id="title")
    print(title)
    price = soup.find(id="buyNew_noncbb")
    print(price)
    converted_price = float(price[0:5])

    if (converted_price < 1.700):
        send_mail()

    print(converted_price)
    print(title.strip())

    if (converted_price > 1.700):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #VEJA QUE NA LINHA ABAIXO FORAM REMOVIDAS AS INFORMAÇÕES DE E-MAIL E SENHA DE APLICATIVO
    #ISSO FOI FEITO PORQUE CADA PESSOA PRECISA INSERIR SUA PRÓPRIA SENHA
    #E REMOVI ESSAS MINHAS INFORMAÇÕES POR QUESTÃO DE SEGURANÇA
    server.login('YOUR FIRST EMAIL HERE','GOOGLE APP PASSWORD HERE')
    subject = 'Price feel down'
    body = 'Check the amazon link ' + URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('YOUR FIRST EMAIL HERE', 'YOUR SECOND EMAIL HERE', msg)

    print('Hey email has been sent')

    server.quit()


while(True):
    check_price()
    time.sleep(60*60)