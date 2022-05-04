from pages.labirint import *
from tests.test_data import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_auth_page(selenium):
    page = AuthPage(selenium)
    page.visit()
    page.btn_click()
    input_form = WebDriverWait(selenium, 10)
    assert input_form.until(EC.presence_of_element_located(By.ID, '_inputnamecode_33'))
    page.enter_login("C445-4740-B91D")
    time.sleep(3)
    page.btn_entry_click()
    time.sleep(8)
    page.btn_click()
    time.sleep(2)
    assert page.get_relative_link() == '/cabinet/'

def test_visit(selenium):
    page = MainPage(selenium)
    page.visit()
    assert page.main_delivery().is_displayed()


def test_school_main_menu(selenium):
    page = SchoolPage(selenium)
    school_main_menu = page.school_main_menu
    for i in range(len(school_main_menu)):
        for j in school_main_menu_list:
            assert j in school_main_menu(i).text

def test_stationery_categories(selenium):
    page = OfficePage(selenium)
    stationery_categories = page.stationery_categories
    for i in range(len(stationery_categories)):
        for j in stationery_categories_list:
            assert j in stationery_categories(i).text

def test_sidebar_personal(selenium):
    page = MainPage(selenium)
    sidebar_personal = page.sidebar_personal
    for i in range(len(sidebar_personal)):
        for j in sidebar_personal_list:
            assert j in sidebar_personal(i).text

def test_main_mess(selenium):
    page = MainPage(selenium)
    page.main_mess.click()
    main_m = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//span[@class="cabinet-menu__nowrap"]'))
    assert 'Код скидки' in main_m.text

def test_main_mylab(selenium):
    page = MainPage(selenium)
    page.main_mylab.click()
    main_ml = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//span[@class="cabinet-menu__nowrap"]'))
    assert 'Личный кабинет' in main_ml.text


def test_main_reserve(selenium):
    page = MainPage(selenium)
    page.main_reserve.click()
    main_r = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//span[@class=" inlineblock pt15 pr10 h1"]'))
    assert 'отложен' in main_r.text
    assert page.get_relative_link() == '/cabinet/putorder/'

def test_main_store(selenium):
    page = MainPage(selenium)
    page.main_store.click()
    main_s = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//a[@data-event-label="myCart"]'))
    assert 'Моя корзина' in main_s.text
    assert page.get_relative_link() == '/cart/'

def test_main_rat(selenium):
    page = MainPage(selenium)
    page.main_rat.click()
    main_ra = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Рейтинг' in main_ra.text
    assert page.get_link_query() == 'id_genre=-1&nrd=1'

def test_main_new(selenium):
    page = MainPage(selenium)
    page.main_new.click()
    main_n = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Новые книги' in main_n.text
    assert page.get_relative_link() == '/novelty/'

def test_main_discounts(selenium):
    page = MainPage(selenium)
    page.main_discounts.click()
    main_disc = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//a[@class="block-link-title"]'))
    assert 'Все акции сегодня' in main_disc.text
    assert page.get_link_query() == 'discount=1'

def test_main_tel(selenium):
    page = MainPage(selenium)
    page.main_tel.click()
    main_t = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//a[@class="btn btn-small btn-primary btn-select"]'))
    assert '8 800 600-95-25' in main_t.text

def test_main_cont(selenium):
    page = MainPage(selenium)
    page.main_cont.click()
    main_с = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Обратная связь' in main_с.text
    assert page.get_relative_link() == '/contact/'

def test_main_support(selenium):
    page = MainPage(selenium)
    page.main_support.click()
    main_sup = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//div[@class="fright"]'))
    assert 'Задать вопрос' in main_sup.text
    assert page.get_relative_link() == '/support/'

def test_main_points(selenium):
    page = MainPage(selenium)
    page.main_points.click()
    time.sleep(2)
    assert page.get_relative_link() == '/maps/'

def test_school_textbooks(selenium):
    page = SchoolPage(selenium)
    page.school_textbooks.click()
    school_t = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//div[@class="mb8"]'))
    assert 'Учебники' in school_t.text
    assert page.get_link_query() == 'stype[]=1&tab=schoolbook'

