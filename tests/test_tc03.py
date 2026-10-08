import allure
from pages.login_page import ERR_INVALID_CREDENTIALS, UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 3,
    "ID": "TC3",
    "Description": "Đúng tên đăng nhập, sai mật khẩu",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Nhập username.",
        "Nhập password.",
        "Click nút Đăng nhập.",
    ],
    "Giá trị": {
        "Username": "huongnt",
        "Password": "123456@utc",
    },
    "Expected Output": "Hiển thị thông báo \"Tài khoản không đúng\".",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Kiểm tra xác thực tài khoản không hợp lệ")
@allure.title("TC3: Đúng tên đăng nhập, sai mật khẩu")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc03_valid_username_invalid_password(driver):
    """TC3: Đúng tên đăng nhập, sai mật khẩu."""
    data = attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    page.enter_username(data["Username"])
    page.enter_password(data["Password"])
    page.click_login()

    assert page.get_error_text() == ERR_INVALID_CREDENTIALS
    assert page.is_on_login_page()
