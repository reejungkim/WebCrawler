#!/usr/bin/env python
# coding: utf-8

# In[7]:


import time
from bs4 import BeautifulSoup
import sys, io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import *


# In[8]:
def GetGooglePlayStore(link):

    
    no_of_reviews = 10000
    
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    driver = webdriver.Chrome("/Users/reejungkim/Downloads/chromedriver")
    
    wait = WebDriverWait( driver, 20 )
    
    
    # In[9]:
    
    
    #Append your app store urls here
    #urls = ["https://play.google.com/store/apps/details?id=kr.co.ssg&hl=ko&gl=KR"]
    urls = [link]
    
    # In[10]:
    
    
    import pandas as pd
    df = pd.DataFrame()
    
    
    # In[11]:
    
    for url in urls:
    
        driver.get(url)
    
        page = driver.page_source
    
        soup_expatistan = BeautifulSoup(page, "html.parser")
    
        # open all reviews
        url = url+'&showAllReviews=true'
        driver.get(url)
        time.sleep(20) # wait dom ready
        for i in range(1,30):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')#scroll to load other reviews
            time.sleep(30)
        page = driver.page_source
    
        soup_expatistan = BeautifulSoup(page, "html.parser")
        expand_pages = soup_expatistan.findAll("div", class_="d15Mdf")
        counter = 1
        for expand_page in expand_pages:
            try:
                
                author = str(expand_page.find("span", class_="X43Kjb").text)
                review_date = expand_page.find("span", class_="p2TkOb").text
                
                #print("\n===========\n")
                #print("review："+str(counter))
                #print("Author Name: ", author)
                #print("Review Date: ", review_date)
                '''
                //didn't find reviewer link
                print("Reviewer Link: ", expand_page.find("a", class_="reviews-permalink")['href'])
                '''
                reviewer_ratings = expand_page.find("div", class_="jUL89d y92BAb").text
                #print("Reviewer Ratings: ", reviewer_ratings)
                '''
                //didn't find review title
                print("Review Title: ", str(expand_page.find("span", class_="review-title").string))
                '''
                review_body = str(expand_page.find("div", class_="UD7Dzf").text)
                #print("Review Body: ", review_body)
                
                star = expand_page.find("div", class_="pf5lIe").find_next()['aria-label']
                
                developer_reply = expand_page.find_parent().find("div", class_="LVQB0b")
                #if hasattr(developer_reply, "text"):
                #    print("Developer Reply: "+"\n", str(developer_reply.text))
                #else:
                #    print("Developer Reply: ", "")
            
    
                new_row = {'author':author, 'review_date':review_date, 
                           'reviewer_ratings':reviewer_ratings, 'review':review_body, 'star':star,
                           'developer_reply': developer_reply
                    }
                df = df.append(new_row, ignore_index=True)
    
                counter+=1
            except:
                pass
    driver.quit()
    # In[12]:
    
    
    import datetime as dt
    timestamp = dt.datetime.today().strftime('%Y-%m-%d-%H:%m:%S')
    file_name = 'GooglePlayStore_Review_' + timestamp + '.csv'
    df.to_csv(file_name, index = True)
    
    return df
    
    
    
