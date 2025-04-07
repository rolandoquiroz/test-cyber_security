#!/bin/bash
awk '{ip=$1; req=$6} NR==1{max_ip=ip; max_req=req} {ip_count[ip]++; if(ip_count[ip]>ip_count[max_ip]) max_ip=ip; ip_req[ip,req]++} END{for(i in ip_req) {split(i,a,SUBSEP); if(a[1]==max_ip && ip_req[i]>max) {max=ip_req[i]; res=a[2]}}} END{print res}' logs.txt
