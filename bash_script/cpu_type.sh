#!/usr/bin/env bash
# 判断CPU厂商

m=`cat /proc/cpuinfo |grep vendor_id|awk -F":" '{print $2}'|tail -1`
if [ $m == "GenuineIntel" ]
then
echo "CPU is 英特尔"
elif [ $m == "AuthenticAMD" ]
then
echo "CPU is AMD"
else
echo "CPU is 非主流"
fi
