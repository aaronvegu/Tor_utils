import csv
import itertools

def read_relay_data_from_csv(file_path):
    print('Reading relay data from csv...')
    relay_data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            relay_data.append(row)
    print('Reading finished')
    return relay_data

def generate_circuit_combinations(relay_data):
    print('Calculate of combinations started...')
    guard_relay_data = [relay for relay in relay_data if relay['Guard'] == 'Yes' and relay['Middle'] != 'Yes']
    middle_relay_data = [relay for relay in relay_data if relay['Middle'] == 'Yes' and relay['Guard'] != 'Yes']
    exit_relay_data = [relay for relay in relay_data if relay['Exit'] == 'Yes']

    circuits = list(itertools.product(guard_relay_data, middle_relay_data, exit_relay_data))
    print('Circuit combinations finished')
    return circuits

def write_circuit_combinations_to_file(circuits, output_file):
    print('Combination writing started...')
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Guard Fingerprint', 'Guard Address', 'Middle Fingerprint', 'Middle Address', 'Exit Fingerprint', 'Exit Address'])
        for circuit in circuits:
            writer.writerow([
                circuit[0]['Fingerprint'],
                circuit[0]['Address'],
                circuit[1]['Fingerprint'],
                circuit[1]['Address'],
                circuit[2]['Fingerprint'],
                circuit[2]['Address'],
            ])
    print('Combination writing finished...')

def main():
    input_csv_file = 'relay_data.csv'  # Replace with the path to your input CSV file
    output_csv_file = 'circuit_combinations.csv'  # Replace with the desired output CSV file name

    relay_data = read_relay_data_from_csv(input_csv_file)
    circuits = generate_circuit_combinations(relay_data)
    write_circuit_combinations_to_file(circuits, output_csv_file)

if __name__ == "__main__":
    main()
