import allure
from pages.login_page import UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 6,
    "ID": "TC6",
    "Description": "Đăng nhập thành công và không chọn \"Giữ tôi luôn đăng nhập\"",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Nhập username.",
        "Nhập password.",
        "Không tích chọn \"Giữ tôi luôn đăng nhập\".",
        "Click nút Đăng nhập.",
        "Tắt trình duyệt và mở lại.",
        "Truy cập lại website.",
    ],
    "Giá trị": {
        "Username": "huongnt",
        "Password": "123456@utc",
        "Giữ tôi luôn đăng nhập": False,
    },
    "Expected Output": "Đăng nhập thành công, chuyển đến trang chủ. Sau khi mở lại trình duyệt, hiển thị trang đăng nhập theo yêu cầu của mẫu.",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Luồng đăng nhập thành công & Quản lý phiên")
@allure.title("TC6: Đăng nhập thành công và không chọn 'Giữ tôi luôn đăng nhập'")
@allure.severity(allure.severity_level.BLOCKER)
def test_tc06_login_success_without_remember_me(driver):
    """TC6: Đăng nhập thành công và không chọn 'Giữ tôi luôn đăng nhập'."""
    data = attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    page.enter_username(data["Username"])
    page.enter_password(data["Password"])
    page.set_remember_me(data["Giữ tôi luôn đăng nhập"])
    assert page.is_remember_me_selected() is False

    page.click_login()
    page.assert_logged_in_successfully()

    # Mô phỏng tắt trình duyệt và mở lại: xóa session cookies
    persistent_cookies = [c for c in driver.get_cookies() if "expiry" in c]
    driver.delete_all_cookies()
    for cookie in persistent_cookies:
        driver.add_cookie(cookie)

    driver.get(UTCLoginPage.BASE_URL)
    assert page.is_on_login_page(), "Sau khi mở lại trình duyệt phải yêu cầu đăng nhập lại"
