# Amazon Web Scraper

## Introduction
This Python script utilizes the Selenium library to scrape data from Amazon's laptop search results. The script extracts the product title, price, and link for each laptop listed on the page and saves this information to a file in the "my_files" directory. Finally, the script reads the saved files and extracts the same information into a list of dictionaries.

## Prerequisites
- Python 3
- Selenium library
- ChromeDriver executable for Selenium

## Installation

- Create a Virtual Environment
```
  python -m venv venv
```

- Activate The Virtual Environment
### Windows
```
  venv/Scripts/activate
```
### Linux
```
  source venv/bin/activate
```
- Install Requirements
```
  pip install -r requirements.txt
```
- Download WebDriver
1. Go to [This](https://sites.google.com/chromium.org/driver/?pli=1) Page and Download Version Based On Your Chrome Version.
2. Put the ``chromedriver.exe`` file in `C-D` folder.

## Usage

1. Open a command prompt or terminal window.

2. Navigate to the directory where the script is saved.

3. Run the script using the command ``python main.py``.

4. The script will launch a headless Chrome browser and navigate to the search results page for Asus laptops on Amazon.

5. The script will then extract the product title, price, and link for each laptop listed on the page, and save this information to a file in the "my_files" directory.

6. Finally, the script will read the saved files and extract the same information into a list of dictionaries.

7. The resulting list of dictionaries can be used for further processing, such as storing the data in a database or generating a report.

⚠️ Note: The script assumes that the ChromeDriver executable is located in the 'C-D' folder of your computer. If you have placed it in a different location, please update the path accordingly in the code.

## Conclusion
This Amazon web scraper script can be useful for extracting data from various pages on the Amazon website or other e-commerce sites. It demonstrates how the Selenium library can be used to automate web browsing and extract data from web pages.
