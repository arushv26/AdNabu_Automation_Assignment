# Automation Assignment – Shopify Store
## Overview

This project contains a Selenium automation script that tests the functionality of searching for a product and successfully adding it to the cart on the Shopify store.

## Tech Stack

Python

Selenium

Pytest

## Test Scenario

Search for a product and add it to the cart successfully.

## Test Steps

1. Open the store URL

2. Enter the store password

3. Search for a product

4. Open the first product from the search results

5. Click Add to Cart

6. Verify the cart count updates

## Setup Instructions
1. Clone the Repository
git clone <[your-repository-link](https://github.com/arushv26/AdNabu_Automation_Assignment)>
2. cd AdNabu_Automation_Assignment
3. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
5. Download ChromeDriver

Download the ChromeDriver version compatible with your Chrome browser and place it in the project directory.

Run the Test
test_add_to_cart.py
