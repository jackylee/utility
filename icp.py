import requests
import re
import sys
import urllib
import time
from lxml import etree

def icpExtract(site):
    try:
        icp = re.compile(u"冀ICP备.*号-*\d*")
        extract_url = "http://icp.chinaz.com/".encode("utf-8") + site.encode("utf-8")
        '''extract_url = "http://icp.chinaz.com/info?q=".encode("utf-8") + site.encode("utf8")'''
        headers = {'Host' : 'icp.chinaz.com', 'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36'}
        headers['Referer'] = 'icp.chinaz.com/'+site
        '''print(headers)'''
        #headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel …) Gecko/20100101 Firefox/61.0'}
        req = requests.get(extract_url, headers = headers)
        '''print(req.text)'''
        '''html = etree.HTML(req.text)'''
        '''html_data = html.xpath('/html/body/div[2]/div[2]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/text()')'''
        '''print(html_data[0])'''
        results = re.search('冀ICP备.*号-*\d*', req.text)
        if results is not None:
            print(results[0])
            return results[0]
        else:
            return None
        if html_data is None:
            return None
        else:
            return html_data[0]
    except:
        e = sys.exc_info()[0]
        print("exception happends" + e)
        pass

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage:query.py site_file output_file")
        sys.exit(-1)
    site_icp = {}
    input_file = open(sys.argv[1], 'r')
    total = 0
    for site in input_file.readlines():
        if site.startswith("http://"):
            site = site[7:-1]
        elif site.startswith("https://"):
            site = site[8:-1]
        else:
            site = site[:-1]
        icp = icpExtract(site)
        #time.sleep(2)
        print("分析%s %s" % (site, icp))
        total = total + 1
        if icp is not None and icp != '--':
            site_icp[site] = icp
        else:
            icp = icpExtract(site)
            print("分析%s %s" % (site, icp))
            if icp is not None and icp != '--':
                site_icp[site] = icp
            else:
                site_icp[site] = None
    input_file.close()
    count = 0
    output = open(sys.argv[2], 'w')
    for k,v in site_icp.items():
        print("site: %s, icp: %s" % (k, v))
        count = count + 1
        output.write("%s %s\n" % (k, v))
    output.close()
    print("总计%d 爬取%d" % (total, count))


