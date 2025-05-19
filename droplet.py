import requests
import json
import sys

# X: @owldecoy

API_URL = "https://api.digitalocean.com/v2/droplets"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": ""
}

def create_droplet(api_key):
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {api_key}"

    droplet_data = {
        "name": "droplet",
        "region": "nyc1",
        "size": "s-1vcpu-512mb-10gb",
        "image": "debian-12-x64",
        "ssh_keys": [],
        "backups": False,
        "ipv6": False,
        "private_networking": None,
        "volumes": None,
        "tags": ["droplet"]
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(droplet_data))

    if response.status_code == 202:
        print("Droplet created successfully.")
        print("Response:", response.json())
    else:
        print("Error creating droplet.")
        print("Response:", response.text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python droplet.py <API_KEY>")
    else:
        api_key = sys.argv[1]
        create_droplet(api_key)
