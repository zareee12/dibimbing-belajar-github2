import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter='\t')
        for row in csv_reader:
            data.append(row)
    return data

# Contoh penggunaan fungsi
file_path = "C:\Reza\dibimbing\Batch4\GIT2\dibimbing-belajar-github2\file.csv"
csv_data = read_csv_file(file_path)
for row in csv_data:
    print(row)
