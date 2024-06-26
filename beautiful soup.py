from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to the chromedriver executable
service = Service('path/to/chromedriver')  # Replace with the actual path

# Set up the WebDriver
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get('https://example-news-website.com')

# Wait for the page to load
time.sleep(5)

# Extract dynamic content
articles = driver.find_elements(By.CSS_SELECTOR, 'h2.article-title')  # Adjust the selector based on the website's structure
titles = [article.text for article in articles]

# Close the browser
driver.quit()

# Print the titles
for title in titles:
    print(title)

# Save to CSV
df = pd.DataFrame(titles, columns=['Title'])
df.to_csv('dynamic_article_titles.csv', index=False)
print('Data saved to dynamic_article_titles.csv')
