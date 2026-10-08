import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 17,
    "ID": "TC17",
    "Description": "Kiểm tra đăng nhập bằng e-mail UTC",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Click vào \"Đăng nhập bằng e-mail UTC\".",
        "Quan sát kết quả.",
    ],
    "Giá trị": {
        "Phương thức": "E-mail UTC",
    },
    "Expected Output": "Chuyển đến quy trình xác thực bằng e-mail UTC.",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Liên kết phụ trợ & Đăng nhập thay thế")
@allure.title("TC17: Kiểm tra đăng nhập bằng e-mail UTC")
@allure.severity(allure.severity_level.NORMAL)
def test_tc17_login_with_utc_email_oauth(driver):
    """TC17: Kiểm tra đăng nhập bằng e-mail UTC."""
    attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    oauth_btn = driver.find_element(*UTCLoginPage.GOOGLE_OAUTH_LINK)
    href = oauth_btn.get_attribute("href")
    assert "accounts.google.com" in href

    page.click_google_email_login()

    WebDriverWait(driver, 10).until(EC.url_contains("accounts.google.com"))
    assert "accounts.google.com" in driver.current_url
