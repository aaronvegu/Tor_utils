import csv
import time

def read_relay_data_from_csv(file_path):
    print('Reading relay data from csv...')
    start_time = time.time()
    relay_data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            relay_data.append(row)
    end_time = time.time()
    print(f"Reading finished.\nTime taken: {end_time - start_time:.4f} seconds")
    return relay_data

def generate_circuit_combinations(relay_data):
    print('Calculate of combinations started...')
    start_time = time.time()
    guard_relay_data = [relay for relay in relay_data if relay['Guard'] == 'Yes']
    middle_relay_data = [relay for relay in relay_data if relay['Middle'] == 'Yes']
    exit_relay_data = [relay for relay in relay_data if relay['Exit'] == 'Yes']

    circuits = []

    for guard in guard_relay_data:
        for middle in middle_relay_data:
            if guard['Fingerprint'] != middle['Fingerprint']:
                for exit in exit_relay_data:
                    circuits.append((guard, middle, exit))
    end_time = time.time()
    print(f"Circuit combinations finished.\nTime taken: {end_time - start_time:.4f} seconds")
    return circuits

def write_circuit_combinations_to_file(circuits, output_file):
    print('Combination writing started...')
    start_time = time.time()
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Guard Fingerprint', 'Middle Fingerprint', 'Exit Fingerprint'])
        for circuit in circuits:
            writer.writerow([
                circuit[0]['Fingerprint'],
                circuit[1]['Fingerprint'],
                circuit[2]['Fingerprint']
            ])
            writer.writerow([
                ' ',
                circuit[1]['Fingerprint'],
                circuit[2]['Fingerprint']
            ])
    end_time = time.time()
    print(f"Combination writing finished.\nTime taken: {end_time - start_time:.4f} seconds")

def main():
    start_time = time.time()
    input_csv_file = 'sample.csv'  # Replace with the path to your input CSV file
    output_csv_file = 'sample_combinations.csv'  # Replace with the desired output CSV file name

    relay_data = read_relay_data_from_csv(input_csv_file)
    circuits = generate_circuit_combinations(relay_data)
    write_circuit_combinations_to_file(circuits, output_csv_file)
    end_time = time.time()
    print(f"Total Time taken: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()