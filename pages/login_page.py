import json
import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Thông báo lỗi thực tế trên trang https://vanphongdientu.utc.edu.vn/Login
ERR_EMPTY_USERNAME = "Bạn chưa nhập tên đăng nhập"
ERR_EMPTY_PASSWORD = "Bạn chưa nhập mật khẩu"
ERR_INVALID_CREDENTIALS = "Tài khoản hoặc mật khẩu không đúng."


def attach_test_case(tc: dict) -> dict:
    """Đính kèm đặc tả hardcode trong file test vào Allure và trả về dữ liệu đầu vào."""
    tc_id = tc["ID"]
    allure.dynamic.description(
        f"**Mã kịch bản:** {tc['ID']}  \n"
        f"**Mô tả:** {tc['Description']}  \n"
        f"**Các bước thực hiện:**\n"
        + "\n".join(f"- {step}" for step in tc["Steps"])
        + f"\n\n**Kết quả kỳ vọng:** {tc['Expected Output']}"
    )
    allure.attach(
        json.dumps(tc, ensure_ascii=False, indent=2),
        name=f"Dữ liệu đặc tả {tc_id} (hardcode)",
        attachment_type=allure.attachment_type.JSON,
    )
    return tc["Giá trị"]


class UTCLoginPage:
    """Page Object cho trang đăng nhập Văn phòng điện tử UTC (dựa trên resources/login.html)."""

    LOGIN_URL = "https://vanphongdientu.utc.edu.vn/Login?r=https%3A%2F%2Fvanphongdientu.utc.edu.vn%2F"
    BASE_URL = "https://vanphongdientu.utc.edu.vn/"

    # Locators từ resources/login.html
    FORM = (By.CSS_SELECTOR, "form[action='/Login'][method='post']")
    HIDDEN_REDIRECT = (By.CSS_SELECTOR, "input[type='hidden'][name='r']")
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "userpwd")
    PERSISTENT_CHECKBOX = (By.ID, "persistent")
    # jQuery trong login.html ẩn input#persistent và chèn label.check[for='persistent'] ngay phía sau
    PERSISTENT_CHECK_LABEL = (By.CSS_SELECTOR, "label.check[for='persistent']")
    PERSISTENT_TEXT_LABEL = (By.CSS_SELECTOR, "label[for='persistent']")
    GOOGLE_OAUTH_LINK = (By.CSS_SELECTOR, "a.button")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input.submit_login[type='submit']")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "div.helps a[href='/Login/GetPass']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.error")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Mở trang đăng nhập Văn phòng điện tử UTC")
    def open(self):
        """Mở trang đăng nhập UTC."""
        self.driver.get(self.LOGIN_URL)
        self.wait.until(EC.presence_of_element_located(self.FORM))
        return self

    @allure.step("Nhập tên đăng nhập: {username!r}")
    def enter_username(self, username: str):
        """Click vào ô username, xóa nội dung cũ và nhập username."""
        el = self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT))
        el.click()
        el.clear()
        if username:
            el.send_keys(username)
        return el

    @allure.step("Nhập mật khẩu: {password!r}")
    def enter_password(self, password: str):
        """Click vào ô password, xóa nội dung cũ và nhập password."""
        el = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        el.click()
        el.clear()
        if password:
            el.send_keys(password)
        return el

    @allure.step("Thiết lập tùy chọn 'Giữ tôi luôn đăng nhập' = {remember}")
    def set_remember_me(self, remember: bool):
        """Tích hoặc bỏ tích 'Giữ tôi luôn đăng nhập'."""
        checkbox = self.driver.find_element(*self.PERSISTENT_CHECKBOX)
        if checkbox.is_selected() != remember:
            labels = self.driver.find_elements(*self.PERSISTENT_CHECK_LABEL)
            if labels and labels[0].is_displayed():
                labels[0].click()
            else:
                self.driver.find_element(*self.PERSISTENT_TEXT_LABEL).click()

    @allure.step("Kiểm tra trạng thái checkbox 'Giữ tôi luôn đăng nhập'")
    def is_remember_me_selected(self) -> bool:
        """Kiểm tra trạng thái checkbox #persistent."""
        checkbox = self.driver.find_element(*self.PERSISTENT_CHECKBOX)
        return checkbox.is_selected()

    @allure.step("Click nút 'Đăng nhập'")
    def click_login(self):
        """Click nút Đăng nhập."""
        btn = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        btn.click()

    @allure.step("Nhấn phím Enter tại ô mật khẩu")
    def submit_with_enter(self):
        """Nhấn phím Enter tại ô mật khẩu."""
        pwd_el = self.driver.find_element(*self.PASSWORD_INPUT)
        pwd_el.send_keys(Keys.ENTER)

    @allure.step("Click liên kết 'Bạn quên mật khẩu đăng nhập ?'")
    def click_forgot_password(self):
        """Click vào liên kết 'Bạn quên mật khẩu đăng nhập ?'."""
        link = self.wait.until(EC.element_to_be_clickable(self.FORGOT_PASSWORD_LINK))
        link.click()

    @allure.step("Click nút 'Đăng nhập bằng e-mail UTC'")
    def click_google_email_login(self):
        """Click vào nút 'Đăng nhập bằng e-mail UTC'."""
        btn = self.wait.until(EC.element_to_be_clickable(self.GOOGLE_OAUTH_LINK))
        btn.click()

    @allure.step("Lấy nội dung thông báo lỗi trên giao diện")
    def get_error_text(self) -> str | None:
        """Lấy nội dung thông báo lỗi trong <div class='error'> nếu có."""
        try:
            err = self.driver.find_element(*self.ERROR_MESSAGE)
            return err.text.strip()
        except NoSuchElementException:
            return None

    def is_on_login_page(self) -> bool:
        """Kiểm tra trình duyệt có đang ở trang đăng nhập hay không."""
        return "/Login" in self.driver.current_url

    @allure.step("Xác nhận đăng nhập thành công và chuyển hướng về trang chủ")
    def assert_logged_in_successfully(self):
        """Khẳng định đã đăng nhập thành công và chuyển sang trang chủ."""
        error_text = self.get_error_text()
        assert error_text is None and not self.is_on_login_page(), (
            f"Đăng nhập không thành công (URL hiện tại: {self.driver.current_url}, "
            f"Thông báo lỗi trên web: {error_text!r})"
        )
