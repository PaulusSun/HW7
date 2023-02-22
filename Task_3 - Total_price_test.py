from selenium import webdriver
from Total_price import Total_price

def test_total_price():
    total_price = Total_price(webdriver.Chrome())
    
    total_price.open_main_page()
    total_price.autorization()
    total_price.add_goods()
    total_price.go_to_cart()
    total_price.push_checkout()
    total_price.fill_form()
    total_price.quit()
    
    assert total_price.get_total_price() == 'Total: $58.29'
