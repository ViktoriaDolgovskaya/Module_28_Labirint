from selenium.webdriver.common.by import By


class AuthLocators:
    AUTH_BTN = (By.CLASS_NAME, "js-b-autofade-text")
    AUTH_CODE_LOGIN = (By.ID, "_inputnamecode_33")
    AUTH_BTN_ENTRY = (By.ID, "g-recap-0-btn")


class MainpageLocators:
    MAIN_SIDEBAR_PERSONAL = (By.XPATH, '//ul[@class="b-header-b-personal-e-list ul-justify"]')
    MAIN_MESS = (By.XPATH, '//span[contains(text(), "Сообщения")]')
    MAIN_MYLAB = (By.XPATH, '//span[@class="js-b-autofade-text"]')
    MAIN_RESERVE = (By.XPATH, '//span[contains(text(), "Отложено")]')
    MAIN_STORE = (By.XPATH, '//span[contains(text(), "Корзина")]')
    MAIN_DELIVERY = (By.XPATH, '//a[contains(text(), "Доставка и оплата")]')
    MAIN_CERT = (By.XPATH, '//li[@data-event-content="Сертификаты"]')
    MAIN_RAT = (By.XPATH, '//a[contains(text(), "Рейтинги")]')
    MAIN_NEW = (By.XPATH, '//li[@data-event-content="Новинки"]')
    MAIN_DISCOUNTS = (By.XPATH, '//li[@data-event-content="Скидки"]')
    MAIN_TEL = (By.XPATH, '//li//a[contains(text(), "8 800")]')
    MAIN_CONT = (By.XPATH, '//a[contains(text(), "Контакты")]')
    MAIN_SUPPORT = (By.XPATH, '//li[@data-event-content="Поддержка"]')
    MAIN_POINTS = (By.XPATH, '//li[@data-event-content="Пункты самовывоза"]')
    MAIN_RAT_PRICES = (By.XPATH, '//div[@class="products-row "]')

class RatingLocators:
    RAT_PRICES = (By.XPATH, '//div[@class="products-row "]')

class StationeryLocators:
    STATIONERY_CATEGORIES = (By.XPATH, '//ul[@class="genre-list genre-list-all "]')
    STATIONERY_IMPORTANT_ALL = (By.XPATH, '//label[contains(text(), "все")]')
    STATIONERY_IMPORTANT_MIDDLE = (By.XPATH, '//label[contains(text(), "средняя")]')
    STATIONERY_IMPORTANT_ELEMENTARY = (By.XPATH, '//label[contains(text(), "начальная")]')
    STATIONERY_ACCESS = (By.XPATH, '//a[contains(text(), "Аксессуары для книг")]')
    STATIONERY_FOLDER = (By.XPATH, '//a[contains(text(), "скоросшиватели")]')
    STATIONERY_GLOBE = (By.XPATH, '//a[contains(text(), "Глобусы")]')
    STATIONERY_COVER = (By.XPATH, '//a[contains(text(), "Обложки")]')
    STATIONERY_OFFICE = (By.XPATH, '//a[contains(text(), "Офисн")]')
    STATIONERY_WRITING = (By.XPATH, '//a[contains(text(), "Письменн")]')
    STATIONERY_DRAWING = (By.XPATH, '//a[contains(text(), "черчен")]')
    STATIONERY_PAINTING = (By.XPATH, '//a[contains(text(), "Рисование")]')
    STATIONERY_BAGS = (By.XPATH, '//a[contains(text(), "Сумки")]')
    STATIONERY_SCHOOL_SUPPLIES = (By.XPATH, '//a[contains(text(), "Товары для школы")]')

class GamesLocators:
    GAMES_SEARCH_BTN = (By.XPATH, '//span[@class="find-button__hover"]')
    GAMES_CREATIVITY = (By.XPATH, '//a[contains(text(), "Детское творчество")]')
    GAMES_TOYS = (By.XPATH, '//a[contains(text(), "Игры и игрушки")]')
    GAMES_TYPE = (By.CLASS_NAME, "navisort-part navisort-filter navisort-part-1 fleft")
    GAMES_AVAILABLE = (By.CLASS_NAME, "navisort-part navisort-filter navisort-part-2 fleft")
    GAMES_PRICE = (By.CLASS_NAME, "navisort-part navisort-filter navisort-part-3 fleft")
    GAMES_CORRECTION = (By.CLASS_NAME, "navisort-part navisort-filter navisort-part-4 fleft")
    GAMES_ALL_FILTERS = (By.CLASS_NAME, "navisort-part navisort-filter navisort-part-5 fleft")
    GAMES_FIRST_NEW = (By.CLASS_NAME, "navisort-part navisort-sortings navisort-part-8 fright")
    GAMES_VIEW_COVER = (By.XPATH, '//a[@title="обложки"]')
    GAMES_VIEW_TABLE = (By.XPATH, '//a[@title="таблицей"]')
    GAMES_SUBSCR = (By.CLASS_NAME, "navisort-part navisort-subscribes navisort-part-6 fright ")

class SchoolLocators:
    SCHOOL_MAIN_MENU = (By.XPATH, '//ul[@class="school-cap-menu"]')
    SCHOOL_ALL = (By.XPATH, '//*[@class="school-cap-menu"]//a[@href="/school/"]')
    SCHOOL_TEXTBOOKS = (By.XPATH, '//ul/li/a[contains(text(), "Учебники")]')
    SCHOOL_EGE = (By.XPATH, '//*[@class="school-cap-menu"]//a[contains(text(), "ЕГЭ")]')
    SCHOOL_OGE = (By.XPATH, '//*[@class="school-cap-menu"]//a[contains(text(), "ОГЭ")]')
    SCHOOL_VPR = (By.XPATH, '//ul/li/a[contains(text(), "ВПР")]')
    SCHOOL_PREPARATION = (By.XPATH, '//a[@href="/school/?preschool[]=1&tab=preschool"]')
    SCHOOL_STATIONERY = (By.XPATH, '//*[@class="school-cap-menu"]//a[@href="/office/"]')
    SCHOOL_PRICE_FROM = (By.XPATH, '//*[@class="inputs"]//input[@name="price_min"]')
    SCHOOL_PRICE_UPTO = (By.XPATH, '//*[@class="inputs"]//input[@name="price_max"]')
    SCHOOL_PRICE_DISCOUNT = (By.XPATH, '//input[@type="checkbox" and @name="discount"]')
    SCHOOL_FILTER_EDSYST = (By.XPATH, '//span[contains(text(), "Учебные системы")]')
    SCHOOL_FILTER_TYPESMAT = (By.XPATH, '//span[contains(text(), "Типы материалов")]')
    SCHOOL_FILTER_PUBLISH = (By.XPATH, '//span[contains(text(), "Издательства")]')
    SCHOOL_FILTER_AUTHOR = (By.XPATH, '//span[contains(text(), "Авторы")]')
    SCHOOL_SEARCHBTN_SHOW = (By.XPATH, '//input[@class="btn btn-primary btn-small"]')
    SCHOOL_SEARCHBTN_RESET = (By.CLASS_NAME, "act-reset")
