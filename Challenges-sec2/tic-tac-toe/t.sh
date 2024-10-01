#! /usr/bin/bash
c=0
d=0
#while [ $? -ne 0 ];do
out=$(echo "$c,$d" | ./ttt)
echo "$out"
c=2
d=2
read "$c,$d"
#while [ $? -ne 0 ];do
#out=$(echo "$c,$d" |
#echo "$out"
#done
#done

