# from: https://www.youtube.com/watch?v=NB8OceGZGjA&t=326s

# for codespaces install:
# update the package list >>sudo apt update
# download google chrome >>wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# install google chrome >>sudo dpkg -i google-chrome-stable_current_amd64.deb
# install any other dependacies for chrome >>sudo apt-get install -f
# re-install chrome >>sudo dpkg -i google-chrome-stable_current_amd64.deb
# verify installation >>google-chrome --version
# download chrome driver >>wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
# open zip >>unzip chromedriver_linux64.zip
# move driver into directory included in path >>sudo mv chromedriver /usr/local/bin/
# remove zip >>rm chromedriver_linux64.zip


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="")
driver = webdriver.Chrome(service=service)

