from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time

def scrape_videos(query):
    # Set Chrome options
    options = Options()
    # Uncomment below if you want to run in headless mode
    options.add_argument("--headless")
    
    # Initialize Chrome driver
    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to the target webpage
        driver.get(f"https://xgroovy.com/search/{query}")

        # Wait for the page to load (you might need to add explicit wait strategies here if content loads dynamically)
        time.sleep(5)

        # Find all video elements within the list-videos container
        video_elements = driver.find_elements(By.CSS_SELECTOR, '.list-videos .item')

        videos_data = []

        # Iterate over each video element to extract data
        for video in video_elements:
            thumbnail_url = video.find_element(By.CSS_SELECTOR, 'img.thumb').get_attribute('src')
            preview_url = video.find_element(By.CSS_SELECTOR, 'img.thumb').get_attribute('data-preview')
            video_url = video.find_element(By.CLASS_NAME, "popito").get_attribute("href")
            title = video.find_element(By.CLASS_NAME, "title").text
            
            # Store data in dictionary
            video_data = {
                'thumbnail_url': thumbnail_url,
                'preview_url': preview_url,
                'video_url': video_url,
                'title': title
            }
            
            # Append to list
            videos_data.append(video_data)

        # Convert to JSON format
        json_data = json.dumps(videos_data, indent=2)
        print(json_data)
        return json_data

    finally:
        # Release the resources and close the browser
        driver.quit()
