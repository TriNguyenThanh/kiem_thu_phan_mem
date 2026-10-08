import allure
from pages.login_page import UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 12,
    "ID": "TC12",
    "Description": "Đăng nhập bằng phím Enter",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Nhập username.",
        "Nhập password.",
        "Nhấn phím Enter.",
    ],
    "Giá trị": {
        "Username": "huongnt",
        "Password": "123456@utc",
        "Phím": "Enter",
    },
    "Expected Output": "Đăng nhập thành công và chuyển đến trang chủ.",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Luồng đăng nhập thành công & Quản lý phiên")
@allure.title("TC12: Đăng nhập bằng phím Enter")
@allure.severity(allure.severity_level.NORMAL)
def test_tc12_login_with_enter_key(driver):
    """TC12: Đăng nhập bằng phím Enter."""
    data = attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    page.enter_username(data["Username"])
    page.enter_password(data["Password"])
    page.submit_with_enter()

    page.assert_logged_in_successfully()
