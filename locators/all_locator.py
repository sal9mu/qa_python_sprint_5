from selenium.webdriver.common.by import By


class HomePageLocators:
    login_account_button = (By.XPATH, "//button[text() = 'Войти в аккаунт']") # кнопка "Войти в аккаунт"
    personal_account_button = (By.XPATH, "//p[text()='Личный Кабинет']")  # кнопка "Личный кабинет"
    make_an_order_button = (By.XPATH, "//button[text() = 'Оформить заказ']") # кнопка Оформления заказа
    constructor_button = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and @href='/']") # Кнопка Конструктор
    stellar_burgers_label = (By.XPATH,".//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']") # Логотип Stellar Burgers
    choose_buns_section = (By.XPATH, "//div[contains(@class, 'tab')]//span[text()='Булки']") # Переход к разделу выбора булок
    choose_sauces_section = (By.XPATH, "//div[contains(@class, 'tab')]//span[text()='Соусы']") # Переход к разделу выбора соусов
    choose_fillings_section = (By.XPATH, "//div[contains(@class, 'tab')]//span[text()='Начинки']") # Переход к разделу выбора начинки
    create_burger_label = (By.XPATH, "//h1[text() = 'Соберите бургер']") # Надпись Соберите бургер
    current_section = (By.XPATH, "//div[contains(@class, 'tab') and contains(@class, 'current')]") # выбранный раздел создания бургера

class LoginPageLocators:
    email_input = (By.XPATH, "//label[text() = 'Email']/following-sibling::input") # поле ввода Email
    password_input = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input") # поле ввода Пароль
    login_button = (By.XPATH, "//button[text() = 'Войти']") # кнопка Войти
    restore_password_link = (By.XPATH, "//a[@href='/forgot-password']") # кнопка Восстановить пароль
    registration_link = (By.XPATH, "//a[@href='/register']") # Кнопка для перехода на страницу регистрации
    login_label = (By.XPATH, "//h2[text() = 'Вход']") # надпись Вход
    stellar_burgers_label = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']")# Логотип Stellar Burgers

class RegistrationPageLocators:
    name_reg_input = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input") # поле ввода Имя
    email_reg_input = (By.XPATH, "//label[text() = 'Email']/following-sibling::input") # поле ввода Логин
    password_reg_input = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input") # поле ввода Пароль
    error_message = (By.XPATH, "//p[text() = 'Некорректный пароль']") # текст ошибки
    registration_label = (By.XPATH, "//h2[text() = 'Регистрация']") # надпись Регистрация
    registration_button = (By.XPATH, "//button[text() = 'Зарегистрироваться']") # кнопка Зарегистрироваться
    login_button = (By.XPATH, "//a[@href='/login']") # кнопка Войти на странице регистрации

class PersonalAccountLocators:
    logout_button = (By.XPATH, "//button[text() = 'Выход']") # кнопка выхода из аккаунта
    history_order_button = (By.XPATH, "//button[text() = 'История заказов']") # кнопка просмотра истории заказов
