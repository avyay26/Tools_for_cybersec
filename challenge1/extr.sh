#!/usr/bin/bash

# Create directories if they don't exist
mkdir -p ch us
7z x 'chall1(lat).7z' >/tmp/7z_output.log 2>&1
# Move files to ch directory (assuming these files exist)
mv ~/files.zip ~/enc_pass ~/ch/

# Change directory to ch


# Initialize variables for password and encrypted file
pass=""
encfile=""
flag=true
# Loop through files in current directory
while [ "$flag" = true ];do
cd ~/ch/
  for file in *; do
    # Get the MIME type of the file and ignore warnings
    mime_type=$(file -b --mime-type "$file" 2>/dev/null)

    # Check MIME type and assign variables accordingly
    if [ "$mime_type" != "text/plain" ]; then
        encfile="$file"
        echo  "extracted $encfile"
    elif [ "$mime_type" = "text/plain" ]; then
        pass="$file"
        echo "extracted $pass"
    fi
  done

# If no suitable password or encrypted file found, exit
  if [ -z "$pass" ] || [ -z "$encfile" ]; then
    flag = false

    echo "Error: No suitable password or encrypted file found."
    echo "Flag is $(cat $pass)"
    exit 1
  fi

# Encode password using base32, base64, and hexadecimal
 bone=$(base32 "$pass")
 btwo=$(base64 "$pass")
 hex=$(xxd -p "$pass")
 act=$(cat "$pass")
 extraction_successful=false
 # Try extracting with each encoded password until successful
 for password in "$bone" "$btwo" "$hex" "$act"; do

    # Extract with 7z and redirect output to a temporary file

    if 7z x "$encfile" -p"$password" -aoa >/tmp/7z_output.log 2>&1; then
        echo "Extraction successful with password: $password"
        extraction_successful=true
        break
      #if [ $? -eq 0 ]; then

      #  break
    fi
 done

# Move files back to us directory (assuming paths are correct)
if [ "$extraction_successful" = true ];then
 mv "$pass" "$encfile" ~/us/
fi

# Clean up temporary file if needed
rm -f /tmp/7z_output.log
done
