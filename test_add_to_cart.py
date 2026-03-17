from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://adnabu-store-assignment1.myshopify.com"
PASSWORD = "AdNabuQA"

def setup_driver():
    service = Service("./chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)
    return driver, wait

def login(driver, wait):
    driver.get(URL)
    password = wait.until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )
    password.send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

def search_product(driver, wait, product_name):
    search_icon = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'summary[aria-label="Search"]'))
    )
    search_icon.click()
    search_box = wait.until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys(product_name)
    search_box.submit()

    wait.until(EC.url_contains("/search"))

def select_first_product(driver, wait):
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".card-wrapper"))
    )
    products = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href*="/products/"]'))
    )
    driver.execute_script("arguments[0].click();", products[0])

def add_to_cart(driver, wait):
    add_button = wait.until(
        EC.element_to_be_clickable((By.NAME, "add"))
    )
    add_button.click()

def verify_added_to_cart(driver, wait, expected_count="1"):
    cart = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-count-bubble"))
    )
    wait.until(lambda d: expected_count in cart.text)


def driver_quit(driver):
    driver.quit()

def test_add_to_cart():
    driver, wait = setup_driver()

    login(driver, wait)
    search_product(driver, wait, "Snowboard")
    select_first_product(driver, wait)
    add_to_cart(driver, wait)
    verify_added_to_cart(driver, wait, "1")
    print("Test Passed: Product added to the cart")

    driver_quit(driver)


if __name__ == "__main__":
    test_add_to_cart()
