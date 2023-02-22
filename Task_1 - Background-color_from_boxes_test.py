from selenium import webdriver
from MainPage import MainPage

def test_color_boxes():
    red_background_color = 'rgba(248, 215, 218, 1)'
    green_background_color = 'rgba(209, 231, 221, 1)'
    
    mainPage = MainPage(webdriver.Chrome())
    mainPage.open_main_page()
    mainPage.fill_form()
    mainPage.click_the_button()
    mainPage.quit
#Проверить (assert), что поле Zip code подсвечено красным:
    assert mainPage.get_background_color_from_zip_code() == red_background_color
#Проверить (assert), что остальные поля подсвечены зеленым:
    assert mainPage.get_background_color_from_first_name() == green_background_color
    assert mainPage.get_background_color_from_last_name() == green_background_color
    assert mainPage.get_background_color_from_address() == green_background_color
    assert mainPage.get_background_color_from_city() == green_background_color
    assert mainPage.get_background_color_from_country() == green_background_color
    assert mainPage.get_background_color_from_job_position() == green_background_color
    assert mainPage.get_background_color_from_company() == green_background_color

