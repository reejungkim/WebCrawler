#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:49:39 2021

@author: reejungkim
"""

#from apps import GetReviewGooglePlayStore
from GetReviewGooglePlayStore import GetGooglePlayStore

import time
from bs4 import BeautifulSoup
import sys, io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import *

GetGooglePlayStore(link="https://play.google.com/store/apps/details?id=com.kakaobank.channel&hl=ko&showAllReviews=true")
print("done!")