import re

import pytest

from conftest import login


def _go_to_dashboard(page):
    if page.locator('a:has-text("Dashboard")').count() > 0:
        page.locator('a:has-text("Dashboard")').first.click()
    page.wait_for_timeout(500)


def _fill_and_submit(page, plate: str, slot: str):
    page.locator('input[name="car_plate"]').fill(plate)
    page.locator('input[name="slot"]').fill(slot)
    page.locator('input[name="submit"]').click()
    page.wait_for_timeout(800)


@pytest.mark.xfail(
    reason="Known bug from Part 1: invalid slot values are accepted.",
    strict=False,
)
def test_slot_input_validation_expected_rejection(page):
    login(page)
    _go_to_dashboard(page)

    _fill_and_submit(page, plate="24681357", slot="ABC@@")

    # Product expectation: invalid slot should be rejected with slot-specific validation.
    assert page.get_by_text(
        re.compile(r"(invalid slot|slot.*invalid|slot.*number)", re.IGNORECASE)
    ).count() > 0


@pytest.mark.xfail(
    reason="Known bug from Part 1: duplicate slot assignment is not blocked.",
    strict=False,
)
def test_prevent_duplicate_slot_assignment_expected_block(page):
    login(page)
    _go_to_dashboard(page)

    target_slot = "77"
    if page.locator("tbody tr td:nth-child(2)").count() > 0:
        text = page.locator("tbody tr td:nth-child(2)").first.inner_text().strip()
        if text:
            target_slot = text

    _fill_and_submit(page, plate="24681357", slot=target_slot)
    _fill_and_submit(page, plate="97531864", slot=target_slot)

    # Product expectation: second assignment to same slot should be blocked.
    assert page.get_by_text(
        re.compile(r"(occupied|already taken|slot.*in use|duplicate)", re.IGNORECASE)
    ).count() > 0
