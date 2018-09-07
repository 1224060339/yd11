# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 19:50:01 2018

@author: 杨丹
"""
import requests
import random
import re
import json

#需要爬取的页面地址
url="http://www.xicidaili.com/"
#创建UA池，准备随机调用
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


def yemian(url,headers):
	'''
	对url页面发起请求获取页面信息
	'''
	#发起请求
	response = requests.get(url,headers=random.choices(headers)[0])
	response.encoding = "utf-8"
	if response.status_code == 200:
		# print(response.text)
		return response.text
	else:
		print("响应失败")
		yemian(url,headers)

def pipei():
	'''
	利用万能正则表达式匹配需要的数据ip,端口号,协议类型
	获取到需要的数据
	'''
	response=yemian(url,headers)
	str1 = '<td class="country"><img[\s\S]+?<td>'
	#ip
	str2 = '</td>[\s\S]*?<td>'
	#端口号
	str3 = '</td>[\s\S]*?<td>[\s\S]*?<td>'
	#协议类型
	str4 = '</td>'
	regex = str1+"([\s\S]*?)"+str2+"([\s\S]*?)"+str3+"([\s\S]*?)"+str4
	IP_List = re.findall(regex, response)
	return IP_List

def test_ip(ip,port,headers):
	server = ip+":"+port
	proxies = {'http': 'http://' + server}
	try:
		r = requests.get('https://www.baidu.com/', headers=random.choices(headers)[0],proxies=proxies,timeout=1)
		if r.status_code == 200:
			return 1
		else:
			return None
	except:
		return None

def ip_pool():
	'''
	对获取到的ip进行筛选，利用每个ip进行访问百度，是否成功
	返回筛选后的ip池
	'''
	L=pipei()
	for i in L:
		#如果ip不可用,从L中删除
		if not test_ip(i[0],i[1],headers):
			L.remove(i)
	#返回筛选后的L
	return L


if __name__ == '__main__':
	L=ip_pool()
	for i in L:
		with open("ip代理池", "a", encoding="utf-8") as f:
			f.write(json.dumps(i, ensure_ascii=False)+'\n')