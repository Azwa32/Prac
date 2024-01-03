# from: https://www.youtube.com/watch?v=NB8OceGZGjA&t=326s

# for codespaces install:
# update the package list >>sudo apt update
# download google chrome >>wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# install google chrome >>sudo dpkg -i google-chrome-stable_current_amd64.deb
# install any other dependacies for chrome >>sudo apt-get install -f
# re-install chrome >>sudo dpkg -i google-chrome-stable_current_amd64.deb
# verify installation >>google-chrome --version
# install chrome driver >>pip install selenium chromedriver-binary

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class PriceScraper:

    def scrape(self):

        input_url = "https://www.google.com"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(input_url)

if __name__ == '__main__':
    scraper = PriceScraper()
    scraper.scrape()

