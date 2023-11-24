# Automaçao Web com Selenium
# Instale as duas bibliotecas com o pipinstall
# +selenium
# +webdriver-manager
#no ambiente virtual proprio
#link em que vamos automatizar o processo
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqblNFNlpFMzFLTVNDS3E3NTI3ZkxRZ052eV92Z3xBQ3Jtc0trOUc5WjAtREd5QllCYkNLbVF3eXJiamEteEVHQjIxRHNPVFB6M1ZxUTA5aXBXUzMtQ1hvcTdZbjZULUpzcTVpREhFeDlYOG1XeGZkVzNfQTNTQjRETTh4VnpNWEJqenQ3SDJaZVZoZlRhaGNkdnpPVQ&q=https%3A%2F%2Fpages.hashtagtreinamentos.com%2Fesperapythonimpressionador%3Forigemurl%3Dhashtag_yt_org_listaesperapython_8AMNaVt0z_M&v=8AMNaVt0z_M

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

#maneira de pegar qual a página vai ser automatizada
navegador.get('https://pages.hashtagtreinamentos.com/esperapythonimpressionador?origemurl=hashtag_yt_org_listaesperapython_8AMNaVt0z_M')
navegador.find_element('xpath',
                       '//*[@id="klickart-link18jo1igt2sv000"]').click()
navegador.find_element('xpath',
                       '/html/body/div[4]/div/div/div/div/div/div[3]/form/div[1]/div/div[1]/div/input').click()
navegador.find_element('xpath',
                       '/html/body/div[4]/div/div/div/div/div/div[3]/form/div[1]/div/div[1]/div/input').send_keys('alace')
#navegador.find_element('xpath',
#                       '/html/body/div[4]/div/div/div/div/div/div[3]/form/div[1]/div/div[2]/div/input').click()
navegador.find_element('xpath',
                       '/html/body/div[4]/div/div/div/div/div/div[3]/form/div[1]/div/div[2]/div/input').send_keys('alac@blindo.com.br')

espera = input("Pressione Enter:")