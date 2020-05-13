#!/bin/bash

domains="./ip_hy.txt"
touch "./ip_sp.txt"
cat $domains | while read line;
do
    sp=$(curl http://freeapi.ipip.net/$line >/dev/null 1>&2)
    echo $line $sp
done
