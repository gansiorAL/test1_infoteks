# Модуль Task1_InfoTeks получает с сайта list-org описание компании.
# Входные данные: ссылка на компанию (например https://www.list-org.com/company/4868135)
# Выходные данные: таблица , в каждой строке которой должны находиться:
# Полное юридическое наименование, Руководитель, Дата регистрации, Статус, ИНН,
# КПП, ОГРН,

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from tabulate import tabulate

def init_drive(brauser):
    """
    Инициализация драйвера
    :param brauser: Название браузеров GoogleChrome Firefox
    :return:
    """
    full_path=os.path.abspath('chromedriver78_0_3904')
    if brauser=="GoogleChrome":
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(full_path,chrome_options=options)
    if brauser == "Firefox":
        print("Firefox not here.")
    return driver

def analis_page(driver,page):
    """
    Модуль анализа страницы
    :param driver: Страница
    :return: словарь ключи - название полей в таблице и значение этих полей
    """
    driver.get(page)
    inform={}
    inform["Полное юридическое наименование "]=driver.find_element(By.XPATH,'//div/p/a[@class="upper"]').text
    inform["Руководитель "]=driver.find_element(By.XPATH,'//div//td/a[@class="upper"]').text
    inform["Дата регистрации "]=driver.find_element(By.XPATH,'//div/table//tr[6]/td[2]').text
    inform["Статус "]=driver.find_element(By.XPATH,'//div/table//tr[7]/td[2]').text
    inn=driver.find_element(By.XPATH,'//div/table//tr[2]').text.strip().split('/')
    inform["ИНН "]=inn[2]
    inform["КПП "] = inn[1].strip().split(' ')[1]
    inform["ОГРН "]=driver.find_element(By.XPATH,'//div/p[4]').text
    return inform

def print_table(all_info):
    """
    распечатка словаря в таблицу
    :param all_info:
    :return:
    """
    print(tabulate(all_info.items(), headers=['Название', 'Значение'], tablefmt="fancy_grid"))

def main_path(page):
    driver=init_drive("GoogleChrome")
    all_info=analis_page(driver,page)
    print_table(all_info)

if __name__=="__main__":
    main_path('https://www.list-org.com/company/4868135')