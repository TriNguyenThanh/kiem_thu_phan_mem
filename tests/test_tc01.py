import allure
from pages.login_page import ERR_EMPTY_USERNAME, UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 1,
    "ID": "TC1",
    "Description": "Để trống tên đăng nhập",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Click vào ô username và để trống.",
        "Nhập dữ liệu vào ô password.",
        "Click nút Đăng nhập.",
    ],
    "Giá trị": {
        "Username": "",
        "Password": "123456@utc",
    },
    "Expected Output": "Hiển thị thông báo \"Bạn chưa nhập tên đăng nhập\".",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Kiểm tra ràng buộc dữ liệu đầu vào (Validation)")
@allure.title("TC1: Để trống tên đăng nhập")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc01_empty_username(driver):
    """TC1: Để trống tên đăng nhập."""
    data = attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    page.enter_username(data["Username"])
    page.enter_password(data["Password"])
    page.click_login()

    assert page.get_error_text() == ERR_EMPTY_USERNAME
    assert page.is_on_login_page()
