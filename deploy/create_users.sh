#!/bin/bash
sudo groupadd -f students

for username in NickMarkovicz Pervyshev27062004 vitaliypavlovich andreymamona Akhralovich faridjon7 Andreas-Lych juls-teacher akinfina-ulyana GrinevichEvgen harankou-anton UlianaMeashkova
do
    port=$((RANDOM * (8100 - 8000) / 32767 + 8000))
    password=$(cat /proc/sys/kernel/random/uuid|sha256sum|base64|head -c 16)
    sudo useradd $username -p $(openssl passwd -1 "$password")  -s /bin/bash -m -G students
    echo "$username:$password:$port"
done

