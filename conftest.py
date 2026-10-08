from pathlib import Path
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Chạy trình duyệt Chrome ở chế độ headless (không giao diện)",
    )


def _find_cached_chromedriver() -> str | None:
    """Tìm ChromeDriver đã được Selenium Manager tải sẵn trong ~/.cache/selenium."""
    cache_dir = Path.home() / ".cache" / "selenium" / "chromedriver"
    if cache_dir.exists():
        drivers = sorted(cache_dir.rglob("chromedriver"), reverse=True)
        for drv in drivers:
            if drv.is_file():
                return str(drv)
    return None


@pytest.fixture(scope="function")
def driver(request):
    """Fixture khởi tạo và đóng Chrome WebDriver cho mỗi test case."""
    headless = request.config.getoption("--headless")

    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    cached_driver = _find_cached_chromedriver()
    if cached_driver:
        service = Service(executable_path=cached_driver)
        web_driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        web_driver = webdriver.Chrome(options=chrome_options)

    web_driver.implicitly_wait(5)

    yield web_driver

    web_driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook tự động chụp ảnh màn hình trình duyệt và đính kèm vào Allure Report."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and "driver" in item.funcargs:
        web_driver = item.funcargs["driver"]
        try:
            status_label = "FAILED" if report.failed else "PASSED"
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name=f"Screenshot [{status_label}] - {item.name}",
                attachment_type=allure.attachment_type.PNG,
            )
            allure.attach(
                web_driver.current_url,
                name="URL hiện tại sau khi thực thi",
                attachment_type=allure.attachment_type.TEXT,
            )
        except Exception:
            pass


def pytest_sessionfinish(session, exitstatus):
    """Ghi thông tin môi trường và sinh viên vào Allure Report sau khi chạy xong."""
    allure_dir = session.config.getoption("--alluredir")
    if allure_dir:
        results_path = Path(allure_dir)
        results_path.mkdir(parents=True, exist_ok=True)
        env_file = results_path / "environment.properties"
        env_content = (
            "Sinh_Vien=Nguyen Thanh Tri\n"
            "MSSV=6451071079\n"
            "Hoc_Phan=Kiem thu phan mem\n"
            "He_Thong_Kiem_Thu=Van phong dien tu UTC (https://vanphongdientu.utc.edu.vn/Login)\n"
            "Trinh_Duyet=Google Chrome\n"
            "Framework=Selenium 4 + Pytest + Allure Report\n"
        )
        env_file.write_text(env_content, encoding="utf-8")
