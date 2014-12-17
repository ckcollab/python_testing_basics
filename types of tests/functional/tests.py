import os
import unittest

from selenium import webdriver


class TestButton(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        '''Need this in tearDown method because it's always called, otherwise we have
        hanging processes left over'''
        self.driver.close()

    def test_clicking_button_shows_alert(self):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        path = 'file://%s' % os.path.join(current_directory, 'index.html')
        self.driver.get(path)
        button = self.driver.find_element_by_css_selector("#click_me_button")
        button.click()

        alert = self.driver.switch_to.alert
        assert alert.text == 'test'
        alert.accept()


if __name__ == "__main__":
    unittest.main()
