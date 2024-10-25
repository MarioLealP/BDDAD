import csv

def generate_oracle_inserts(csv_file, table_name):
    with open(csv_file, mode='r') as file:
        # Read the CSV file
        csv_reader = csv.reader(file)
        
        # Skip the header row
        next(csv_reader)
        
        # Loop through the rows and generate the INSERT statements
        for row in csv_reader:
            pfid = row[0]
            name = row[1]
            
            # Create the INSERT SQL statement
            insert_statement = f"INSERT INTO {table_name} (Code, Name) VALUES ('{pfid}', '{name}');"
            print(insert_statement)

# Example usage
csv_file = 'path_to_your_csv.csv'  # Replace with the path to your CSV file
table_name = 'ProductFamily'  # Replace with your table name

generate_oracle_inserts(csv_file, table_name)
