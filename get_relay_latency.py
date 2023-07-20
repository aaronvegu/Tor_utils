import time
import stem
from stem import Flag
from stem.control import Controller

# File to store latency data
latency_file = "latency_data.txt"

with Controller.from_port(port=9051) as controller:
    controller.authenticate()  # Authenticate with the control port

    # Get the relay descriptors
    relay_descriptors = controller.get_router_statuses()

    # Find your relay and retrieve the latency information
    for descriptor in relay_descriptors.values():
        if descriptor.fingerprint == 'BD304969C6CF695599FA8F079ED7576FEE7F9D30':
            relay = descriptor
            break
    else:
        raise ValueError("Your relay was not found.")

    # Get current timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Store the latency data with timestamp in a file
    with open(latency_file, "a") as file:
        file.write(f"{timestamp}: {relay.average_rtt}\n")
