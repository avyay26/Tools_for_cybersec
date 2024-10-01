#!/bin/bash

# Create directories if they don't exist
mkdir -p ch us garb
7z x 'chall1(lat).7z'
# Move files to ch directory (assuming these files exist)
mv ~/files.zip ~/enc_pass ~/ch/

# Change directory to ch
cd ch

# Initialize variables for password and encrypted file
pass=""
encfile=""

# Loop through files in current directory
for file in *; do
    # Get the MIME type of the file and ignore warnings
    mime_type=$(file -b --mime-type "$file" 2>~/garb/neww)

    # Check MIME type and assign variables accordingly
    if [ "$mime_type" != "text/plain" ]; then
        encfile="$file"
    elif [ "$mime_type" = "text/plain" ]; then
        pass="$file"
    fi
done

# If no suitable password or encrypted file found, exit
if [ -z "$pass" ] || [ -z "$encfile" ]; then
    echo "Error: No suitable password or encrypted file found."
    exit 1
fi

# Encode password using base32, base64, and hexadecimal
bone=$(base32 "$pass")
btwo=$(base64 "$pass")
hex=$(xxd -p "$pass")

# Try extracting with each encoded password until successful
for password in "$btwo" "$bone" "$hex"; do
    echo "Trying password: $password"
    # Extract with 7z and redirect output to a temporary file
    7z x "$encfile" -p"$password" > ~/garb/new 2>&1
    if [ $? -eq 0 ]; then
        echo "Extraction successful with password: $password"
        break
    fi
done

# Move files back to us directory (assuming paths are correct)
mv "$pass" "$encfile" ~/us/

# Clean up temporary file if needed
