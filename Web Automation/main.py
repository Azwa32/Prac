# from: https://www.youtube.com/watch?v=NB8OceGZGjA&t=326s

# for codespaces install:
# install selenium >>pip install selenium
# update the package list >>sudo apt update
# download google chrome >>wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# install google chrome >>sudo dpkg -i google-chrome-stable_current_amd64.deb
# install any other dependacies for chrome >>sudo apt-get install -f
# re-install chrome >>sudo dpkg -i google-chrome-stable_current_amd64.deb
# verify installation >>google-chrome --version

# driver download
# chrome driver download >>wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/linux64/chromedriver-linux64.zip
# unzip driver >> unzip chromedriver-linux64.zip
# delete .zip >> sudo remove chromedriver-linux64.zip
# go into folder and extract driver into folder
# or
# install chrome driver >>pip install chromedriver-binary
# Install version of chrome driver to match version of chrome installed >>pip install chromedriver-binary-sync

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary_sync
import time

# Download chromedriver to current directory.
# (chromedriver version matches installed chrome)
chromedriver_binary_sync.download()

options = Options()
options.add_argument("--headless")  # Ensure GUI is off
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("https://google.com")
print(driver.title)


time.sleep(10)
driver.quit()

