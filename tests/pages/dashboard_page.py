from __future__ import annotations

import re

from tests.pages.base_page import BasePage


class DashboardPage(BasePage):
    DASHBOARD_TAB = ['a:has-text("Dashboard")', '[role="tab"]:has-text("Dashboard")']
    SLOT_INPUT = ['input[name="slot"]', 'input[name="parkingSlot"]']
    PLATE_INPUT = ['input[name="car_plate"]', 'input[name="plate"]', 'input[name="licensePlate"]']
    SUBMIT_INPUT = ['input[name="submit"]', 'button[type="submit"]']
    VEHICLE_TYPE_SELECT = [
        'select[name="vehicle_type"]',
        'select[name="vehicleType"]',
        'select[id*="vehicle" i]',
    ]

    def open(self) -> None:
        if self.page.locator(self.DASHBOARD_TAB[0]).count() > 0:
            self.click_with_fallback(self.DASHBOARD_TAB)
        self.page.wait_for_timeout(500)

    def create_or_attempt_parking(self, plate: str, slot: str) -> None:
        self.fill_with_fallback(self.PLATE_INPUT, plate)
        self.fill_with_fallback(self.SLOT_INPUT, slot)
        self.click_with_fallback(self.SUBMIT_INPUT)
        self.page.wait_for_timeout(800)

    def first_existing_slot_or_default(self, default_slot: str = "77") -> str:
        if self.page.locator("tbody tr td:nth-child(2)").count() > 0:
            text = self.page.locator("tbody tr td:nth-child(2)").first.inner_text().strip()
            if text:
                return text
        return default_slot

    def first_available_slot(self, start: int = 50, end: int = 300) -> str:
        taken_slots = set()
        slot_cells = self.page.locator("tbody tr td:nth-child(2)")
        for i in range(slot_cells.count()):
            raw = slot_cells.nth(i).inner_text().strip()
            if raw.isdigit():
                taken_slots.add(int(raw))

        for candidate in range(start, end + 1):
            if candidate not in taken_slots:
                return str(candidate)
        return str(end + 1)

    def is_plate_visible_in_active_table(self, plate: str) -> bool:
        return self.page.locator(f"tbody tr td:text-is('{plate}')").count() > 0

    def has_slot_validation_error(self) -> bool:
        return (
            self.page.get_by_text(
                re.compile(r"(invalid slot|slot.*invalid|slot.*number)", re.IGNORECASE)
            ).count()
            > 0
        )

    def has_duplicate_slot_blocking_error(self) -> bool:
        return (
            self.page.get_by_text(
                re.compile(r"(occupied|already taken|slot.*in use|duplicate)", re.IGNORECASE)
            ).count()
            > 0
        )

    def vehicle_type_option_count(self) -> int:
        selector = self.first_match(self.VEHICLE_TYPE_SELECT)
        return selector.locator("option").count()
