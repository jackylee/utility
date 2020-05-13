#!/bin/bash

domains="./domain_fail.txt"
touch "./ip_sp.txt"
truncate -s 0 ./ip_sp.txt
cat $domains | while read line;
do
    ip=$(dig @111.11.11.1 $line +short | tail -n 1)
    sp=$(curl http://freeapi.ipip.net/$ip)
    echo $line $ip $sp >> ./ip_sp.txt
done
