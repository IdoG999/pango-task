import pytest

from tests.data import test_data


@pytest.mark.high
@pytest.mark.critical
@pytest.mark.tc_01
def test_login_with_valid_credentials(login_page):
    login_page.open(test_data.BASE_URL)
    login_page.login(test_data.APP_USERNAME, test_data.APP_PASSWORD)
    assert login_page.is_user_logged_in()


def test_login_with_invalid_credentials(login_page):
    login_page.open(test_data.BASE_URL)
    login_page.login(test_data.APP_USERNAME, "wrong")
    assert login_page.is_login_form_visible()
