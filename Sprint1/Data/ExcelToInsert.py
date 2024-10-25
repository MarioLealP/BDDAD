import pandas as pd
import random
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def excelToInsert(excel_file, insert_file):
    if not os.path.exists(excel_file):
        logging.error("Excel file does not exist: %s", excel_file)
        return

    try:
        # Read the Excel file
        xls = pd.ExcelFile(excel_file, engine='openpyxl')
        
        sql_statements = []
        used_ids = set()  # Set to keep track of used Address IDs

        # Insert predefined customer types into the CostumerType table
        sql_statements.append("INSERT INTO CostumerType (Type) VALUES ('Individual');")
        sql_statements.append("INSERT INTO CostumerType (Type) VALUES ('Company');")

        # Process each sheet; ensure the sheet names match your Excel file
        sql_statements.extend(generate_insert_clients(xls.parse("Clients"), used_ids))
        sql_statements.extend(generate_insert_productFamily(xls.parse("ProductFamily")))
        sql_statements.extend(generate_insert_product(xls.parse("Products")))
        sql_statements.extend(generate_insert_workstationType(xls.parse("WorkstationTypes")))
        sql_statements.extend(generate_insert_workstation(xls.parse("Workstations")))
        sql_statements.extend(generate_insert_operations(xls.parse("Operations")))
        sql_statements.extend(generate_insert_orders(xls.parse("Orders")))
        sql_statements.extend(generate_insert_boo(xls.parse("BOO")))
        sql_statements.extend(generate_insert_bom(xls.parse("BOM")))

        # Write the SQL statements to a file with utf-8 encoding
        with open(insert_file, 'w', encoding='utf-8') as f:
            for statement in sql_statements:
                f.write(statement + '\n')

        
        logging.info("SQL statements successfully written to %s", insert_file)

    except Exception as e:
        logging.error("Error processing Excel file: %s", e)

def generate_random_id(used_ids):
    while True:
        # Generate a random Address ID between 1 and 99999
        random_id = random.randint(1, 99999)
        if random_id not in used_ids:
            used_ids.add(random_id)
            return f"{random_id:05d}"  # Format to always have 5 digits

def generate_insert_clients(df, used_ids):
    sql_statements = []
    
    # Iterate through each row in the DataFrame to generate INSERT statements
    for index, row in df.iterrows():
        # Insert into Address table
        street_name = row['Addess']
        post_code = row['ZIP']
        town = row['Town']
        country_code = row['Country'][:2].upper()  # Taking the first two letters of the country
        
        # Generate a unique Address ID
        address_id = generate_random_id(used_ids)

        insert_country = f"INSERT INTO Country (Code, Name) VALUES ('{country_code}', '{row['Country']}');"

        sql_statements.append(insert_country)

        insert_address = f"INSERT INTO Address (ID, Street, PostCode, Town, CountryCode) " \
                         f"VALUES ('{address_id}', '{street_name}', '{post_code}', '{town}', '{country_code}');"
        
        sql_statements.append(insert_address)

        # Clean the phone number
        contact = str(row['Phone']).replace('+', '').replace('-', '').replace(' ', '')
        name = row['Name']
        
        # Use CostumerID directly from the CSV
        costumer_id = row['IDClient']  # Assuming 'IDClient' column has the Costumer ID

        insert_costumer = f"INSERT INTO Costumer (ID, Name, Contact, AddressID, CostumerType) " \
                          f"VALUES ('{costumer_id}', '{name}', {contact}, {address_id}, 'Company');"
        sql_statements.append(insert_costumer)

    return sql_statements

def generate_insert_productFamily(df):
    sql_statements = []
    for index, row in df.iterrows():
        product_family_id = row['PFID']
        product_family_name = row['Name']
        insert_product_family = f"INSERT INTO ProductFamily (Code, Name) VALUES ('{product_family_id}', '{product_family_name}');"
        sql_statements.append(insert_product_family)
    return sql_statements

def generate_insert_product(df):
    sql_statements = []
    for index, row in df.iterrows():
        product_id = row['Code']
        product_name = row['Name']
        product_description = row['Description']
        product_family_id = row['Family']
        insert_product = f"INSERT INTO Product (Code, Name, Description, ProductFamilyCode) VALUES ('{product_id}', '{product_name}', '{product_description}', {product_family_id});"
        sql_statements.append(insert_product)
    return sql_statements

