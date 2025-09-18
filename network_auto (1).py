#Script Code Automation of Network

devices = {
    "Router1": {
        "interfaces": {
            "g0/0": {"ip": "192.168.10.1", "mask": "255.255.255.0"},
            "g0/1": {"ip": "10.0.0.1", "mask": "255.255.255.252"},
        },
        "routing": "ospf"
    },
    "Router2": {                #Router Parts
        "interfaces": {
            "g0/0": {"ip": "192.168.20.1", "mask": "255.255.255.0"},
            "g0/1": {"ip": "10.0.0.2", "mask": "255.255.255.252"},
        },
        "routing": "ospf"
    },
    "Router3": {
        "interfaces": {
            "g0/0": {"ip": "192.168.30.1", "mask": "255.255.255.0"},
            "g0/1": {"ip": "10.0.0.6", "mask": "255.255.255.252"},
            "g0/2": {"ip": "10.0.0.9", "mask": "255.255.255.252"},
        },
        "routing": "ospf"
    },
}

for device, config in devices.items():                  #Device Process
    print(f"\n=== Configuration for {device} ===")
    print(f"hostname {device}")
    for iface, details in config["interfaces"].items():
        print(f"interface {iface}")
        print(f" ip address {details['ip']} {details['mask']}")
        print(" no shutdown")
        print("exit")
    if config["routing"] == "ospf":
        print("router ospf 1")
        for iface, details in config["interfaces"].items():
            ip = details['ip']
            if ip.startswith("192.168"):
                print(f" network {ip} 0.0.0.255 area 0")
        print("exit")
