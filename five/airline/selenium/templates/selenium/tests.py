from django.test import TestCase

# Create your tests here.
import os 
import pathlib
import unittest

from selenium import webdriver

#Finds the Uniform Resourse Indertifier of a file

def file_url(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

#Sets up a web driver using Google chrome

driver = webdriver.Chrome() 