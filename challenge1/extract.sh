#! /usr/bin/bash

mkdir ch
mkdir us
pass="t"
encfile="t"
7z x 'chall1(lat).7z'
 mv ~/files.zip ~/enc_pass ~/ch/

cd ch

 for i in *; do
    # Get the MIME type of the file
    mime_type=$(file -b --mime-type "$i")

    # Check if the file is not text/plain
    if [ "$mime_type" != "text/plain" ]; then
        encfile="$i"


    # Check if the file is text/plain
    elif [ "$mime_type" = "text/plain" ]; then
        pass="$i"
    fi
done







bone=$(base32 "$pass")

btwo=$(base64 "$pass")

hex=$(xxd -p "$pass")

for i in "$bone","$btwo","$hex";do
   7z x "$encfile" -p"$i"
   if [ $? -eq 0 ]; then
      break
   fi
done
mv ~/ch/"$pass" ~/ch/"$encfile" ~/us/









