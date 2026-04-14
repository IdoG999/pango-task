import pytest

from tests.data import test_data


@pytest.mark.high
@pytest.mark.critical
@pytest.mark.bug_02
@pytest.mark.tc_07
def test_slot_input_validation_current_behavior(authenticated_dashboard):
    dashboard = authenticated_dashboard
    dashboard.create_or_attempt_parking(
        plate=test_data.VALID_PLATE_A,
        slot=test_data.INVALID_SLOT_VALUE,
    )
    # Current product behavior (known defect): invalid slot value is accepted.
    assert not dashboard.has_slot_validation_error()


@pytest.mark.high
@pytest.mark.critical
@pytest.mark.bug_03
@pytest.mark.tc_06
def test_duplicate_slot_assignment_current_behavior(authenticated_dashboard):
    dashboard = authenticated_dashboard
    target_slot = dashboard.first_available_slot()
    dashboard.create_or_attempt_parking(plate=test_data.VALID_PLATE_A, slot=target_slot)
    assert dashboard.is_plate_visible_in_active_table(test_data.VALID_PLATE_A)

    dashboard.create_or_attempt_parking(plate=test_data.VALID_PLATE_B, slot=target_slot)
    # Current product behavior (known defect): second vehicle can still be added.
    assert dashboard.is_plate_visible_in_active_table(test_data.VALID_PLATE_B)


@pytest.mark.high
@pytest.mark.bug_01
@pytest.mark.tc_09
def test_vehicle_type_single_option_current_behavior(authenticated_dashboard):
    dashboard = authenticated_dashboard
    # Current product behavior (known defect): only one vehicle type exists.
    assert dashboard.vehicle_type_option_count() == 1
