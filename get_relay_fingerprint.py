from stem import CircStatus
from stem.descriptor.remote import DescriptorDownloader
from stem.util import str_tools

relay_fingerprint = None

# Download relay descriptors
downloader = DescriptorDownloader()
descriptors = downloader.get_server_descriptors()

# Find the descriptor for your relay
for desc in descriptors:
    if str_tools.compare_caseless(desc.address, '10.12.223.92') and desc.or_port == 9001:
        relay_fingerprint = desc.fingerprint
        break

# Print or use the relay fingerprint
print("Relay Fingerprint: {}".format(relay_fingerprint))
