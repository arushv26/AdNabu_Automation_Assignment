from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://adnabu-store-assignment1.myshopify.com"
PASSWORD = "AdNabuQA"


def test_search_and_add_to_cart():

    service = Service("./chromedriver")
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 15)

    driver.get(URL)
    driver.maximize_window()

    password = wait.until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )
    password.send_keys(PASSWORD)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    search_icon = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'summary[aria-label="Search"]'))
    )
    search_icon.click()

    search_box = wait.until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Snowboard")
    search_box.submit()

    wait.until(EC.url_contains("/search"))

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".card-wrapper"))
    )

    products = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href*="/products/"]'))
    )

    driver.execute_script("arguments[0].click();", products[0])

    add_button = wait.until(
        EC.element_to_be_clickable((By.NAME, "add"))
    )
    add_button.click()

    cart = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-count-bubble"))
    )

    wait.until(lambda d: "1" in cart.text)

    print("Test Passed: Product successfully added to cart")

    driver.implicitly_wait(80)

    driver.quit()


if __name__ == "__main__":
    test_search_and_add_to_cart()