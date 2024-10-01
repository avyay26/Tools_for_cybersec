#!/bin/bash

# Initialize variables
c=0
d=0

# Loop until the command is successful (exit status 0)
#while true; do
  # Run the executable with the current values of c and d
  out=$(echo "$c,$d" | ./ttt )
  echo "$out"
c=2
d=2
#c,$d"
  # Check if the command was successful
  #if [ $? -ne 0 ]; then
    #break
  #fi

  # Update c and d within the script
 # c=$((c + 1))  # Example increment, modify as needed
 # d=$((d + 1))  # Example increment, modify as needed
#c=2
#d=2
#read <<< #$c,$d"
#don
send "$c,$d"
