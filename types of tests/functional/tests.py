import os
import unittest

from selenium import webdriver


class TestButton(unittest.TestCase):
    def test_clicking_button_shows_alert(self):
        driver = webdriver.Firefox()
        current_directory = os.path.dirname(os.path.realpath(__file__))
        path = 'file://%s' % os.path.join(current_directory, 'index.html')
        print path
        driver.get(path)
        button = driver.find_element_by_css_selector("#click_me_button")
        button.click()

        alert = driver.switch_to.alert
        assert alert.text == 'test'
        alert.accept()

        driver.close()


if __name__ == "__main__":
    unittest.main()
