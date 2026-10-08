import allure
from pages.login_page import ERR_EMPTY_PASSWORD, UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 2,
    "ID": "TC2",
    "Description": "Để trống mật khẩu",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Nhập dữ liệu vào ô username.",
        "Để trống ô password.",
        "Click nút Đăng nhập.",
    ],
    "Giá trị": {
        "Username": "huongnt",
        "Password": "",
    },
    "Expected Output": "Hiển thị thông báo \"Bạn chưa nhập mật khẩu\".",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Kiểm tra ràng buộc dữ liệu đầu vào (Validation)")
@allure.title("TC2: Để trống mật khẩu")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc02_empty_password(driver):
    """TC2: Để trống mật khẩu."""
    data = attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    page.enter_username(data["Username"])
    page.enter_password(data["Password"])
    page.click_login()

    assert page.get_error_text() == ERR_EMPTY_PASSWORD
    assert page.is_on_login_page()
