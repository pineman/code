#!/bin/bash
set -uxo pipefail

# https://docs.mitmproxy.org/stable/howto-transparent/
# https://docs.mitmproxy.org/stable/howto-wireshark-tls/

# run ./mitmproxy.sh start on one terminal
# on another, run ./mitmproxy.sh addca 
# to stop quit mitmproxy and run ./mitmproxy.sh clean

start() {
sudo sysctl net.ipv4.conf.all.send_redirects=0
sudo useradd -m mitmproxy; sudo chmod 777 /home/mitmproxy
sudo iptables -t nat -A OUTPUT -p tcp -m owner ! --uid-owner mitmproxy --dport 80 -j REDIRECT --to-port 8080
sudo iptables -t nat -A OUTPUT -p tcp -m owner ! --uid-owner mitmproxy --dport 443 -j REDIRECT --to-port 8080
sudo ip6tables -t nat -A OUTPUT -p tcp -m owner ! --uid-owner mitmproxy --dport 80 -j REDIRECT --to-port 8080
sudo ip6tables -t nat -A OUTPUT -p tcp -m owner ! --uid-owner mitmproxy --dport 443 -j REDIRECT --to-port 8080
sudo -H -u mitmproxy bash -c 'SSLKEYLOGFILE="/home/mitmproxy/sslkeylogfile-mitmproxy.txt" mitmproxy --mode transparent --showhost --set block_global=false'
}

addca() {
sudo trust anchor --store /home/mitmproxy/.mitmproxy/mitmproxy-ca-cert.pem
}

clean() {
sudo trust anchor --remove /home/mitmproxy/.mitmproxy/mitmproxy-ca-cert.pem
sudo iptables -t nat -D OUTPUT -p tcp -m owner ! --uid-owner mitmproxy --dport 80 -j REDIRECT --to-port 8080
sudo iptables -t nat -D OUTPUT -p tcp -m owner ! --uid-owner mitmproxy --dport 443 -j REDIRECT --to-port 8080
sudo ip6tables -t nat -D OUTPUT -p tcp -m owner ! --uid-owner mitmproxy --dport 80 -j REDIRECT --to-port 8080
sudo ip6tables -t nat -D OUTPUT -p tcp -m owner ! --uid-owner mitmproxy --dport 443 -j REDIRECT --to-port 8080
sudo userdel -r mitmproxy
sudo sysctl net.ipv4.conf.all.send_redirects=1
}

eval "$1"
