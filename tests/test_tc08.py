import allure
from pages.login_page import ERR_INVALID_CREDENTIALS, UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 8,
    "ID": "TC8",
    "Description": "Sai cả tên đăng nhập và mật khẩu",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Nhập username.",
        "Nhập password.",
        "Click nút Đăng nhập.",
    ],
    "Giá trị": {
        "Username": "user_invalid",
        "Password": "123456@utc",
    },
    "Expected Output": "Hiển thị thông báo \"Tài khoản không đúng\".",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Kiểm tra xác thực tài khoản không hợp lệ")
@allure.title("TC8: Sai cả tên đăng nhập và mật khẩu")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc08_invalid_both_username_and_password(driver):
    """TC8: Sai cả tên đăng nhập và mật khẩu."""
    data = attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    page.enter_username(data["Username"])
    page.enter_password(data["Password"])
    page.click_login()

    assert page.get_error_text() == ERR_INVALID_CREDENTIALS
    assert page.is_on_login_page()
