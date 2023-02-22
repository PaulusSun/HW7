from selenium import webdriver
from Calculator import Calculator


def test_result_calculator():
    calculator = Calculator(webdriver.Chrome(), 45)
    calculator.open_main_page()
    calculator.clear_locator_delay()
    calculator.add_time_for_locator_delay()
    calculator.push_7()
    calculator.push_plus()
    calculator.push_8()
    calculator.push_equals()
    calculator.wait_for_result()
    calculator.quit()

    assert calculator.get_result() == '15'