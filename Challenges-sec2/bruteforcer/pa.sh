q#!/usr/bin/bash

# Read the content of the file into an array
readarray -t lines < "newsort.txt"

echo "This is the sixth element: ${lines[6]}"
echo "The length of the given array is: ${#lines[@]}"

# Binary search initialization
i=0
j=$((${#lines[@]} - 1))
p="True"

while [ "$p" = "True" ]; do
    curr=$(( (i + j) / 2 ))

    echo "i: $i"
    echo "j: $j"
    echo "curr: $curr"
    # Check the current element
    check=$(echo "${lines[curr]}" | ./bruteforcer)

    if [ "$(echo "$check")" = "Enter your password : WRONG :( Key too low" ]; then
        i=$((curr + 1))
    elif [ "$(echo "$check")" = "Enter your password : WRONG :( Key too high" ]; then
        j=$((curr - 1))
    else
        echo "$check ${lines[$curr]}" > flag.txt
        echo "${lines[$curr]}"
        p="False"
    fi
done
