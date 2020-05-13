from netaddr import *
import sys

ip_list = []

ips = open(sys.argv[1], 'r')
output = open('merged.txt', 'w')

for line in ips.readlines():
    ip_list.append(IPNetwork(line[:-1]))
print(len(ip_list))

final = cidr_merge(ip_list)
for ip in final:
    output.write('%s\n' % ip)
ips.close()
output.close()
