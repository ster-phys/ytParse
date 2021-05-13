# -*- coding: utf-8 -*-

import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

class ytParse():
    def __init__(self, url):
        self.ytURL = url
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome("./chromedriver", options=options)
        self.driver.implicitly_wait(10)
        self.html = None
        self.videoList = []

    def main(self):
        self.driver.get(self.ytURL)

        while True:
            for _ in range(50):
                self.pageDown()
            html = self.driver.page_source
            if self.html == html:
                break
            else:
                self.html = html

        self.html.encode('utf-8')

        soup = BeautifulSoup(self.html, 'lxml')
        souplist = soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-grid-video-renderer")
        for video in souplist:
            id = video.get("href").replace("/watch?v=","")
            title = video.get("title")
            self.videoList.append({"id":id,"title":title})

    def pageDown(self):
        body = self.driver.find_element_by_css_selector('body')
        body.send_keys(Keys.PAGE_DOWN)

    def save(self,path=""):
        if path == "":
            print("Specify the path to save.")
            return
        else:
            if not path.endswith(".json"):
                path += ".json"

            with open(path, 'w') as f:
                json.dump(self.videoList, f, indent=4, ensure_ascii=False)

    def __del__(self):
        self.driver.quit()
