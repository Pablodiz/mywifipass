import os
import sys
import django

# RADIUS_PORT, RADIUS_SERVER and RADIUS_SECRET need to be defined as env variables

# Add the project directory to PYTHONPATH
sys.path.append('/opt/openwisp/')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'openwisp2.settings')
django.setup()

# Import models
from openwisp_controller.config.models import Template
from openwisp_users.models import Organization, User

radius_secret = os.environ.get("RADIUS_SECRET", "")
if not radius_secret:
    raise ValueError("RADIUS_SECRET environment variable is not set.")

radius_port = os.environ.get('RADIUS_PORT', 10812)
if not radius_port.isdigit():
    raise ValueError("RADIUS_PORT environment variable must be a number.")

radius_port = int(radius_port)

radius_server = os.environ.get('RADIUS_SERVER', "radius-server")


# Load your JSON configuration
config_json = {
    "interfaces": [
        {
            "wireless": {
                "network": ["lan"],
                "mode": "access_point",
                "radio": "radio0",
                "ack_distance": 0,
                "rts_threshold": 0,
                "frag_threshold": 0,
                "ssid": "TLS_Wifi",
                "hidden": False,
                "wds": False,
                "encryption": {
                    "protocol": "wpa2_enterprise",
                    "key": radius_secret,
                    "disabled": False,
                    "cipher": "auto",
                    "ieee80211w": "0",
                    "server": radius_server,
                    "port": radius_port,
                    "acct_server": "",
                    "acct_server_port": 1813,
                    "acct_secret": "",
                    "acct_interval": 600,
                    "dae_client": "",
                    "dae_port": 3799,
                    "dae_secret": "",
                    "nasid": ""
                },
                "wmm": True,
                "isolate": False,
                "ieee80211r": False,
                "reassociation_deadline": 1000,
                "ft_psk_generate_local": False,
                "ft_over_ds": True,
                "rsn_preauth": False,
                "macfilter": "disable",
                "maclist": []
            },
            "type": "wireless",
            "name": "wireless",
            "mtu": 1500,
            "disabled": False,
            "network": "",
            "mac": "",
            "autostart": True,
            "addresses": []
        }
    ],
    "radios": [
        {
            "protocol": "802.11n",
            "name": "radio0",
            "phy": "",
            "channel": 0,
            "channel_width": 20,
            "tx_power": 20,
            "country": "ES",
            "disabled": False,
            "driver": "mac80211",
            "hwmode": "11g",
            "band": "2g"
        }
    ]
}

# Get user and organization (adjust to your environment)
user = User.objects.get(username='admin')  # or by ID
organization = Organization.objects.first()  # or select as needed

# Create the template
Template.objects.create(
    name='EAP-TLS Template 11',
    config=config_json,
    organization=organization,
    type='generic',
    default=False,
    required=False,
    auto_cert=False,
    backend='netjsonconfig.OpenWrt',
    default_values={},
)

print("Template created successfully.")


# Docker CP + docker exec ... python3...