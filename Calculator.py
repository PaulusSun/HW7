from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout

    def open_main_page(self):
    #Открыть страницу 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
        self.driver.implicitly_wait(10)
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    def clear_locator_delay(self):
    #Очистить поле ввода по локатору #delay
        self.driver.find_element(By.CSS_SELECTOR,'#delay').clear()

    def add_time_for_locator_delay(self):
    #В поле ввода по локатору #delay ввести значение timeout
        self.driver.find_element(By.CSS_SELECTOR,'#delay').send_keys(self.timeout)

    def push_7(self):
    #Нажать кнопку 7
        self.driver.find_element(By.XPATH,"//span [contains(text(),'7')]").click()

    def push_plus(self):
    #Нажать кнопку +
        self.driver.find_element(By.XPATH,"//span [contains(text(),'+')]").click()

    def push_8(self):
    #Нажать кнопку 8
        self.driver.find_element(By.XPATH,"//span [contains(text(),'8')]").click()

    def push_equals(self):
    #Нажать кнопку =
        self.driver.find_element(By.XPATH,"//span [contains(text(),'=')]").click()

    def wait_for_result(self):
    #Ожидать появления результата
        WebDriverWait(self.driver, self.timeout+5).until(EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR,'.screen') , 'innerHTML', '15'))
       
    def quit(self):
    #Закрыть браузер
        self.driver.quit

    def get_result(self):
    #Получить результат вычисления
        return self.driver.find_element(By.CSS_SELECTOR,'.screen').get_attribute('innerHTML')

    