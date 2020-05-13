#!/bin/bash

domains="./domain.txt"
touch "./ip_sp.txt"
truncate -s 0 ./ip_sp.txt
cat $domains | while read line;
do
    ip=$(dig @114.114.114.114 $line +short | tail -n 1)
    sp=$(curl http://freeapi.ipip.net/$ip)
    echo $line $ip $sp >> ./ip_sp.txt
done
