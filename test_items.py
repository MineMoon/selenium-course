import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    
    # Раскомментируйте строку ниже, если проверяющему нужно визуально оценить язык кнопки (по условию задания):
    # time.sleep(30)

    # Ищем кнопку добавления в корзину по уникальному классу
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")

    # Проверяем, что кнопка найдена на странице (список не пустой)
    assert len(add_to_basket_button) > 0, "Button 'Add to basket' is not found on the page!"
