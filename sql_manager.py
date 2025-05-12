import pymssql
from dotenv import load_dotenv
import os

load_dotenv()

def open_connection():
    database = pymssql.connect(server=SERVER, user=os.getenv("DATABASE_USERNAME"), password=os.getenv("DATABASE_PASSWORD"), database=os.getenv("DATABASE_DB"))
    return database

def insert_product(product_name, product_image_link, product_ingredients, product_slices):
    database = open_connection()
    cursor = database.cursor()
    cursor.execute(
        """
            INSERT INTO dbo.products (product_name, product_image_link, product_ingredients, product_slices)
            VALUES (%s, %s, %s, %s)
        """,
        (product_name, product_image_link, product_ingredients, product_slices)
    )
    database.commit()
    cursor.close()

def get_products():
    database = open_connection()
    cursor = database.cursor()
    cursor.execute(
        """
            SELECT * FROM products
        """
    )
    rows = cursor.fetchall()
    products = []
    for row in rows:
        product = {
            "product_id": row[0],
            "product_name": row[1],
            "product_image_link": row[2],
            "product_ingredients": row[3],
            "product_slices": row[4]
        }
        products.append(product)
    cursor.close()
    return products

def delete_product(product_id):
    database = open_connection()
    cursor = database.cursor()
    cursor.execute(
        """
            DELETE FROM products WHERE product_id = %s
        """,
        (product_id,)
    )
    database.commit()
    cursor.close()
