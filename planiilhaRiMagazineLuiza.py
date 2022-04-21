#importando bibliotecas
from selenium import webdriver

navegador = webdriver.Chrome()

#Acessar site https://ri.magazineluiza.com.br/show.aspx?idCanal=CHN0/Z4bUSgrS8IkQeL+Wg==
navegador.get('https://ri.magazineluiza.com.br/show.aspx?idCanal=CHN0/Z4bUSgrS8IkQeL+Wg==')
#Fazer download Planilha de Resultados Trimestrais
navegador.find_element_by_xpath('//*[@id="njHO0wkFb2425KPP/mEasg=="]').click()

