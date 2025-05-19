# Droplet
A quick Digital Ocean Debian 12 droplet creator. Will create the cheapest droplet available (`s-1vcpu-512mb-10gb`) and within the `nyc1` region. You can modify these options if you so desire:

```python
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
```

# Usage
`python droplet.py <api_key>`
