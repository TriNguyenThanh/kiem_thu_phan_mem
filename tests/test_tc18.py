import allure
from pages.login_page import UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 18,
    "ID": "TC18",
    "Description": "Làm mới trang sau khi đăng nhập",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Nhập username.",
        "Nhập password.",
        "Click nút Đăng nhập.",
        "Nhấn F5 tại trang chủ.",
    ],
    "Giá trị": {
        "Username": "huongnt",
        "Password": "123456@utc",
        "Phím": "F5",
    },
    "Expected Output": "Trang được làm mới và vẫn duy trì phiên đăng nhập còn hiệu lực.",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Luồng đăng nhập thành công & Quản lý phiên")
@allure.title("TC18: Làm mới trang sau khi đăng nhập")
@allure.severity(allure.severity_level.NORMAL)
def test_tc18_refresh_page_after_login(driver):
    """TC18: Làm mới trang sau khi đăng nhập."""
    data = attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    page.enter_username(data["Username"])
    page.enter_password(data["Password"])
    page.click_login()

    page.assert_logged_in_successfully()

    # Làm mới trang (tương đương nhấn F5)
    driver.refresh()
    assert not page.is_on_login_page(), "Phiên đăng nhập bị mất sau khi làm mới trang (F5)"