def test_school_ege(selenium):
    page = SchoolPage(selenium)
    page.school_ege.click()
    school_eg = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//label[@class="checkbox-ui label checked"]'))
    assert 'ЕГЭ' in school_eg.text
    assert page.get_link_query() == 'examtype[]=1&tab=exam1'

def test_school_oge(selenium):
    page = SchoolPage(selenium)
    page.school_oge.click()
    school_og = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//label[@class="checkbox-ui label checked"]'))
    assert 'ОГЭ' in school_og.text
    assert page.get_link_query() == 'examtype[]=2&tab=exam2'

def test_school_vpr(selenium):
    page = SchoolPage(selenium)
    page.school_vpr.click()
    school_vp = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//div[@class="products-row "]/div'))
    for i in range(len(school_vp)):
        assert school_vp[i].get_attribute('data-name') == 'ВПР' or 'провер'
    assert page.get_link_query() == 'id_genre=3053&tab=vpr'

def test_school_preparation(selenium):
    page = SchoolPage(selenium)
    page.school_preparation.click()
    school_prep = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//div[@class="row"]/label[@class="checkbox-ui label checked"]'))
    assert 'Для дошкольников' in school_prep.text
    assert page.get_link_query() == 'preschool[]=1&tab=preschool'

def test_school_stationery(selenium):
    page = SchoolPage(selenium)
    page.school_stationery.click()
    school_stat = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Канцелярские товары' in school_stat.text
    assert page.get_relative_link() == '/office/'

def test_games_search_btn(selenium):
    page = GamesPage(selenium)
    page.games_search_btn.click()
    games_s_b = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//input[@class="text navisort-find-text"]'))
    assert 'Введите что-нибудь' in games_s_b.text

def test_games_creativity(selenium):
    page = GamesPage(selenium)
    page.games_creativity.click()
    games_creat = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Детское творчество' in games_creat.text
    assert page.get_relative_link() == '/genres/1644/'

def test_games_toys(selenium):
    page = GamesPage(selenium)
    page.games_toys.click()
    games_t = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Игры и Игрушки' in games_t.text
    assert page.get_relative_link() == '/genres/1643/'

def test_games_type(selenium):
    page = GamesPage(selenium)
    page.games_type.click()
    games_ty = WebDriverWait(selenium, 3)
    assert games_ty.until(EC.text_to_be_present_in_element(By.LINK_TEXT, 'Бумажные книги'))

def test_games_available(selenium):
    page = GamesPage(selenium)
    page.games_available.click()
    games_av = WebDriverWait(selenium, 3)
    assert games_av.until(EC.text_to_be_present_in_element(By.LINK_TEXT, 'В наличии'))

def test_games_price(selenium):
    page = GamesPage(selenium)
    page.games_price.click()
    games_pr = WebDriverWait(selenium, 3)
    assert games_pr.until(EC.text_to_be_present_in_element(By.LINK_TEXT, 'Со скидкой'))

def test_games_correction(selenium):
    page = GamesPage(selenium)
    page.games_correction.click()
    games_cor = WebDriverWait(selenium, 3)
    assert games_cor.until(EC.text_to_be_present_in_element(By.LINK_TEXT, 'ДЕТСКОЕ ТВОРЧЕСТВО'))

def test_games_first_new(selenium):
    page = GamesPage(selenium)
    page.games_first_new.click()
    games_fn = WebDriverWait(selenium, 3)
    assert games_fn.until(EC.text_to_be_present_in_element(By.LINK_TEXT, 'новинки'))

def test_games_view_table(selenium):
    page = GamesPage(selenium)
    page.games_view_table.click()
    time.sleep(2)
    assert page.get_link_query() == 'display=table'

def test_games_view_cover(selenium):
    page = GamesPage(selenium)
    page.games_view_cover.click()
    time.sleep(2)
    assert page.get_link_query() == 'display=cover'

def test_games_subscr(selenium):
    page = GamesPage(selenium)
    page.games_subscr.click()
    games_sub = WebDriverWait(selenium, 3)
    assert games_sub.until(EC.text_to_be_present_in_element(By.LINK_TEXT, 'на новинки жанра'))

