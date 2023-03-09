from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class ManagerWebphone:

    def __init__(self):
        # Permitir uso de micro
        opt = Options()
        opt.add_argument('--disable-blink-features=AutomationControlled')
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 0,
            "profile.default_content_setting_values.notifications": 1
        })

        self.drive = webdriver.Chrome(options=opt)
        self.drive.get('https://fonebeta.55pbx.com/')

    def login(self, email: str, password: str, name_client: str):
        div_root = self.drive.find_element(By.XPATH, '/html/body/div')

        # necessário para renderização do elemento
        form_login = WebDriverWait(div_root, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div/div[2]/div[1]/form'))
        )

        [email_input, password_input] = form_login.find_elements(By.TAG_NAME, 'input')

        email_input.send_keys(email)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        div_clients = WebDriverWait(div_root, 50).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div/div[2]/div[1]/div/div[1]/div/div[2]/*'))
        )

        for client in div_clients:
            if client.text.upper() == name_client.upper():
                client.click()
                break

        try:
            modal_error = WebDriverWait(self.drive, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/footer/button"))
            )
            modal_error.click()
        except:
            pass

    def diskPhone(self, number: str):
        print('DISCANDO PARA O NÚMERO:', number)
        self.drive.implicitly_wait(500)
        input_number = WebDriverWait(self.drive, 5).until(
            EC.presence_of_element_located  ((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[3]/input'))
        )

        input_number.send_keys(number)
        input_number.send_keys(Keys.RETURN)

    def getTitle(self) -> str:
        return self.drive.title

    def close(self):
        self.drive.close()
