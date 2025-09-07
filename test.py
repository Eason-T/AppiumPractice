import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# 定义设备能力参数
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',  # 使用当前运行的模拟器
    udid='emulator-5554',  # 指定设备ID
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

# Appium服务器地址
appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        """测试前的准备工作，创建WebDriver实例"""
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        """测试后的清理工作，关闭WebDriver"""
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        """测试查找并点击Battery选项"""
        # 查找"Battery"文本元素并点击
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        el.click()
        
        # 等待一下以便观察自动化效果
        import time
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
