import allure
from pages.login_page import UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 13,
    "ID": "TC13",
    "Description": "Kiểm tra chức năng che mật khẩu",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Click vào ô password.",
        "Nhập password.",
        "Quan sát nội dung ô password.",
    ],
    "Giá trị": {
        "Password": "123456@utc",
    },
    "Expected Output": "Mật khẩu được che bằng các ký tự thay thế, không hiển thị văn bản gốc.",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Kiểm tra giao diện & Bảo mật hiển thị")
@allure.title("TC13: Kiểm tra chức năng che mật khẩu")
@allure.severity(allure.severity_level.NORMAL)
def test_tc13_password_masking(driver):
    """TC13: Kiểm tra chức năng che mật khẩu."""
    data = attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    pwd_input = page.enter_password(data["Password"])

    assert pwd_input.get_attribute("type") == "password"
    assert pwd_input.get_attribute("value") == data["Password"]
