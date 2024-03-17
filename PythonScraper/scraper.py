from datetime import date, timedelta
import re
from Models.TradeEntry import TradeEntry
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def getTradesByPublishedDate() -> list:
    # Set up Selenium options
    options = Options()
    options.headless = True  # Run Chrome in headless mode

    # Set up the Chrome WebDriver
    # If you want to make chrome not pop up you can fix it here by creating a path for chromium.
    # https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    # Load the webpage
    url = "https://www.capitoltrades.com/trades?per_page=12"
    driver.get(url)

    try:
        # Wait for the table to be loaded
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "q-table")))

        # Find the table
        table = driver.find_element(By.CLASS_NAME, "q-table")

        # Extract data from the table
        rows = table.find_elements(By.TAG_NAME, "tr")
        table_data = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            row_data = []
            for cell in cells:
                # Check if the td element has the class "q-column--owner"
                if "q-column--owner" in cell.get_attribute("class"):
                    div = cell.find_element(By.CSS_SELECTOR, "div.q-cell.cell--owner")
                    # Find the span element within the div
                    span = div.find_element(By.CSS_SELECTOR, "span.q-label")
                    # Get the text of the span element
                    span_text = str(span.get_attribute("innerHTML"))
                    row_data.append(span_text)
                else:
                    # If the td element doesn't have the class "q-column--owner", just get its text
                    cell_text = cell.text.strip()
                    row_data.append(cell_text)
            table_data.append(row_data)
        
        return fixDatesForList(table_data[1:])
    except Exception as e:
        print("Error:", e)

    finally:
        # Close the browser
        driver.quit()


def fixDatesForList(data: list) -> list:
    trade_entries = []

    for trade in data:
        # print("Single trade: ", trade)
        # politician_party, issuer_ticker, published, traded, filed_after, owner, buy_or_sell, size, price = map(lambda item: item.replace("\n", " "), trade)
        trade_components = [item.replace("\n", " ") for item in trade]
        # print("Trying to fix this stuff", trade_components)

        # Split Politician and Party
        politician_and_party = trade_components[0].split(" ")
        political_position = re.match(r"(Republican|Democrat)", politician_and_party.pop()).group()
        politician = " ".join(politician_and_party)

        # Split Issuer and Ticker
        issuer_ticker = trade_components[1].split(" ")
        ticker = issuer_ticker.pop()
        issuer = (" ").join(issuer_ticker)

        # Parse dates
        published = parseAndReplaceTodayDate(trade_components[2])
        traded = parseAndReplaceTodayDate(trade_components[3])
        filed_after = trade_components[4]

        owner = "N/A" if trade_components[5] == "" else trade_components[5]
        buy_or_sell = trade_components[6]
        size = trade_components[7]
        price = trade_components[8]
        
        # Create TradeEntry object
        trade_entry = TradeEntry(
            politician=politician,
            party=political_position,
            issuer=issuer,
            ticker=ticker,
            published=published,
            traded=traded,
            filed_after=filed_after,
            owner=owner,
            buy_or_sell=buy_or_sell,
            size=size,
            price=price
        )

        trade_entries.append(trade_entry)

    return trade_entries

def parseAndReplaceTodayDate(date_string: str) -> str:
    parts = date_string.split(" ")

    if len(parts) == 3:
        year, day, month = parts
        return f"{year} {month} {day}"
    else:
        day = parts[0]

    # Check if the date string contains "Today"
    if day.lower() == "today":
        today = date.today()
        return f"{today.year} {today.strftime("%b")} {today.day}"
    
    if day.lower() == "yesterday":
        yesterday = date.today() - timedelta(days = 1)
        return f"{yesterday.year} {yesterday.strftime("%b")} {yesterday.day}"

    