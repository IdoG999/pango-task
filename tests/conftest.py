import os
from typing import Iterable

import pytest
from playwright.sync_api import Page, sync_playwright


BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")
APP_USERNAME = os.getenv("APP_USERNAME", "admin")
APP_PASSWORD = os.getenv("APP_PASSWORD", "password")


def _first_visible_locator(page: Page, selectors: Iterable[str]):
    for selector in selectors:
        locator = page.locator(selector).first
        if locator.count() > 0:
            return locator
    raise AssertionError(f"None of selectors matched: {selectors}")


def fill_with_fallback(page: Page, selectors: Iterable[str], value: str) -> None:
    locator = _first_visible_locator(page, selectors)
    locator.fill(value)


def click_with_fallback(page: Page, selectors: Iterable[str]) -> None:
    locator = _first_visible_locator(page, selectors)
    locator.click()


def login(page: Page, username: str = APP_USERNAME, password: str = APP_PASSWORD) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    fill_with_fallback(
        page,
        [
            'input[name="username"]',
            'input[name="email"]',
            'input[type="email"]',
            'input[placeholder*="user" i]',
            'input[placeholder*="email" i]',
        ],
        username,
    )
    fill_with_fallback(
        page,
        [
            'input[name="password"]',
            'input[type="password"]',
            'input[placeholder*="password" i]',
        ],
        password,
    )
    click_with_fallback(
        page,
        [
            'button:has-text("Sign In")',
            'button:has-text("Login")',
            'button[type="submit"]',
        ],
    )

    page.wait_for_timeout(1000)


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
