#!/bin/bash

cd /var/app

./stockholm -h
echo

# Encrypt files with
echo "== ENCRYPTION =="
./stockholm
echo

ls $HOME/infection

# Test that stockholm encrypted files are not encrypted again
./stockholm
echo

ls $HOME/infection

cat $HOME/infection/get_next_line.c.ft

# Decrypt files
echo "== DECRYPTION =="
./stockholm -r 0123456789ABCDEF
echo

ls $HOME/infection
cat $HOME/infection/get_next_line.c
