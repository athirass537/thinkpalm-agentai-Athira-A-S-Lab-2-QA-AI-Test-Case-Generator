
**Feature Description:**

1. Open https://www.amazon.in/.
2. Search for "Dell Laptop".
3. Scroll through the search results and find the Dell Laptop priced at ₹49,490.
4. Highlight the product.
5. Click "Add to Cart".
6. Click "Go to Cart".
7. Verify the product is present in the cart.
8. Click "Proceed to Buy".
9. Print "Amazon Purchase Success" in the console.
10. Generate an HTML report showing:
Test Case Name
Status (PASS/FAIL)
Execution Time
Result Summary

**PROMPT:**

Use Selenium WebDriver with Python.
Use explicit waits (WebDriverWait).
Handle exceptions properly.
Use dynamic XPath locators where possible.
Include comments explaining each step.
Generate a complete executable Python script.
Close the browser after execution.
<img width="385" height="521" alt="image" src="https://github.com/user-attachments/assets/faf36740-62e1-411f-be93-ee944dbe2382" />

**RUN COMMANDS**

PS C:\Users\athira.as.DC\PycharmProjects\PythonProject7> python amazon.py

**TESTCASES:**

Test Case ID	Test Scenario	Steps	Expected Result
TC_001	Verify user can login to Amazon website	1. URL available	Ensure User can open Amazon URL
TC_002	Verify user can search for Dell Laptop	"Open Amazon India.
Enter ""Dell Laptop"" in the search box.
Press Enter"	Search results for Dell Laptop are displayed
TC_003	Verify Dell Laptop priced ₹49,490 is displayed	"Search for Dell Laptop.
Scroll through search results."	Laptop priced ₹49,490 is displayed in the search results.
TC_004	Verify user can add Dell Laptop to cart	"Locate Dell Laptop priced ₹49,490.
Click Add to Cart."	Product is successfully added to the cart
TC_005	Verify user can navigate to cart	Click Go to Cart.	Cart page is displayed with the selected Dell Laptop.
TC_006	Verify user can proceed to buy	Click Proceed to Buy.	User is redirected to the checkout/sign-in page.
TC_007	Verify successful execution of Amazon purchase flow	"Search Dell Laptop.
Add laptop priced ₹49,490 to cart.
Go to Cart.
Click Proceed to Buy."	Purchase flow completes successfully and status is displayed as PASS in the HTML report.
<img width="667" height="441" alt="image" src="https://github.com/user-attachments/assets/33d58dcb-7665-44fe-8fe6-f80ceb5a0aae" />


