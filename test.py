from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("https://www.amazon.ca/")

# Find the search input field by its ID and enter a search query
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Sony Playstation 5")  # Replace with your desired search query
search_box.send_keys(Keys.RETURN)

# Wait for the search results container to be present
wait = WebDriverWait(driver, 20)
search_results_container = wait.until(EC.presence_of_element_located((By.ID, "search")))

# Wait for the individual search result elements to be visible
wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".s-result-item")))

# Find all individual search result elements within the container
search_results = driver.find_elements(By.CSS_SELECTOR, ".s-result-item")

# Initialize a list to store the data for the first 10 results
first_10_results = []

# Iterate through the search results and extract data for the first 10
for result in search_results[:10]:
    try:
        title = result.find_element(By.CSS_SELECTOR, "h2 a").text
        price = result.find_element(By.CSS_SELECTOR, "a-price").text
        link = result.find_element(By.CSS_SELECTOR, "h2 a").get_attribute("href")

        # Store the data for this result in a dictionary
        result_data = {
            "Title": title,
            "Price": price,
            "Link": link,
        }

        first_10_results.append(result_data)
    except Exception as e:
        print(f"An error occurred while extracting data: {e}")

# Print the data for the first 10 results
for index, result_data in enumerate(first_10_results, start=1):
    print(f"Result {index}:")
    print(f"Title: {result_data.get('Title', 'N/A')}")
    print(f"Price: {result_data.get('Price', 'N/A')}")
    print(f"Link: {result_data.get('Link', 'N/A')}")
    print("\n")

# Close the browser when done
driver.quit()
