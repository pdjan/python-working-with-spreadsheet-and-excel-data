# LinkedIn Learning Course
# Example file for Python: Working with Excel and Spreadsheet Data by Joe Marini

# Čitanje CSV fajla u niz

# uvoz csv modula iz standardne biblioteke
import csv


def read_csv_to_array(filename):
    # definiši niz koji će sadržavati podatke
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

# učitaj podatke u niz nizova inventory_data
inventory_data = read_csv_to_array("Inventory.csv")

# svaki red u nizu je niz vrednosti
print(f"Items: {len(inventory_data)}")
print(inventory_data[0])  # Ovo će odštampati prvi red (header)
print(inventory_data[1])  # Ovo će odštampati prvi red sa vrednostima
# Sledeći kod će odštampati ime i broj prve stavke
print(inventory_data[1][0], inventory_data[1][2])
