import re
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create the my_files directory if it doesn't exist
if not os.path.exists('my_files'):
    os.mkdir('my_files')

options = Options()
options.add_argument("--headless")  # add headless option
driver = webdriver.Chrome('C-D\chromedriver.exe', options=options)

brand_url = 'https://www.amazon.com/s?k=laptop+asus'
driver.get(brand_url)

products = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
    (By.XPATH, "//div[@data-component-type='s-search-result']")))

for product in products:
    title_element = product.find_element(By.XPATH, ".//h2/a")
    title = title_element.text

    price_element = product.find_element(
        By.XPATH, ".//span[@class='a-price-whole']")
    price = price_element.text

    link = title_element.get_attribute("href")

    # save data into a file
    max_title_length = 20
    title = title[:max_title_length].strip()
    file_path = os.path.join('my_files', f'{title}.txt')
    with open(file_path, 'w') as f:
        f.write(f'Title: {title}\nPrice: {price}\nLink: {link}')


data = []

file_dir = os.path.join(os.getcwd(), 'my_files')
for filename in os.listdir(file_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(file_dir, filename)
        with open(file_path, 'r') as f:
            contents = f.read()
            title_match = re.search(r'Title: (.+)', contents)
            price_match = re.search(r'Price: (.+)', contents)
            link_match = re.search(r'Link: (.+)', contents)

            if title_match and price_match and link_match:
                title = title_match.group(1)
                price = price_match.group(1)
                link = link_match.group(1)

                data.append({'title': title, 'price': price, 'link': link})

driver.quit()  # quit the driver
