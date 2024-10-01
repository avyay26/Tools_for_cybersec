#! /use/bin/bash
ori=""
se=$(echo {a..z} {A..Z} {0..9} _ | tr -d ' ')
echo "$se"
or=""
len=30
check="True"
while [ "$check" = "True" ];do

string=$(cat /dev/urandom | tr -dc "$se" | fold -w "$len" | head -n 1)
string="$or$string"
num=$(echo "$string" | ./notwordle | grep -o '[0-9]\+' | head -n 2 | sed -n '2p')
len=$((30-num))
if [ "$len" != 0 ];then
or="${string:0:num}"
fi
if [ "$len" = 0 ];then
check="False"
echo "$string">"password.txt"
break
fi
echo "$num"
echo "$string"
echo "$or"
done
