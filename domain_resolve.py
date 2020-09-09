import requests
import dns.resolver
import sys
import pycurl
import time

nameserver = '111.11.11.1'

'''指定DNS服务器获取域名解析，返回CNAME记录和A记录'''
def get_dns_record(domain, nameserver):
    dns_record = {}
    dns_record['CNAME'] = []
    dns_record['A'] = []
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = []
    resolver.nameservers.append(nameserver)
    answer = resolver.query(domain)
    for rr in answer.response.answer:
        for j in rr.items:
            #CNAME记录
            if rr.rdtype == 5:
                dns_record['CNAME'].append(j)
            #A RECORD
            elif rr.rdtype == 1:
                dns_record['A'].append(j)
    return dns_record

class ipgeolocation():
    def __init__(self):
        self.XRL = 45
        self.XTTL = 60

    def get_ip_location(self,ip):
        if self.XRL == 0:
            time.sleep(self.XTTL)
        try:
            req = requests.get('http://ip-api.com/json/%s' % ip)
            print(req.status_code)
            if req.status_code != 200:
                self.XRL = int(req.headers['X-Rl'])
                self.XTTL = int(req.headers['X-Ttl'])
                return
            else:
                self.XRL = int(req.headers['X-Rl'])
                self.XTTL = int(req.headers['X-Ttl'])
                print('XRL: %d XTT: %d' % (self.XRL, self.XTTL))
                json = req.json()
                ans = []
                ans.append(ip)
                ans.append(json['country'])
                ans.append(json['regionName'])
                ans.append(json['city'])
                ans.append(json['isp'])
                ans.append(json['as'])
                return ans
        except:
            pass

location = ipgeolocation()

def get_domain_info(domain):
    info = get_dns_record(domain, nameserver)
    if not info:
        return None
    elif 'A' not in info:
        return None
    elif not info['A']:
        return None
    else:
        ip = info['A'][0]
        ans = location.get_ip_location(ip)
        print("%s %s" % (ip, ans))
        return ans

def domain_resove(argv):
    if len(argv) < 2:
        print('%s input' % argv[0])
        sys.exit(-1)
    output = open('output.txt', 'w')
    with open(argv[1], 'r') as f:
        for line in f.readlines():
            record = get_domain_info(line[:-1])
            if not record:
                continue
            else:
                print('%s %s %s %s %s %s %s\n' % (line[:-1], record[0], record[1], record[2], record[3], record[4], record[5]))
                output.write('%s %s %s %s %s %s %s\n' % (line[:-1], record[0], record[1], record[2], record[3], record[4], record[5]))
        output.close()

def ip_resolve(argv):
    if len(argv) < 2:
        print('%s input' % argv[0])
        sys.exit(-1)
    output = open('output.txt', 'w')
    with open(argv[1], 'r') as f:
        for ip in f.readlines():
            isp = location.get_ip_location(ip[:-1])
            if not isp:
                continue
            else:
                output.write('%s %s\n' % (ip[:-1], isp))
    output.close()

if __name__ == '__main__':
    ip_resolve(sys.argv)