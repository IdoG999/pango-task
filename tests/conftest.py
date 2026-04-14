import os

import pytest
from playwright.sync_api import sync_playwright

from tests.data import test_data
from tests.pages.dashboard_page import DashboardPage
from tests.pages.login_page import LoginPage


BASE_URL = os.getenv("BASE_URL", test_data.BASE_URL)
APP_USERNAME = os.getenv("APP_USERNAME", test_data.APP_USERNAME)
APP_PASSWORD = os.getenv("APP_PASSWORD", test_data.APP_PASSWORD)
HEADLESS = os.getenv("HEADLESS", "true").lower() != "false"


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture()
def login_page(page):
    return LoginPage(page)


@pytest.fixture()
def dashboard_page(page):
    return DashboardPage(page)


@pytest.fixture()
def authenticated_dashboard(login_page, dashboard_page):
    login_page.open(BASE_URL)
    login_page.login(APP_USERNAME, APP_PASSWORD)
    dashboard_page.open()
    return dashboard_page
