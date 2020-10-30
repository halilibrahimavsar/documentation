from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup as bs



def headless_for_windows():
    chrome_opt = Options()
    chrome_opt.headless = True
    ask_for_consumer = input("Open headless ? [y/n] : ")
    if (ask_for_consumer.lower()) == "y":
        return chrome_opt
    elif (ask_for_consumer.lower()) == "n":
        chrome_opt.headless = False
        return chrome_opt
    else:
        return chrome_opt



class OpenWebsite:
    def __init__(self, url, path):
        self.url = url
        self.path = path
        self.page_link = []
        self.page_link_clicked = []
    
    def open_url(self):
        self.browser = Chrome(executable_path=self.path, options=headless_for_windows())
        self.browser.get(self.url)
        self.browser.implicitly_wait(20)

    
    def search_empty(self):
        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/section[1]/div/div[1]/div[1]/div/form/div[12]/div[1]/input").click()
        self.browser.implicitly_wait(20)

    def change_page(self):
        self.next_links = self.browser.find_elements_by_class_name("next")
        self.browser.implicitly_wait(20)
        for i in self.next_links:
            i.click()
            self.browser.imlicitly_wait(20)
    
    def check_info(self):
        self.bsoup = bs(self.browser.page_source, "lxml")
        print(self.bsoup.find("div",attrs={"class":"annuaire_result_list"}))



    def close(self):
        self.browser.close()
    




if __name__ == "__main__":
    run = OpenWebsite("https://www.escpalumni.org/gene/main.php?langue=uk&base=520", r"C:\Users\avsar\OneDrive\Masaüstü\Chrome-Driver\chromedriver")
    run.open_url()
    run.search_empty()
    run.change_page()


    run.close()




