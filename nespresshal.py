from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import requests as rq, json, time
from bs4 import BeautifulSoup as bs

my_login = input("Entrez votre login HAL : ")
my_pass = input("Entrez votre mot de passe HAL : ")
my_struct = input("Entrez le numéro de votre structure : ")
portail = input("Entrez l'url de votre portail HAL : ")
review = input("Entrez le nom de la revue dont vous souhaitez ajouter le texte sur HAL : ")


def identify(login, password):
    driver.get('https://cas.ccsd.cnrs.fr/cas/login?service=https%3A%2F%2Fhal.science%2Fuser%2Flogin%3Furl%3Dhttps%253A%252F%252Fhal.science%252F')
    time.sleep(3)
    login = driver.find_element(By.NAME, "username")
    login.send_keys(my_login)
    password = driver.find_element(By.NAME, "password")
    password.send_keys(my_pass)
    driver.find_element(By.NAME, "submit").click()

# url = f"https://api.archives-ouvertes.fr/search/?q&wt=json&rows=250&fq=structId_i:{struct}}&fq=(submitType_s:notice%20AND%20openAccess_bool:(true))&fl=halId_s"
# url = f"https://api.archives-ouvertes.fr/search/?q&wt=json&rows=250&fq=structId_i:{my_struct}&fq=(submitType_s:notice%20AND%20journalPublisher_s:%22MDPI%22)&fl=halId_s"
url = f"https://api.archives-ouvertes.fr/search/?&wt=json&rows=200&fq=structId_i:{my_struct}&fq=(submitType_s:notice%20AND%20openAccess_bool:(true)%20AND%20journalPublisher_s:%22{review}%22)&fl=halId_s"
req = rq.get(url)
req = req.json()
liste_id = []
for i in range(len(req['response']['docs'])):
    liste_id.append(req['response']['docs'][i]['halId_s'])
print("Bienvenue sur NespressHal ! Votre login et votre mot de passe vont vous être demandés")
print(" mais aucune information ne sera collectée ou conservée, pas d'inquiétude! ")
print("Script créé par J. Caugant, Cellule Science Ouverte du SCD d'Aix-Marseille Université, sous licence GNU-GPL")


for id in liste_id:
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(options=options)
    identify(my_login, my_pass)
    time.sleep(5)
    url = portail+"/"+id
    req = rq.get(url)
    time.sleep(2)
    result = req.content
    soup = bs(result,'html.parser')
    lien_text = soup.find('div', attrs={'class': 'section-content section-shadow hal-visualize-button widget-files'}).find("a").get("href")
    req = rq.get(lien_text)
    get_url = req.url
    # driver.get(lien_text)
    time.sleep(5)
    # get_url = driver.current_url
    time.sleep(5)
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "hal-login-button").click()
    time.sleep(4)
    try :
        driver.find_element(By.CLASS_NAME, "icon-add_file").click()
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "btn-link").click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "form-control").send_keys(get_url)
        # driver.find_element(By.CLASS_NAME, "form-control").send_keys(lien_text)
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "btn-confirm").click()
        time.sleep(10)
        driver.find_element(By.NAME, "accept_licence").click()
        time.sleep(5)
        driver.find_element(By.ID, "submission-btn").click()
        time.sleep(15)
        driver.close()
    except :
        time.sleep(5)
        driver.close()





