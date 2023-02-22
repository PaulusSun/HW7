from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self):
    #Открыть страницу https://bonigarcia.dev/selenium-webdriver-java/data-types.html
        self.driver.implicitly_wait(10)
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
   

    def fill_form(self):
    #Заполнить форму значениями 
        self.driver.find_element(By.CSS_SELECTOR,'[name="first-name"]').send_keys('Иван')
        self.driver.find_element(By.CSS_SELECTOR,'[name="last-name"]').send_keys('Петров')
        self.driver.find_element(By.CSS_SELECTOR,'[name="address"]').send_keys('Ленина, 55-3')
        self.driver.find_element(By.CSS_SELECTOR,'[name="city"]').send_keys('Москва')
        self.driver.find_element(By.CSS_SELECTOR,'[name="country"]').send_keys('Россия')
        self.driver.find_element(By.CSS_SELECTOR,'[name="job-position"]').send_keys('QA')
        self.driver.find_element(By.CSS_SELECTOR,'[name="company"]').send_keys('SkyPro')

    def click_the_button(self):
    #Нажать кнопку Submit
        self.driver.find_element(By.CSS_SELECTOR, '[class*="btn-outline-primary"]').click()

    def get_background_color_from_zip_code(self):
    #Получить цвет Zip code:
        return self.driver.find_element(By.CSS_SELECTOR,'#zip-code').value_of_css_property("background-color")

    def get_background_color_from_first_name(self):
    #Получить цвет first_name:
        return self.driver.find_element(By.CSS_SELECTOR,'#first-name').value_of_css_property("background-color")

    def get_background_color_from_last_name(self):
    #Получить цвет last_name:
        return self.driver.find_element(By.CSS_SELECTOR,'#last-name').value_of_css_property("background-color")

    def get_background_color_from_address(self):
    #Получить цвет last_address:
        return self.driver.find_element(By.CSS_SELECTOR,'#address').value_of_css_property("background-color")

    def get_background_color_from_city(self):
    #Получить цвет last_city:
        return self.driver.find_element(By.CSS_SELECTOR,'#city').value_of_css_property("background-color")

    def get_background_color_from_country(self):
    #Получить цвет country:
        return self.driver.find_element(By.CSS_SELECTOR,'#country').value_of_css_property("background-color")

    def get_background_color_from_job_position(self):
    #Получить цвет job_position:
        return self.driver.find_element(By.CSS_SELECTOR,'#job-position').value_of_css_property("background-color")

    def get_background_color_from_company(self):
    #Получить цвет company:
        return self.driver.find_element(By.CSS_SELECTOR,'#company').value_of_css_property("background-color")

    def quit(self):
    #Закрыть браузер
        self.driver.quit





