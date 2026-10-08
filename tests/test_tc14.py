import allure
from pages.login_page import ERR_INVALID_CREDENTIALS, UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 14,
    "ID": "TC14",
    "Description": "Tên đăng nhập không tồn tại",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Nhập username.",
        "Nhập password.",
        "Click nút Đăng nhập.",
    ],
    "Giá trị": {
        "Username": "nonexistent_user_12345",
        "Password": "123456",
    },
    "Expected Output": "Hiển thị thông báo \"Tài khoản không đúng\".",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Kiểm tra xác thực tài khoản không hợp lệ")
@allure.title("TC14: Tên đăng nhập không tồn tại")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc14_nonexistent_username(driver):
    """TC14: Tên đăng nhập không tồn tại."""
    data = attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    page.enter_username(data["Username"])
    page.enter_password(data["Password"])
    page.click_login()

    assert page.get_error_text() == ERR_INVALID_CREDENTIALS
    assert page.is_on_login_page()
