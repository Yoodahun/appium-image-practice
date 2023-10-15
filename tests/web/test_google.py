import pytest

@pytest.mark.incremental
@pytest.mark.usefixtures("print_for_testcase")
class TestGoogle:

    def test_google_home(self, print_for_testcase):
        self.driver.get("http://www.google.com")
        print(print_for_testcase)
        print(self.driver.current_url)
        assert "google" in self.driver.current_url

