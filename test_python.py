import pytest
from dotenv import load_dotenv
import os
from playwright.sync_api import expect

load_dotenv(dotenv_path=".env", override=True)
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

assert USERNAME and PASSWORD, "Doplňte prosim .env"

# Pomocná funkce pro odmítnutí cookies
def reject_cookies(page):
    page.goto("https://www.engeto.cz")

    page.locator("#cookiescript_reject").click()

    page.locator("#cookiescript_injected").wait_for(state="hidden")

# Ověření, že cookie banner zmizel po odmítnutí cookies
def test_cookie_refuse_engeto(page):
    reject_cookies(page)

    cookie_banner = page.locator("#cookiescript_injected")

    expect(cookie_banner).to_be_hidden()


# Ověření navigace na stránku kurzu a dostupnosti rozvrhu termínů.
def test_testing_course(page):
    reject_cookies(page)

    course_button = page.get_by_role("link", name="Testing Akademie")
    course_button.click()

    course_term = page.get_by_role("link", name="Zobrazit termíny kurzu")
    course_term.click()

    title_term = page.get_by_role("heading", name="Termíny", exact=True)

    expect(title_term).to_be_visible()


# Ověření fungujícího přihlášení a přístupu k záznamu lekcí.
def test_testing_course_url(page):
    reject_cookies(page)

    page.get_by_role("link", name="Výukový portál").click()

    page.get_by_role("button", name="Přihlásit se pomoci e-mailu a hesla").click()

    username_input = page.locator("#username")
    username_input.fill(USERNAME)

    password_input = page.locator("#password")
    password_input.fill(PASSWORD)


    page.get_by_role("button", name="Pokračovat").click()

    page.wait_for_url("**/study/**")

    course_records_button = page.get_by_role("button", name="Záznamy lekcí")

    expect(course_records_button).to_be_visible()