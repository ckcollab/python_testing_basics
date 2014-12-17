import os
import unittest

from selenium import webdriver


class TestButton(unittest.TestCase):
    def test_clicking_button_shows_alert(self):
        driver = webdriver.Firefox()
        path = os.path.join(os.getcwd(), 'index.html')
        driver.get(path)
        button = driver.find_element_by_css_selector("#click_me_button")
        button.click()

        alert = driver.switch_to.alert
        assert alert.text == 'test'
        alert.accept()

        driver.close()


if __name__ == "__main__":
    unittest.main()
