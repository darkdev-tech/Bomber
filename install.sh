#!/bin/bash
clear
echo -e "\033[1;32m"
echo "╔════════════════════════════╗"
echo "║   INSTALLING DEPENDENCIES  ║"
echo "║    Email Bomber XENO v1    ║"
echo "╚════════════════════════════╝"
echo -e "\033[0m"
pkg update -y
pkg install python -y
echo -e "\033[1;34m[✔] Done! Run with: python emailbomber.py\033[0m"
