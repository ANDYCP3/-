met_data = read_met_file("20230723.met")

for i, record in enumerate(met_data[:5], 1):
    print(f"Record {i} | ERROR: {record['ERROR']} | VELOCITY: {record['VELOCITY']}")
    print(f"  SNR: {record['SNR']}")
    print(f"  POWER: {record['POWER']}")
