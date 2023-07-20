
import csv
import stem
from stem.descriptor.remote import DescriptorDownloader
from datetime import datetime
import geoip2.database

def download_consensus():
    downloader = DescriptorDownloader()
    try:
        consensus = downloader.get_consensus()
        return consensus
    except stem.DescriptorUnavailable as e:
        print(f"Unable to download network consensus: {str(e)}")
        return None

consensus = download_consensus()

def get_country_code(ip_address):
    reader = geoip2.database.Reader('GeoLite2-Country.mmdb')
    try:
        response = reader.country(ip_address)
        return response.country.iso_code
    except geoip2.errors.AddressNotFoundError:
        return None

def write_to_csv(consensus):
    if consensus:
        fieldnames = ['Address', 'CountryCode', 'Nickname', 'Fingerprint', 'Bandwidth', 'Flags']
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        file_name = f"relay_data_{timestamp}.csv"

        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for relay in consensus:
                country_code = get_country_code(relay.address)
                relay_info = {
                    'Address': relay.address,
                    'CountryCode': country_code,
                    'Nickname': relay.nickname,
                    'Fingerprint': relay.fingerprint,
                    'Bandwidth': relay.bandwidth,
                    'Flags': ' '.join(relay.flags[:]) if relay.flags else ''
                }
                writer.writerow(relay_info)

write_to_csv(consensus)
