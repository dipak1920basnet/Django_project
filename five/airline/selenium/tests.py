from django.test import TestCase
import time
# Create your tests here.
import os 
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

#Finds the Uniform Resourse Indertifier of a file

def file_url(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

#Sets up a web driver using Google chrome

driver = webdriver.Chrome() 


#Standard outline of testing class
class WebpageTests(unittest.TestCase):

    def test_title(self):
        """
        Make sure title is correct
        """
        driver.get(file_url("counter.html"))
        self.assertEqual(driver.title,"Document")

    def test_increase(self):
        """Make sure header updated to 1 after 1 click of increase button"""
        driver.get(file_url("counter.html"))
        increase = driver.find_element(By.ID,"increase")
        increase.click()
        self.assertEqual(driver.find_element(By.TAG_NAME,"h1").text, "1")

    def test_decrease(self):
        """Make sure header updated to -1 after click of decrease button"""
        driver.get(file_url("counter.html"))
        decrease = driver.find_element(By.ID, "decrease")
        decrease.click()
        self.assertEqual(driver.find_element(By.TAG_NAME,"h1").text, "-1")

    def test_multiple_increase(self):
        """Make sure header updated to 3 after 3 clicks of increase button"""
        driver.get(file_url("counter.html"))
        increase = driver.find_element(By.ID,"increase")
        for i in range(3):
            time.sleep(2)
            increase.click()
        self.assertEqual(driver.find_element(By.TAG_NAME,"h1").text, "3")

if __name__ == "__main__":
    unittest.main()