from pages.base_page import BasePage
from pages.locators import *
from config import *
import time, os

class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        url = os.getenv("LOGIN_URL") or 'https://www.labirint.ru/'
        driver.get(url)

        # создаём необходимые элементы
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.code_login = driver.find_element(*AuthLocators.AUTH_CODE_LOGIN)
        self.btn_entry = driver.find_element(*AuthLocators.AUTH_BTN_ENTRY)

        time.sleep(3)



    def btn_click(self):
        self.btn.click()
        time.sleep(2)
        return btn

    def enter_login(self, value):
        self.code_login.click()
        self.code_login.clear()
        time.sleep(3)
        self.code_login.send_keys(value)
        time.sleep(7)
        return code_login

    def btn_entry_click(self):
        self.btn_entry.click()
        return btn_entry

    def auth_mycab_click(self):
        self.auth_mycab.click()
        return auth_mycab


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'
        driver.get(url)

        self.sidebar_personal = driver.find_elements(*MainpageLocators.MAIN_SIDEBAR_PERSONAL)
        self.main_mess = driver.find_element(*MainpageLocators.MAIN_MESS)
        self.main_mylab = driver.find_element(*MainpageLocators.MAIN_MYLAB)
        self.main_reserve = driver.find_element(*MainpageLocators.MAIN_RESERVE)
        self.main_store = driver.find_element(*MainpageLocators.MAIN_STORE)
        self.main_delivery = driver.find_element(*MainpageLocators.MAIN_DELIVERY)
        self.main_rat = driver.find_element(*MainpageLocators.MAIN_RAT)
        self.main_new = driver.find_element(*MainpageLocators.MAIN_NEW)
        self.main_discounts = driver.find_element(*MainpageLocators.MAIN_DISCOUNTS)
        self.main_tel = driver.find_element(*MainpageLocators.MAIN_TEL)
        self.main_cont = driver.find_element(*MainpageLocators.MAIN_CONT)
        self.main_support = driver.find_element(*MainpageLocators.MAIN_SUPPORT)
        self.main_points = driver.find_element(*MainpageLocators.MAIN_POINTS)

    def visit(self):
        return self.driver.get(self.url)

    def main_delivery(self):
        return self.driver.find_element_by_xpath('//a[contains(text(), "Доставка и оплата")]')

class SchoolPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        url = os.getenv("SCHOOL_URL") or 'https://www.labirint.ru/school/'
        driver.get(url)

        self.school_main_menu = driver.find_elements(*SchoolLocators.SCHOOL_MAIN_MENU)
        self.school_all = driver.find_element(*SchoolLocators.SCHOOL_ALL)
        self.school_textbooks = driver.find_element(*SchoolLocators.SCHOOL_TEXTBOOKS)
        self.school_ege = driver.find_element(*SchoolLocators.SCHOOL_EGE)
        self.school_oge = driver.find_element(*SchoolLocators.SCHOOL_OGE)
        self.school_vpr = driver.find_element(*SchoolLocators.SCHOOL_VPR)
        self.school_preparation = driver.find_element(*SchoolLocators.SCHOOL_PREPARATION)
        self.school_stationery = driver.find_element(*SchoolLocators.SCHOOL_STATIONERY)
        self.school_price_from = driver.find_element(*SchoolLocators.SCHOOL_PRICE_FROM)
        self.school_price_upto = driver.find_element(*SchoolLocators.SCHOOL_PRICE_UPTO)
        self.school_price_discount = driver.find_element(*SchoolLocators.SCHOOL_PRICE_DISCOUNT)
        self.school_filter_edsyst = driver.find_element(*SchoolLocators.SCHOOL_FILTER_EDSYST)
        self.school_filter_typesmat = driver.find_element(*SchoolLocators.SCHOOL_FILTER_TYPESMAT)
        self.school_filter_publish = driver.find_element(*SchoolLocators.SCHOOL_FILTER_PUBLISH)
        self.school_filter_author = driver.find_element(*SchoolLocators.SCHOOL_FILTER_AUTHOR)
        self.school_searchbtn_show = driver.find_element(*SchoolLocators.SCHOOL_SEARCHBTN_SHOW)
        self.school_searchbtn_reset = driver.find_element(*SchoolLocators.SCHOOL_SEARCHBTN_RESET)


class GamesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        url = os.getenv("GAMES_URL") or 'https://www.labirint.ru/games/'
        driver.get(url)

        self.games_search_btn = driver.find_element(*GamesLocators.GAMES_SEARCH_BTN)
        self.games_creativity = driver.find_element(*GamesLocators.GAMES_CREATIVITY)
        self.games_toys = driver.find_element(*GamesLocators.GAMES_TOYS)
        self.games_type = driver.find_element(*GamesLocators.GAMES_TYPE)
        self.games_available = driver.find_element(*GamesLocators.GAMES_AVAILABLE)
        self.games_price = driver.find_element(*GamesLocators.GAMES_PRICE)
        self.games_correction = driver.find_element(*GamesLocators.GAMES_CORRECTION)
        self.games_first_new = driver.find_element(*GamesLocators.GAMES_FIRST_NEW)
        self.games_view_cover = driver.find_element(*GamesLocators.GAMES_VIEW_COVER)
        self.games_view_table = driver.find_element(*GamesLocators.GAMES_VIEW_TABLE)
        self.games_subscr = driver.find_element(*GamesLocators.GAMES_SUBSCR)


class OfficePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        url = os.getenv("OFFICE_URL") or 'https://www.labirint.ru/office/'
        driver.get(url)

        self.stationery_categories = driver.find_elements(*StationeryLocators.STATIONERY_CATEGORIES)
        self.stationery_important_all = driver.find_element(*StationeryLocators.STATIONERY_IMPORTANT_ALL)
        self.stationery_important_middle = driver.find_element(*StationeryLocators.STATIONERY_IMPORTANT_MIDDLE)
        self.stationery_important_elementary = driver.find_element(*StationeryLocators.STATIONERY_IMPORTANT_ELEMENTARY)
        self.stationery_access = driver.find_element(*StationeryLocators.STATIONERY_ACCESS)
        self.stationery_folder = driver.find_element(*StationeryLocators.STATIONERY_FOLDER)
        self.stationery_globe = driver.find_element(*StationeryLocators.STATIONERY_GLOBE)
        self.stationery_cover = driver.find_element(*StationeryLocators.STATIONERY_COVER)
        self.stationery_office = driver.find_element(*StationeryLocators.STATIONERY_OFFICE)
        self.stationery_writing = driver.find_element(*StationeryLocators.STATIONERY_WRITING)
        self.stationery_drawing = driver.find_element(*StationeryLocators.STATIONERY_DRAWING)
        self.stationery_painting = driver.find_element(*StationeryLocators.STATIONERY_PAINTING)
        self.stationery_bags = driver.find_element(*StationeryLocators.STATIONERY_BAGS)
        self.stationery_school_supplies = driver.find_element(*StationeryLocators.STATIONERY_SCHOOL_SUPPLIES)

class RatingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        url = os.getenv("RATING_URL") or 'https://www.labirint.ru/rating/?id_genre=-1&nrd=1'
        driver.get(url)

        self.rat_books = driver.find_elements(*RatingLocators.RAT_PRICES)