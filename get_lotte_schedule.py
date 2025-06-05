import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

today = datetime.now().strftime("%Y%m%d")
url = f"https://sports.news.naver.com/kbaseball/schedule/index?date={today}"

driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

games = soup.select('.sch_tb tbody tr')
lotte_games = []

for game in games:
    if '롯데' in game.text:
        lotte_games.append(game.text.strip())

with open("lotte_today.json", "w", encoding="utf-8") as f:
    json.dump(lotte_games, f, ensure_ascii=False, indent=2)
