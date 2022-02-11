from selenium import webdriver
import time

contato = input("para quem gostaria de enviar? ")
mensagem = input("sua mensagem: ")

class WhatsappBoth:
    def __init__(self):
        self.mensagem = mensagem
        self.pessoas = [contato]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagem(self):

        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)

        for pessoa in self.pessoas:
            pessoa = self.driver.find_element_by_xpath(f"//span[@title='{pessoa}']")
            time.sleep(3)
            pessoa.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBoth()
bot.EnviarMensagem()
