#! /usr/bash/bin

#content=$(<newsort.txt)
readarray -t lines < "newsort.txt"

echo "This is the sixth element:${lines[6]}"
echo "The length of the given array is :${#lines[@]}"

# binary search:
i=0
j="${#lines[@]}"
j=$((j-1))
p="True"
curr=$((i/2+j/2))
#first try 1 and end
#then try middle
while [ "$p" = "True" ];
do
  echo "$i"
  echo "$j"
  #curr=$((i/2+j/2))
  echo "$curr"
  check=$(echo "${lines[curr]}" | ./bruteforcer)
  if  [ "$(echo "$check")" = "Enter your password : WRONG :( Key too low" ];then
      curr=$((j/2+curr/2))
      i=$((curr))

  elif [ "$(echo "$check")" = "Enter your password : WRONG :( Key too high" ];then
      curr=$((curr/2+i/2))
      j=$((curr))

  else
     echo "$check" > flag.txt
     break
   fi

done

