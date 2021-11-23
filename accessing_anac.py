from selenium import webdriver
import csv

browser = webdriver.Chrome()

browser.get('https://sso.anac.gov.br/auth/realms/producao/protocol/openid-connect/auth?client_id=client-saci&redirect_uri=https%3A%2F%2Fsistemas%2Eanac%2Egov%2Ebr/SCA/Keycloak.asp&response_type=token&scope=openid&nonce=0n8vpnmmml')

setLogin = browser.find_element_by_xpath('//*[@id="id_username"]')
setLogin.send_keys('')

setPassword = browser.find_element_by_xpath('//*[@id="id_password"]')
setPassword.send_keys('')

loginButton = browser.find_element_by_xpath('//*[@id="kc-form-wrapper"]/ui-view/ux-keycloak-login/section/ux-card-group/div/ux-card/a/md-card/md-card-content/div/div[1]/ux-form/form/div[2]/actions/div/ux-button/ux-tooltip/ng-transclude/button/div[1]')
loginButton.click()