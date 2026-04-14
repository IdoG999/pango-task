from __future__ import annotations

from typing import Iterable

from playwright.sync_api import Locator, Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def first_match(self, selectors: Iterable[str]) -> Locator:
        for selector in selectors:
            locator = self.page.locator(selector).first
            if locator.count() > 0:
                return locator
        raise AssertionError(f"None of selectors matched: {list(selectors)}")

    def fill_with_fallback(self, selectors: Iterable[str], value: str) -> None:
        self.first_match(selectors).fill(value)

    def click_with_fallback(self, selectors: Iterable[str]) -> None:
        self.first_match(selectors).click()
