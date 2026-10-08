import allure
from pages.login_page import ERR_INVALID_CREDENTIALS, UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 20,
    "ID": "TC20",
    "Description": "Kiểm tra đăng nhập bằng SQL Injection",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Nhập username.",
        "Nhập password.",
        "Click nút Đăng nhập.",
    ],
    "Giá trị": {
        "Username": "' OR '1'='1",
        "Password": "123456",
    },
    "Expected Output": "Đăng nhập thất bại. Không cho phép bỏ qua xác thực hoặc tiết lộ thông tin cơ sở dữ liệu.",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Kiểm tra biên & Bảo mật hệ thống")
@allure.title("TC20: Kiểm tra đăng nhập bằng SQL Injection")
@allure.severity(allure.severity_level.BLOCKER)
def test_tc20_sql_injection_login(driver):
    """TC20: Kiểm tra đăng nhập bằng SQL Injection."""
    data = attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    page.enter_username(data["Username"])
    page.enter_password(data["Password"])
    page.click_login()

    error_text = page.get_error_text()
    assert error_text == ERR_INVALID_CREDENTIALS
    assert page.is_on_login_page()
    page_source_lower = driver.page_source.lower()
    assert "sql" not in page_source_lower and "syntax error" not in page_source_lower
