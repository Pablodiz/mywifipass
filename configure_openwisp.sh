#!/bin/ash 

exec > /tmp/log.txt 2>&1
set -x 

# execute with "sh ./configure_openwisp.sh &"

sed -i 's|^root:[^:]*:|root:$6$2Mj1SdFAZ0hUDdUT$HXaRJORBXqaZqqbMx8EgzoLMxc.mTRa33zaMoLflO7qZh7gWIkIh.ag4vWMItHNF1OtqMkHoSfQ0BHUML71Xu.:|' /etc/shadow

uci batch <<EOC
set network.lan.ipaddr=192.168.100.1 # change internal range so that if the one on WAN side is 192.168.1.1 there are no errors 
set network.lan.mask=255.255.255.0 
add firewall rule # add a rule for letting ssh through wan interface
set firewall.@rule[-1].name='Allow-SSH-WAN'
set firewall.@rule[-1].src='wan'
set firewall.@rule[-1].proto='tcp'
set firewall.@rule[-1].dest_port='22'
set firewall.@rule[-1].target='ACCEPT'
set firewall.@rule[-1].family='ipv4'
EOC

uci commit
/etc/init.d/network restart
/etc/init.d/firewall restart

cd /tmp
opkg update
opkg remove $(opkg list-installed | grep '^wpad-' | cut -d' ' -f1) # We remove the current wpad package
opkg install wpad-openssl

wget https://downloads.openwisp.io/openwisp-config/latest/openwisp-config_1.1.0-1_all.ipk
wget https://storage.googleapis.com/downloads.openwisp.io/openwisp-monitoring/latest/netjson-monitoring_0.2.1-1_all.ipk
wget https://storage.googleapis.com/downloads.openwisp.io/openwisp-monitoring/latest/openwisp-monitoring_0.2.1-1_all.ipk
opkg install openwisp-config_1.1.0-1_all.ipk
opkg install openwisp-monitoring_0.2.1-1_all.ipk
opkg install netjson-monitoring_0.2.1-1_all.ipk


echo "192.168.1.69 dashboard.openwisp.org api.openwisp.org openvpn.openwisp.org" |      tee -a /etc/hosts

MNG_IFACE=$(uci get network.wan.device)

cat <<EOC > /etc/config/openwisp 
config controller 'http'
    option url 'https://dashboard.openwisp.org'
    option verify_ssl '0'
    option shared_secret '2qni8daYCv0jLvDneueQLEKgtCHxTxdl'
    option management_interface '$MNG_IFACE'
    option uuid ''
    option key ''
EOC

mkdir /etc/init.d/openwisp
/usr/sbin/openwisp-reload-config
/etc/init.d/openwisp-config restart
