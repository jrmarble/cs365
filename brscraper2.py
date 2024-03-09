#Judson Marble
#cs365
#brscraper2

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace 'your_webdriver_path' with the path to your WebDriver executable
driver_path = 'your_webdriver_path'
driver = webdriver.Chrome(executable_path=driver_path)

# Function to scrape advanced stats for a single player
def scrape_advanced_stats(driver, player_name):
    # Navigate to Basketball Reference search
    driver.get("https://www.basketball-reference.com/")
    search_box = driver.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys(player_name)
    search_box.send_keys(Keys.RETURN)
    
    try:
        # Wait for the search results to load and click the first result
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-item-name a"))).click()
        
        # Navigate to the advanced stats tab
        advanced_stats_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Advanced")))
        advanced_stats_link.click()
        
        # Scrape the required advanced stats (as an example, we're scraping PER and WS)
        per = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "per"))).text
        ws = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "ws"))).text
        
        return {"Name": player_name, "PER": per, "WS": ws}
    except Exception as e:
        print(f"Error scraping data for {player_name}: {e}")
        return {"Name": player_name, "PER": None, "WS": None}

# Read the list of player names from the CSV file
input_csv = "players.csv"  # Update with the path to your input CSV file
player_names_df = pd.read_csv(input_csv)

# Initialize a DataFrame to store the scraped data
scraped_data = pd.DataFrame(columns=["Name", "PER", "WS"])

# Scrape advanced stats for each player
for player_name in player_names_df["Name"]:
    player_stats = scrape_advanced_stats(driver, player_name)
    scraped_data = scraped_data.append(player_stats, ignore_index=True)
    time.sleep(1)  # Be respectful in your scraping

# Save the scraped data to a new CSV file
scraped_data.to_csv("nba_player_advanced_stats.csv", index=False)

# Close the WebDriver
driver.quit()
