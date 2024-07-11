from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def download_video(url):
    # Set up Chrome options
    options = Options()
    # Uncomment below if you want to run in headless mode
    options.add_argument("--headless")
    # if using proxy
    # proxy = "p.webshare.io:9999"

    # options.add_argument(f"--proxy-server={proxy}")

    # Initialize Chrome driver
    driver = webdriver.Chrome(options=options)

    try:
        # Open the URL
        driver.get(url)
        
        # Find the video element and get its source URL
        video_element = driver.find_element(By.TAG_NAME, 'video')
        video_source_url = video_element.get_attribute('src')
        
        # Navigate to the video source URL
        driver.get(video_source_url)
        
        # Wait for some time (adjust as necessary)
        time.sleep(5)  # Wait for 5 seconds (adjust this if needed)
        
        # Get the current URL (which should be the direct video URL)
        current_url = driver.current_url
        print(current_url)
        return current_url

    
    finally:
        # Close the browser
        driver.quit()

# # Example usage:
# video_url = "https://example.com/video"
# direct_video_url = download_video(video_url)
# print("Direct video URL:", direct_video_url)
