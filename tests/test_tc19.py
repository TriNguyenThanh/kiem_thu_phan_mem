import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import UTCLoginPage, attach_test_case


# Đặc tả và dữ liệu được hardcode; không đọc file nguồn khi chạy test.
TEST_CASE = {
    "STT": 19,
    "ID": "TC19",
    "Description": "Đăng xuất sau khi đăng nhập thành công",
    "Steps": [
        "Mở trang đăng nhập https://vanphongdientu.utc.edu.vn.",
        "Nhập username.",
        "Nhập password.",
        "Click nút Đăng nhập.",
        "Click Đăng xuất.",
        "Truy cập lại trang yêu cầu xác thực.",
    ],
    "Giá trị": {
        "Username": "huongnt",
        "Password": "123456@utc",
        "Thao tác": "Đăng xuất",
    },
    "Expected Output": "Kết thúc phiên đăng nhập. Yêu cầu xác thực lại khi truy cập trang được bảo vệ.",
}


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
@allure.story("Luồng đăng nhập thành công & Quản lý phiên")
@allure.title("TC19: Đăng xuất sau khi đăng nhập thành công")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc19_logout_after_login(driver):
    """TC19: Đăng xuất sau khi đăng nhập thành công."""
    data = attach_test_case(TEST_CASE)
    page = UTCLoginPage(driver).open()

    page.enter_username(data["Username"])
    page.enter_password(data["Password"])
    page.click_login()

    page.assert_logged_in_successfully()

    # Tìm và click liên kết Đăng xuất trên trang chủ
    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, 'Logout') or contains(@href, 'logout') or contains(text(), 'Đăng xuất') or contains(text(), 'Thoát')]")
        )
    )
    logout_link.click()

    # Truy cập lại trang chủ yêu cầu xác thực
    driver.get(UTCLoginPage.BASE_URL)
    assert page.is_on_login_page(), "Vẫn truy cập được trang bảo vệ sau khi đã đăng xuất"
