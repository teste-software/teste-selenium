from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class ManagerRealtime:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://realtimebeta.55pbx.com:8600/#/')

    def register(self, email: str, password: str, name_client: str):
        sleep(2)
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'form_email'))
        )
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'form_password'))
        )
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        selected_search_client = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/main/div/form/div[1]/div/div/div[1]/span/span[1]'))
        )
        selected_search_client.click()

        search_client = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/main/div/form/div[1]/div/div/input[1]'))
        )
        search_client.send_keys(name_client)
        search_client.send_keys(Keys.RETURN)

        button_enter = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/main/div/form/div[2]/div/button'))
        )
        button_enter.click()

    def get_status_ramal(self, name: str) -> str:
        sleep(20)
        print('GET STATUS REALTIME: ', name)
        list_ramais = self.driver.find_element(By.XPATH, '/html/body/div[1]/ion-side-menus/ion-side-menu-content/ion-nav-view/ion-view/ion-content/div[1]/div/div[4]/div/div[2]/table/tbody')
        tr_ramais = list_ramais.find_elements(By.TAG_NAME, 'tr')

        self.driver.implicitly_wait(1000)
        status_text = 'não encontrado o ramal'
        for ramal in tr_ramais:
            name_td = ramal.find_elements(By.TAG_NAME, 'td')
            if name_td[1].text == name.upper():
                status = name_td[0].find_element(By.XPATH, '//p/span')
                status_text = status.text

        return status_text

    def close(self):
        self.driver.close()