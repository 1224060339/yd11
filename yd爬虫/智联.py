# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 19:50:01 2018

@author: 杨丹
"""
import requests
import random
import re
import json

headers=[{'User-Agent': 'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'}, 
			{'User-Agent': 'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'},
			{'User-Agent': 'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;'},
			{'User-Agent': 'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)'},
			{'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)'},
			{'User-Agent': 'Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)'}, 
			{'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1'}, 
			{'User-Agent': 'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'}, 
			{'User-Agent': 'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11'}, 
			{'User-Agent': 'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11'},
			{'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11'}, 
			{'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)'},
			{'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)'},
			{'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)'},
			{'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)'},
			{'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)'},
			{'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)'}, 
			{'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)'}, 
			{'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)'}]