def generate_insert_workstationType(df):
    sql_statements = []
    for index, row in df.iterrows():
        workstation_type_id = row['WTID']
        workstation_type_name = row['Name']
        insert_workstationType = f"INSERT INTO WorkstationType (Code, Name) VALUES ('{workstation_type_id}', '{workstation_type_name}');"
        sql_statements.append(insert_workstationType)

    return sql_statements

def generate_insert_workstation(df):
    sql_statements = []
    for index, row in df.iterrows():
        workstation_id = row['WSID']
        workstation_type_id = row['WTID']
        workstation_name = row['Name']
        workstation_description = row['Description']
        insert_workstation = f"INSERT INTO Workstation (ID, Name, Description, WorkstationTypeCode) VALUES ('{workstation_id}', '{workstation_name}', '{workstation_description}', '{workstation_type_id}');"
        sql_statements.append(insert_workstation)

    return sql_statements

def generate_insert_operations(df):
    sql_statements = []
    for index, row in df.iterrows():
        operation_id = row['OPID']
        operation_description = row['Description']
        insert_operation = f"INSERT INTO Operation (ID, Name) VALUES ('{operation_id}', '{operation_description}');"
        sql_statements.append(insert_operation)

        for col in df.columns:
            if 'WorkstationType' in col:  # Check if the column name contains 'WorkstationType'
                workstation_type_id = row[col]
                if pd.notna(workstation_type_id):  # Check if the value is not NaN
                    insert_workstation_type_operation = (
                        f"INSERT INTO WorkstationTypeOperation (WorkstationTypeCode, OperationID) "
                        f"VALUES ('{workstation_type_id}', '{operation_id}');"
                    )
                    sql_statements.append(insert_workstation_type_operation)
    return sql_statements

def generate_insert_orders(df):
    sql_statements = []
    for index, row in df.iterrows():
        order_id = row["OID"]
        order_deliveryDate = row["DateDelivery"]
        order_orderDate = row["DateOrder"]
        order_clientID = row["Client"]

        insert_order = f"INSERT INTO CostumerOrder (ID, DeliveryDate, OrderDate, CostumerID) VALUES ('{order_id}', TO_DATE('{order_deliveryDate}', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('{order_orderDate}', 'YYYY-MM-DD HH24:MI:SS'), {order_clientID});"
         
        sql_statements.append(insert_order)
        order_productId = row["Product"]
        order_quantity = row["Quantity"]

        insert_order_product = f"INSERT INTO ProductOrder (OrderID, ProductCode, Quantity) VALUES ('{order_id}', '{order_productId}', '{order_quantity}');"
        sql_statements.append(insert_order_product)
    
    return sql_statements

def generate_insert_boo(df):
    sql_statements = []
    for index, row in df.iterrows():
        boo_familyid = row['FamilyID']
        boo_operationid = row['OPID']
        boo_operationStep = row['OPNumber']

        insert_boo = f"INSERT INTO BoO (Step, ProductFamilyCode, OperationID) VALUES ('{boo_operationStep}', '{boo_familyid}', '{boo_operationid}');"
        sql_statements.append(insert_boo)
    return sql_statements

def generate_insert_bom(df):
    sql_statements = []
    for index, row in df.iterrows():
        bom_productid = row['ProductID']
        bom_componentid = row['PartNumber']
        bom_descriotion = row['Description']
        bom_quantity = row['Quantity']

        insert_component = f"INSERT INTO Component (Code, Description) VALUES ('{bom_componentid}', '{bom_descriotion}');"
        sql_statements.append(insert_component)

        insert_bom = f"INSERT INTO BoM (ProductCode, ComponentCode, Quantity) VALUES ('{bom_productid}', '{bom_componentid}', '{bom_quantity}');"

        sql_statements.append(insert_bom)
    return sql_statements


# Usage
excel_file = 'Dataset02_v2.xlsx'  # Path to the Excel file
insert_file = 'Inserts.sql'  # Path to the output file for SQL insert statements

# Call the function
excelToInsert(excel_file, insert_file)
