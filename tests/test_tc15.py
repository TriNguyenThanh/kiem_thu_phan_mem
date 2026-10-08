import allure
from pages.login_page import ERR_INVALID_CREDENTIALS, UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 15,
    "ID": "TC15",
    "Description": "Nhập mật khẩu quá dài",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Nhập username.",
        "Nhập password.",
        "Click nút Đăng nhập.",
    ],
    "Giá trị": {
        "Username": "huongnt",
        "Password": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    },
    "Expected Output": "Đăng nhập thất bại. Hệ thống không bị treo hoặc phát sinh lỗi máy chủ.",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Kiểm tra biên & Bảo mật hệ thống")
@allure.title("TC15: Nhập mật khẩu quá dài")
@allure.severity(allure.severity_level.NORMAL)
def test_tc15_excessively_long_password(driver):
    """TC15: Nhập mật khẩu quá dài."""
    data = attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    page.enter_username(data["Username"])
    page.enter_password(data["Password"])
    page.click_login()

    assert page.get_error_text() == ERR_INVALID_CREDENTIALS
    assert page.is_on_login_page()
