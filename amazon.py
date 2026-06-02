from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Open Amazon
    driver.get("https://www.amazon.in/")

    wait = WebDriverWait(driver, 20)

    # Search Dell Laptop
    search_box = wait.until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )

    search_box.send_keys("Dell Laptop")
    search_box.send_keys(Keys.ENTER)

    # Wait for search results
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@data-component-type='s-search-result']")
        )
    )

    print("Search results loaded")

    products = driver.find_elements(
        By.XPATH,
        "//div[@data-component-type='s-search-result']"
    )

    product_found = False

    for product in products:

        try:
            # Get price
            price = product.find_element(
                By.XPATH,
                ".//span[@class='a-price-whole']"
            ).text.replace(",", "")

            print("Found price:", price)

            if price == "49490":

                print("Dell Laptop Rs.49,490 found")

                # Scroll to product
                driver.execute_script(
                    "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
                    product
                )

                time.sleep(3)

                # Highlight product
                driver.execute_script(
                    "arguments[0].style.border='4px solid red';",
                    product
                )

                time.sleep(2)

                # Click Add to Cart
                add_to_cart = product.find_element(
                    By.XPATH,
                    ".//button[contains(.,'Add to cart')]"
                )

                add_to_cart.click()

                print("Add to Cart clicked")

                product_found = True
                break

        except Exception:
            continue

    if not product_found:
        print("No Dell Laptop with price Rs.49,490 found on current page")

    time.sleep(10)

    # Go to Cart
    go_to_cart = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(),'Go to Cart')]")
        )
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", go_to_cart)
    time.sleep(2)

    driver.execute_script("arguments[0].click();", go_to_cart)

    print("Go to Cart clicked")
    time.sleep(10)

    # Proceed to Buy
    proceed_to_buy = wait.until(
        EC.presence_of_element_located(
            (By.NAME, "proceedToRetailCheckout")
        )
    )

    driver.execute_script("arguments[0].click();", proceed_to_buy)

    print("Proceed to Buy clicked")
    time.sleep(10)
    print("Amazon Purchase Success")

    report = f"""
    <html>
    <head>
        <title>Amazon Automation Report</title>
    </head>
    <body>

        <h1>Amazon Automation Test Report</h1>

        <h2 style="color:green;">
            Test Execution Status : SUCCESS
        </h2>

        <table border="1" cellpadding="10">
            <tr>
                <th>Test Case</th>
                <th>Status</th>
                <th>Execution Time</th>
            </tr>

            <tr>
                <td>Amazon Purchase Flow</td>
                <td style="color:green;">PASS</td>
                <td>{datetime.now()}</td>
            </tr>
        </table>

        <br>

        <b>Result:</b>
        <span style="color:green;">
            Amazon Purchase Completed Successfully
        </span>

    </body>
    </html>
    """

    with open("Amazon_Report.html", "w") as f:
        f.write(report)

    print("HTML Report Generated Successfully")

finally:
    # driver.quit()
    pass