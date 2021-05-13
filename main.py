#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import ytParse

if __name__=="__main__":
    try:
        url = sys.argv[1]
        yt = ytParse.ytParse(url)
        yt.main()
        yt.save("./result.json")
        del yt
    except IndexError as e:
        print("Usege: python main.py <url>")
