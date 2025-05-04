
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by  import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
import time

def scrape_product_links(url, num_scrolls=200):
    # Set up Chrome options to run headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Initialize the Chrome WebDriver with the specified options
    driver = webdriver.Chrome()

    try:
        # Load the URL
        driver.get(url)

        # Scroll down multiple times
        for _ in range(num_scrolls):
            body_element = driver.find_element(By.TAG_NAME, 'body')
            body_element.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)  # Adjust the sleep time as needed

        # Get the page source after scrolling
        page_source = driver.page_source

        # Parse the HTML content of the page
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find all elements with class "common_productCard__DwpEm undefined eyeTest_productCard__dkiHG"
        product_elements = soup.find_all(class_='common_productCard__DwpEm undefined eyeTest_productCard__dkiHG')

        # Extract href attributes from the elements
        product_urls = [element['href'] for element in product_elements]

        # Combine URLs with the main URL
        main_url = 'https://www.titaneyeplus.com'
        full_urls = [main_url + url for url in product_urls]

        # Save the list of URLs to a file
        with open('accessories_urls.txt', 'w') as file:
            for full_url in full_urls:
                file.write(full_url + '\n')

        return full_urls

    finally:
        # Close the WebDriver
        driver.quit()



def scrape_product_details(url):
    # Set up Chrome options to run headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Initialize the Chrome WebDriver with the specified options
    driver = webdriver.Chrome()

    try:
        # Load the URL
        driver.get(url)

        # Get the page source after scrolling
        page_source = driver.page_source

        # Parse the HTML content of the page
        soup = BeautifulSoup(page_source, 'html.parser')

        # Extract category
        category_element = soup.find(class_='breadcrumb common_breadcrumb__DlZdr')
        category = category_element.get_text(strip=True) if category_element else ""

        # Extract frame dimensions
        frame_dimensions_element = soup.find(class_='details_copy__aMoPX')
        frame_dimensions = frame_dimensions_element.get_text(strip=True) if frame_dimensions_element else ""

        # Extract brand name
        brand_name_element = soup.find(class_='details_brandName__Wrovx')
        brand_name = brand_name_element.get_text(strip=True) if brand_name_element else ""

        # Extract product name
        product_name_element = soup.find(class_='common_mediumTitle__OzGx_ details_mediumTitle__U_lz8')
        product_name = product_name_element.get_text(strip=True) if product_name_element else ""

        # Extract price
        price_element = soup.find(class_='details_pricing__7Eg6Q')
        price = price_element.get_text(strip=True) if price_element else ""

        # Extract gallery image sources
        gallery_elements = soup.find_all('img', alt='gallery')
        gallery_sources = [element['src'] for element in gallery_elements]

        return {
            'Category': category,
            'Frame Dimensions': frame_dimensions,
            'Brand Name': brand_name,
            'Product Name': product_name,
            'Price': price,
            'Gallery Images': gallery_sources,
        }
    except:
        print(f"Error in url : {url}")
    finally:
        # Close the WebDriver
        print(f"Done Url : {url}")

def append_to_csv(data, csv_file):
    with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Category', 'Frame Dimensions', 'Brand Name', 'Product Name', 'Price', 'Gallery Images']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if the file is empty, and if so, write the header
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow(data)

# Example usage
#url = 'https://example.com/product-page'
#url = 'https://www.titaneyeplus.com/product/black-bugeye-rimmed-sunglasses-from-fastrack-p101bk1'
# Example usage
base_url = 'https://example.com/product-category'
url_list = scrape_product_links('https://www.titaneyeplus.com/accessories')


# Now, you can use the URLs from the list to fetch the product names using the previous code
csv_file = 'accessories_details.csv'

for product_url in url_list:
    product_data = scrape_product_details(product_url)
    append_to_csv(product_data, csv_file)
