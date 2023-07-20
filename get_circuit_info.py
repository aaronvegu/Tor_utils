import stem.control

# Connect to the Tor control port
with stem.control.Controller.from_port(port=9051) as controller:
    controller.authenticate('password')  # Authenticate with the Tor client
    circuit_info = controller.get_circuits()  # Retrieve circuit information

    # Process circuit information
    for circuit in circuit_info:
        # Extract relevant circuit details
        # (such as fingerprint, IP address, role, etc.)
        # based on your specific requirements
        print(circuit)
