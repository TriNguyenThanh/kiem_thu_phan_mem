import allure
from pages.login_page import ERR_INVALID_CREDENTIALS, UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 11,
    "ID": "TC11",
    "Description": "Mật khẩu phân biệt chữ hoa và chữ thường",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Nhập username.",
        "Nhập password đã thay đổi chữ hoa/chữ thường so với mật khẩu đúng.",
        "Click nút Đăng nhập.",
    ],
    "Giá trị": {
        "Username": "huongnt",
        "Password": "123456@utc (đổi chữ hoa/chữ thường)",
    },
    "Expected Output": "Hiển thị \"Tài khoản không đúng\" nếu mật khẩu không khớp chính xác.",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Kiểm tra xác thực tài khoản không hợp lệ")
@allure.title("TC11: Mật khẩu phân biệt chữ hoa và chữ thường")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc11_password_case_sensitivity(driver):
    """TC11: Mật khẩu phân biệt chữ hoa và chữ thường."""
    data = attach_test_case(TEST_CASE)
    valid_password = "123456@utc"
    case_changed_password = valid_password.swapcase()

    page = UTCLoginPage(driver).open()
    page.enter_username(data["Username"])
    page.enter_password(case_changed_password)
    page.click_login()

    assert page.get_error_text() == ERR_INVALID_CREDENTIALS
    assert page.is_on_login_page()
