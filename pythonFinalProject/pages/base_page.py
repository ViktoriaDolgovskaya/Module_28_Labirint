from urllib.parse import urlparse


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.labirint.ru/"
        self.driver.implicitly_wait(5)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def get_url(self):
        url = urlparse(self.driver.current_url)
        return url.netloc

    def get_link_query(self):
        url = urlparse(self.driver.current_url)
        return url.query

    def get_current_url(self):
        return self.driver.current_url

    def visit(self):
        return self.driver.get(self.url)
