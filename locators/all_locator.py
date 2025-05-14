from selenium.webdriver.common.by import By


class HomePageLocators:
    login_account_button = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button') # кнопка "Войти в аккаунт"
    personal_account_button = (By.XPATH, "//p[text()='Личный Кабинет']")  # кнопка "Личный кабинет"
    make_an_order_button = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button') # кнопка Оформления заказа
    constructor_button = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a') # Кнопка Конструктор
    stellar_burgers_label = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a') # Логотип Stellar Bergers
    scroll_to_buns = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]') # Переход к разделу выбора булок
    scroll_to_sauces = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]') # Переход к разделу выбора соусов
    scroll_to_fillings = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]') # Переход к разделу выбора начинки
    create_burger_label = (By.XPATH, '//*[@id="root"]/div/main/section[1]/h1') # надпись Соберите бургер

class LoginPageLocators:
    email_input = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input') # поле ввода Email
    password_input = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input') # поле ввода Пароль
    login_button = (By.XPATH, '//*[@id="root"]/div/main/div/form/button') # кнопка Войти
    restore_password_link = (By.XPATH, "//a[@href='/forgot-password']") # кнопка Восстановить пароль
    registration_link = (By.XPATH, "//a[@href='/register']") # Кнопка для перехода на страницу регистрации
    login_label = (By.XPATH, '//*[@id="root"]/div/main/div/h2') # надпись Вход
    stellar_burgers_label = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a') # Логотип Stellar Bergers

class RegistrationPageLocators:
    name_reg_input = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')  # поле ввода Имя
    email_reg_input = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input') # поле ввода Логин
    password_reg_input = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input') # поле ввода Пароль
    registration_link = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a') # кнопка перехода на страницу регистрации
    error_message = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')  # текст ошибки
    login_label = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a') # надпись Вход
    registration_button = (By.XPATH, '//*[@id="root"]/div/main/div/form/button') # кнопка Зарегистрироваться

class PersonalAccountLocators:
    logout_button = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button') # кнопка выхода из аккаунта
    history_order_button = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[2]/a') # кнопка просмотра истории заказов
