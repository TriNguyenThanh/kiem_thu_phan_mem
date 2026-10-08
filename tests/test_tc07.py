import allure
from pages.login_page import ERR_EMPTY_USERNAME, UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 7,
    "ID": "TC7",
    "Description": "Để trống cả tên đăng nhập và mật khẩu",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Không nhập thông tin vào hai ô.",
        "Click nút Đăng nhập.",
    ],
    "Giá trị": {
        "Username": "",
        "Password": "",
    },
    "Expected Output": "Hiển thị thông báo yêu cầu nhập thông tin đăng nhập; không cho phép đăng nhập.",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Kiểm tra ràng buộc dữ liệu đầu vào (Validation)")
@allure.title("TC7: Để trống cả tên đăng nhập và mật khẩu")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc07_empty_both_username_and_password(driver):
    """TC7: Để trống cả tên đăng nhập và mật khẩu."""
    data = attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    page.enter_username(data["Username"])
    page.enter_password(data["Password"])
    page.click_login()

    assert page.get_error_text() == ERR_EMPTY_USERNAME
    assert page.is_on_login_page()
