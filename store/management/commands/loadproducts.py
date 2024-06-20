from django.core.management.base import BaseCommand
from django.conf import settings
import pandas as pd
import sqlite3
from random import uniform


class Command(BaseCommand):
    def insert_into_table(table_name, column_names, values, db_path):
        db_path = settings.BASE_DIR / 'db.sqlite3'

        try:
            # Connect to the SQLite3 database
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()

            # clear the table if data exists
            qry = "delete from products_subcategory"
            cursor.execute(qry)
            connection.commit()

            # insert
            columns = ', '.join(column_names)
            placeholders = ', '.join(['?'] * len(column_names))
            insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            cursor.executemany(insert_query, values)
            connection.commit()

            print(f"{cursor.rowcount} rows were inserted into {table_name}.")

        except sqlite3.Error as e:
            print(f"Error: {e}")
            print("Make sure you run `python manage.py migrate` first")
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("SQLite connection is closed")


    def handle(self, *args, **options):
        # get product data
        datafile = settings.BASE_DIR / "products.csv"
        df = pd.read_csv(datafile)

        # add misc subcategories for missing values
        for i, row in df.iterrows():
            if type(df.loc[i, "subcategory"]) == float:
                df.loc[i, "subcategory"] = "Misc " + df.loc[i, "category"]
        
        # create categories, subcatgories and products dataframes
        categories = df[['category']].drop_duplicates().reset_index(drop=True)
        categories['category_id'] = categories.index + 1
        subcategories = df[['subcategory', 'category']].drop_duplicates().reset_index(drop=True)
        subcategories = subcategories.merge(categories, on='category')
        subcategories = subcategories[['subcategory', 'category_id']]
        subcategories['subcategory_id'] = subcategories.index + 1
        products = df.merge(subcategories, on='subcategory')
        products = products[['product_name', 'price', 'subcategory_id']]
        products['product_id'] = products.index + 1
        # add randomly generated cost price to products
        products["price"] = products["price"].str.replace(',','')
        products["price"] = products["price"].astype(float)
        products["cost_price"] = round(products["price"].apply(lambda x: x * (1 - uniform(0.03, 0.08))), 2)
        # insert data into database
        self.insert_into_table("customers_region", ["region_name"], [["East"], ["West"], ["North"], ["South"], ["Central"]])
        self.insert_into_table("products_category", ["category_name", "id"], categories.values.tolist())
        self.insert_into_table("products_subcategory", ["subcategory_name", "category_id", "id"], subcategories.values.tolist())
        self.insert_into_table("products_product", ["product_name", "selling_price", "subcategory_id", "id", "cost_price"], products.values.tolist())

        print("Data successfully loaded")


