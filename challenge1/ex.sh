#!usr/bin/bash/

for i in $(ls); do
    if [ "$(file -b --mime-type "$i")" == "text/plain" ]; then
        cat "$i" >> pass.txt;mv /home/sreeavyay/ext/"$i" /home/sreeavyay/used/
    fi
done

for i in $(ls); do
    if [ "$(file -b --mime-type "$i")" != "text/plain" ]; then
        7z x -p/home/sreeavyay/ext/pass.txt "$i";mv /home/sreeavyay/"$i"  /home/sreeavyay/used/
    fi
done
