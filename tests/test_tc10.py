import allure
from pages.login_page import (
    ERR_EMPTY_PASSWORD,
    ERR_INVALID_CREDENTIALS,
    UTCLoginPage,
    attach_test_case,
)


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 10,
    "ID": "TC10",
    "Description": "Mật khẩu chỉ chứa khoảng trắng",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Nhập username.",
        "Nhập password.",
        "Click nút Đăng nhập.",
    ],
    "Giá trị": {
        "Username": "huongnt",
        "Password": "   ",
    },
    "Expected Output": "Không đăng nhập thành công. Hiển thị thông báo lỗi phù hợp.",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Kiểm tra ràng buộc dữ liệu đầu vào (Validation)")
@allure.title("TC10: Mật khẩu chỉ chứa khoảng trắng")
@allure.severity(allure.severity_level.NORMAL)
def test_tc10_whitespace_only_password(driver):
    """TC10: Mật khẩu chỉ chứa khoảng trắng."""
    data = attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    page.enter_username(data["Username"])
    page.enter_password(data["Password"])
    page.click_login()

    assert page.get_error_text() in (ERR_INVALID_CREDENTIALS, ERR_EMPTY_PASSWORD)
    assert page.is_on_login_page()
