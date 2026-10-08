import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 16,
    "ID": "TC16",
    "Description": "Kiểm tra chức năng quên mật khẩu",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Click vào liên kết \"Bạn quên mật khẩu đăng nhập?\".",
        "Quan sát kết quả.",
    ],
    "Giá trị": {
        "Liên kết": "Bạn quên mật khẩu đăng nhập?",
    },
    "Expected Output": "Chuyển đến giao diện hoặc hướng dẫn khôi phục mật khẩu.",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Liên kết phụ trợ & Đăng nhập thay thế")
@allure.title("TC16: Kiểm tra chức năng quên mật khẩu")
@allure.severity(allure.severity_level.NORMAL)
def test_tc16_forgot_password_link(driver):
    """TC16: Kiểm tra chức năng quên mật khẩu."""
    attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    page.click_forgot_password()

    WebDriverWait(driver, 10).until(EC.url_contains("/Login/GetPass"))
    assert "/Login/GetPass" in driver.current_url
    assert "Lấy lại mật khẩu" in driver.title
    assert driver.find_element(By.NAME, "email").is_displayed()
    assert driver.find_element(By.NAME, "captcha").is_displayed()
