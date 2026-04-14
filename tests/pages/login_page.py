from __future__ import annotations

from tests.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_SELECTORS = [
        'input[name="username"]',
        'input[name="email"]',
        'input[type="email"]',
        'input[placeholder*="user" i]',
        'input[placeholder*="email" i]',
    ]
    PASSWORD_SELECTORS = [
        'input[name="password"]',
        'input[type="password"]',
        'input[placeholder*="password" i]',
    ]
    SUBMIT_SELECTORS = [
        'button:has-text("Sign In")',
        'button:has-text("Login")',
        'button[type="submit"]',
    ]
    LOGIN_FORM_HINTS = ['input[name="username"]', 'input[name="password"]']

    def open(self, base_url: str) -> None:
        self.page.goto(base_url, wait_until="domcontentloaded")

    def login(self, username: str, password: str) -> None:
        self.fill_with_fallback(self.USERNAME_SELECTORS, username)
        self.fill_with_fallback(self.PASSWORD_SELECTORS, password)
        self.click_with_fallback(self.SUBMIT_SELECTORS)
        self.page.wait_for_timeout(800)

    def is_login_form_visible(self) -> bool:
        return all(self.page.locator(sel).count() > 0 for sel in self.LOGIN_FORM_HINTS)

    def has_auth_error(self) -> bool:
        return (
            self.page.get_by_text("Invalid", exact=False).count() > 0
            or self.page.get_by_text("incorrect", exact=False).count() > 0
            or self.page.get_by_text("failed", exact=False).count() > 0
        )

    def is_user_logged_in(self) -> bool:
        return (
            self.page.locator('a:has-text("Dashboard")').count() > 0
            and self.page.locator('a:has-text("Logout")').count() > 0
        )
