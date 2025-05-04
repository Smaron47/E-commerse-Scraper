#E-Commerce Product Scraper – Code Documentation

**Developed by:** Smaron Biswas  
**License:** MIT  
**Year:** 2024

---

## Overview

This project is a Python-based automated web scraper designed to extract product data from an e-commerce website. It leverages Selenium (with headless Chrome) and BeautifulSoup to handle dynamic web pages by scrolling down to load content and then parsing the HTML to extract product links and details.

**Key Outputs:**
- A text file (`accessories_urls.txt`) containing the full URLs of products.
- A CSV file (`accessories_details.csv`) storing detailed product information including category, frame dimensions, brand, product name, price, and gallery images.

**SEO Keywords:**  
Web Scraping, Selenium, Headless Chrome, BeautifulSoup, Python Automation, E-commerce Data Extraction, CSV Export, Product Details Scraper, Dynamic Content Extraction

---

## Project Structure & Workflow

The code is organized into several key functions that work together to perform the scraping and data extraction tasks:

1. **`scrape_product_links(url, num_scrolls=200)`**
   - **Functionality:**
     - Initializes Selenium with headless Chrome.
     - Opens the provided URL and scrolls repeatedly (using `Keys.PAGE_DOWN`) to load dynamic content.
     - Parses the HTML with BeautifulSoup.
     - Extracts product link fragments, constructs full URLs (appending a base URL), and saves them to `accessories_urls.txt`.
   - **Keywords:** URL Extraction, Dynamic Content, Selenium Scrolling, HTML Parsing

2. **`scrape_product_details(url)`**
   - **Functionality:**
     - Uses Selenium to open each product URL in headless mode.
     - Retrieves the page source and parses it with BeautifulSoup.
     - Extracts product details such as category, frame dimensions, brand name, product name, price, and gallery image sources.
     - Returns the data as a dictionary.
   - **Keywords:** Product Data Extraction, Detail Scraper, BeautifulSoup Parsing, Error Logging

3. **`append_to_csv(data, csv_file)`**
   - **Functionality:**
     - Opens or creates a CSV file.
     - Checks if the file is empty; if so, writes header rows.
     - Appends each product’s data as a new row into `accessories_details.csv`.
   - **Keywords:** CSV Export, Data Storage, Python CSV Writer

---

## Detailed Code Analysis

### Initialization & Headless Setup
- **Purpose:** Configures Selenium to run in headless mode, allowing the script to automate web browser tasks without launching a visible UI.
- **Implementation:** Uses `Options()` from Selenium and adds the `"--headless"` argument.
- **SEO Keywords:** Headless Chrome, Selenium WebDriver, Browser Automation

### Dynamic Content Handling
- **Purpose:** Automatically scrolls through the page to ensure all dynamic content (lazy-loaded elements) is retrieved.
- **Implementation:** Loops using `Keys.PAGE_DOWN` and `time.sleep(1)` to simulate a user scrolling.
- **SEO Keywords:** Dynamic Web Content, Lazy Loading, Selenium Scrolling

### HTML Parsing with BeautifulSoup
- **Purpose:** After scrolling, BeautifulSoup parses the page source to locate product elements using specific CSS classes.
- **Implementation:** The code calls `soup.find_all()` with a target CSS class to gather links.
- **SEO Keywords:** HTML Parsing, BeautifulSoup, Data Extraction

### URL Construction & File Output
- **Purpose:** Converts relative URL fragments into complete URLs by appending them to the main domain.
- **Implementation:** Combines fragments with a hardcoded base URL and writes the results to `accessories_urls.txt`.
- **SEO Keywords:** URL Construction, File Output, Data Persistence

### Product Detail Extraction
- **Purpose:** Visits each product’s page individually to extract detailed information.
- **Implementation:** Searches for specific CSS selectors for category, dimensions, brand name, product name, price, and gallery images.
- **SEO Keywords:** Product Data Extraction, Web Scraper Details, HTML Data Parsing

### CSV Data Appending
- **Purpose:** Consolidates and saves product details into a CSV format.
- **Implementation:** Uses `csv.DictWriter` to write headers if the file is empty, then appends product rows.
- **SEO Keywords:** CSV Export, Data Storage, Python CSV Module

---

## Installation & Usage

### Prerequisites:
- **Python 3.x** must be installed.
- **Required Packages:**
  - **Selenium:** Install via `pip install selenium`
  - **BeautifulSoup4:** Install via `pip install beautifulsoup4`
- **Chrome WebDriver:**
  - Download the appropriate version from [ChromeDriver](https://sites.google.com/chromium.org/driver).
  - Ensure the WebDriver is in your system PATH, or specify its location in the code.

### Running the Script:
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
