from selenium.webdriver.common.by import By


class Total_price:
    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self):
    #Открыть страницу 'https://www.saucedemo.com/'
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.saucedemo.com/')

    def autorization(self):
    #Авторизоваться под пользователем standard_user
        self.driver.find_element(By.CSS_SELECTOR,'#user-name').send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR,'#password').send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR,'#login-button').click()

    def add_goods(self):
    #Добавить в корзину товары:
        self.driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-onesie').click()

    def go_to_cart(self):
    #Перейти в корзину
        self.driver.find_element(By.CSS_SELECTOR,'#shopping_cart_container > a').click()

    def push_checkout(self):
    #Нажать Checkout
        self.driver.find_element(By.CSS_SELECTOR,'#checkout').click()

    def fill_form(self):
    #Заполнить форму своими данными:
     self.driver.find_element(By.CSS_SELECTOR,'#first-name').send_keys("Pavel")
     self.driver.find_element(By.CSS_SELECTOR,'#last-name').send_keys("Brovkin")
     self.driver.find_element(By.CSS_SELECTOR,'#postal-code').send_keys("140203")
     self.driver.find_element(By.CSS_SELECTOR,'#continue').click()

    def get_total_price(self):
    #Прочитать со страницы итоговую стоимость ( Total )
        return self.driver.find_element(By.CSS_SELECTOR,'#checkout_summary_container > div > div.summary_info > div.summary_total_label').text

    def quit(self):
    #Закрыть браузер
        self.driver.quit


