import enum
from selenium.webdriver.common.by import By


class Browser(enum.Enum):
    FIREFOX = enum.auto()
    IE = enum.auto()
    EDGE = enum.auto()
    CHROME = enum.auto()
    CHROMIUM = enum.auto()
    SAFARI = enum.auto()


class ProfilePictureScraper:
    def __init__(self, browser, binary):
        if browser == Browser.FIREFOX:
            from selenium.webdriver.firefox.webdriver import WebDriver
        elif browser == Browser.IE:
            from selenium.webdriver.ie.webdriver import WebDriver
        elif browser == Browser.EDGE:
            from selenium.webdriver.edge.webdriver import WebDriver
        elif browser == Browser.CHROME:
            from selenium.webdriver.chrome.webdriver import WebDriver
        elif browser == Browser.CHROMIUM:
            from selenium.webdriver.chromium.webdriver import WebDriver
        elif browser == Browser.SAFARI:
            from selenium.webdriver.safari.webdriver import WebDriver

        self.browser = WebDriver(
            executable_path="assets/geckodriver.exe",
            firefox_binary=binary,
        )
        self.browser.implicitly_wait(30)  # Timeout

    def twitter(self, handle):
        self.browser.get(f"https://twitter.com/{handle}/photo")
        return self.browser.find_element(
            by=By.CSS_SELECTOR, value='[draggable="true"]'  # Selector may be unstable, not fully tested (I'll switch to XPath if it does not work)
        ).get_attribute("src")

    def twitch(self, handle):
        self.browser.get(f"https://twitch.tv/{handle}")
        return self.browser.find_element(
            by=By.CSS_SELECTOR, value=f'.tw-image-avatar[alt="{handle}"]'
        ).get_attribute("src")


if __name__ == "__main__":
    scr = ProfilePictureScraper(Browser.FIREFOX, r"C:\Program Files\Mozilla Firefox\firefox.exe")
    print(scr.twitter("TJCTeam"))
    print(scr.twitch("thejocraft_live"))
    scr.browser.close()
