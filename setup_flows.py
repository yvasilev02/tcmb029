import requests
import json

# Floodlight controller URL
floodlight_url = 'http://172.19.0.2:8080'

# Example MAC addresses of the two furthest hosts
host1_mac = '00:00:00:00:00:01'
host2_mac = '00:00:00:00:00:02'

# Function to add a flow entry
def add_flow_entry(switch, name, src_mac, dst_mac, out_port):
    flow = {
        "switch": switch,
        "name": name,
        "cookie": "0",
        "priority": "32768",
        "eth_type": "0x0800",
        "eth_src": src_mac,
        "eth_dst": dst_mac,
        "active": "true",
        "actions": f"output={out_port}"
    }

    response = requests.post(f"{floodlight_url}/wm/staticentrypusher/json", data=json.dumps(flow))
    if response.status_code == 200:
        print(f"Flow {name} added successfully")
    else:
        print(f"Failed to add flow {name}: {response.text}")

# Main function to add bi-directional flows
def main():
    # Assuming the switches and ports are known
    # Replace these values with actual switch IDs and port numbers
    switch1 = '00:00:00:00:00:00:00:01'
    switch2 = '00:00:00:00:00:00:00:02'
    port1_to_2 = 2  # Port on switch1 connected to switch2
    port2_to_1 = 1  # Port on switch2 connected to switch1

    # Add flow from host1 to host2
    add_flow_entry(switch1, 'flow_host1_to_host2', host1_mac, host2_mac, port1_to_2)
    add_flow_entry(switch2, 'flow_host1_to_host2_return', host2_mac, host1_mac, port2_to_1)

    # Add flow from host2 to host1
    add_flow_entry(switch2, 'flow_host2_to_host1', host2_mac, host1_mac, port2_to_1)
    add_flow_entry(switch1, 'flow_host2_to_host1_return', host1_mac, host2_mac, port1_to_2)

if __name__ == "__main__":
    main()

