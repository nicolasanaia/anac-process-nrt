from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
# import os
# import wget
# import time

browser = webdriver.Chrome()
browser.get('https://www.facebook.com/campaign/landing.php?campaign_id=1654787885&extra_1=s%7Cc%7C355276400790%7Ce%7Ccreate%20account%20facebook%7C&placement=&creative=355276400790&keyword=create%20account%20facebook&partner_id=googlesem&extra_2=campaignid%3D1654787885%26adgroupid%3D62478116814%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-307638033092%26loc_physical_ms%3D1001773%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=Cj0KCQiAuP-OBhDqARIsAD4XHpdygiNCGuC5KNgA7_pjO3lN0hUpNH2lovwk40zABlHgVsFCrGe8_yEaAgR4EALw_wcB')
# browser.get('https://sso.anac.gov.br/auth/realms/producao/protocol/openid-connect/auth?client_id=client-saci&redirect_uri=https%3A%2F%2Fsistemas%2Eanac%2Egov%2Ebr/SCA/Keycloak.asp&response_type=token&scope=openid&nonce=0n8vpnmmml')

insert_name = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='firstname']")))
insert_time = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='lastname']")))

insert_name.clear()
insert_name.send_keys("my_username")
insert_time.clear()
insert_time.send_keys("my_password")

send = WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

df = pd.read_csv("nrtStructure.csv")
# ,encoding='utf-8',usecols=['Curso','Dia Início','Dia Fim','Horário Início','Horário Fim','Local'])

print(len(df[(df['Curso'] == 'ARP')]))

counter = len(df)
for treinamento in df:
    counter -= 1
    print(counter)
    create_account.click()
    insert_name.send_keys(df[(df['Curso'][treinamento])])
    insert_time.send_keys(df[(df['Dia Início'][treinamento])])
    send.click()


# setLogin = browser.find_element_by_xpath('//*[@id="id_username"]')
# setLogin.send_keys('')

# setPassword = browser.find_element_by_xpath('//*[@id="id_password"]')
# setPassword.send_keys('')

# loginButton = browser.find_element_by_xpath('//*[@id="kc-form-wrapper"]/ui-view/ux-keycloak-login/section/ux-card-group/div/ux-card/a/md-card/md-card-content/div/div[1]/ux-form/form/div[2]/actions/div/ux-button/ux-tooltip/ng-transclude/button/div[1]')
# loginButton.click()