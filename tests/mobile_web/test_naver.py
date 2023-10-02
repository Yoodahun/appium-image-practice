import pytest

from src.mobile_web.pages.home.naver_home_page import NaverHomePage
from src.mobile_web.pages.search_result.naver_search_result_page import NaverSearchResultPage


@pytest.mark.incremental
class TestNaver:
    def test_naver_home(self):
        self.naver_home_page = NaverHomePage(self.driver)
        assert self.naver_home_page.check_shortcut_area_is_visible()
        pytest.search_keyword = "이것은 셀레니움 테스트 코드 입니다."
        self.naver_home_page.search_text(pytest.search_keyword)

    def test_naver_search_result_page(self):
        self.naver_search_result_page = NaverSearchResultPage(self.driver)
        assert self.naver_search_result_page.check_query_area(pytest.search_keyword)
