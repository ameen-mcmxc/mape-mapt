#!/bin/bash

# Syn-flood protection by rate limiting the packets with 10 packets per second
/sbin/ip netns exec napt iptables -A FORWARD -p tcp --syn -m limit  --limit 10/s -j ACCEPT

# Dropping all other malicious packets that exceed the rate limit
/sbin/ip netns exec napt iptables -A FORWARD -p tcp --syn -j DROP
