import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

# Initialize Chrome WebDriver with options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://olympics.com/en/paris-2024/medals")

# Wait for the page to load
time.sleep(5)

# Accept cookies by clicking the button
accept_button = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
accept_button.click()

# Scroll and collect the data
scroll_position = 0
medals_data = []

for _ in range(20):
    scroll_position += 350
    driver.execute_script(f'window.scrollTo(0, {scroll_position})')


    # Parse page source using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    medal_list = soup.select('div[data-test-id="virtuoso-item-list"] div[data-testid="noc-row"]')

    for item in medal_list:
        country = item.select_one("span.euzfwma5.emotion-srm-uu3d5n").get_text()
        medal_counts = item.select("span.e1oix8v91")
        gold = medal_counts[1].get_text()
        silver = medal_counts[2].get_text()
        bronze = medal_counts[3].get_text()
        total = item.select_one('span.emotion-srm-5nhv3o').get_text()

        medals_data.append({
            "Country": country,
            "Gold": gold,
            "Silver": silver,
            "Bronze": bronze,
            "Total": total
        })

# Create a DataFrame and save the results to a CSV file
medals_df = pd.DataFrame(medals_data).drop_duplicates()
medals_df.to_csv("Paris2024", index=False)