def test_stationery_categories(selenium):
    page = OfficePage(selenium)
    page.stationery_categories.click()
    stationery_cat = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Канцелярские товары' in stationery_cat
    assert page.get_relative_link() == '/office/'

def test_stationery_important_all(selenium):
    page = OfficePage(selenium)
    page.stationery_important_all.click()
    stationery_imp_all = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//div[contains(text(), "Самое важное")]'))
    assert 'для школы' in stationery_imp_all

def test_stationery_important_middle(selenium):
    page = OfficePage(selenium)
    page.stationery_important_middle.click()
    stationery_imp_mid = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//div[contains(text(), "Самое важное для")]'))
    assert 'средней' in stationery_imp_mid

def test_stationery_important_elementary(selenium):
    page = OfficePage(selenium)
    page.stationery_important_elementary.click()
    stationery_imp_el = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.XPATH, '//div[contains(text(), "Самое важное для")]'))
    assert 'начальной' in stationery_imp_el

def test_stationery_access(selenium):
    page = OfficePage(selenium)
    page.stationery_access.click()
    stationery_acc = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Аксессуары для книг' in stationery_acc
    assert page.get_relative_link() == '/genres/2300/'

def test_stationery_folder(selenium):
    page = OfficePage(selenium)
    page.stationery_folder.click()
    stationery_fold = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Папки, скоросшиватели' in stationery_fold
    assert page.get_relative_link() == '/genres/1367/'

def test_stationery_globe(selenium):
    page = OfficePage(selenium)
    page.stationery_globe.click()
    stationery_gl = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Глобусы' in stationery_gl
    assert page.get_relative_link() == '/genres/1500/'

def test_stationery_cover(selenium):
    page = OfficePage(selenium)
    page.stationery_cover.click()
    stationery_cov = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Обложки для документов' in stationery_cov
    assert page.get_relative_link() == '/genres/2646/'

def test_stationery_office(selenium):
    page = OfficePage(selenium)
    page.stationery_office.click()
    stationery_off = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Офисная канцелярия' in stationery_off
    assert page.get_relative_link() == '/genres/1444/'


def test_stationery_writing(selenium):
    page = OfficePage(selenium)
    page.stationery_writing.click()
    stationery_writ = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Письменные принадлежности' in stationery_writ
    assert page.get_relative_link() == '/genres/1321/'

def test_stationery_drawing(selenium):
    page = OfficePage(selenium)
    page.stationery_drawing.click()
    stationery_draw = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Принадлежности для черчения' in stationery_draw
    assert page.get_relative_link() == '/genres/1394/'

def test_stationery_painting(selenium):
    page = OfficePage(selenium)
    page.stationery_painting.click()
    stationery_paint = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Рисование' in stationery_paint
    assert page.get_relative_link() == '/genres/1405/'

def test_stationery_bags(selenium):
    page = OfficePage(selenium)
    page.stationery_bags.click()
    stationery_b = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Сумки' in stationery_b
    assert page.get_relative_link() == '/genres/2752/'

def test_stationery_school_supplies(selenium):
    page = OfficePage(selenium)
    page.stationery_school_supplies.click()
    stationery_ss = WebDriverWait(selenium, 10).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
    assert 'Товары для школы' in stationery_ss
    assert page.get_relative_link() == '/genres/1496/'

def test_rat_prices(selenium):
    page = RatingPage(selenium)
    rat_prices = page.rat_books
    for i in range(len(rat_prices)):
        assert rat_prices[i].get_attribute('data-discount-price') != ''

def test_rat_photos(selenium):
    page = RatingPage(selenium)
    rat_photos = page.rat_books
    for i in range(len(rat_photos)):
        assert rat_photos[i].get_attribute('src') != ''

def test_rat_stores(selenium):
    page = RatingPage(selenium)
    rat_stores = page.rat_books
    for i in range(len(rat_stores)):
        assert rat_stores[i].get_attribute('class') == 'product-buy buy-avaliable fleft'