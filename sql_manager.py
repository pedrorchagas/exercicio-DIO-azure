import pymssql
from dotenv import load_dotenv
import os

load_dotenv()

SERVER = os.getenv("DATABASE_HOST")



database = pymssql.connect(server=SERVER, user=os.getenv("DATABASE_USERNAME"), password=os.getenv("DATABASE_PASSWORD"))

cursor = database.cursor()
cursor.execute(
    """
        CREATE TABLE [dbo].[products] (
            [Id]                  INT  IDENTITY (1, 1) NOT NULL,
            [product_name]        TEXT NULL,
            [product_image_link]  TEXT NULL,
            [product_ingredients] TEXT NULL,
            [product_slices]      INT  NULL,
            CONSTRAINT [PK_products] PRIMARY KEY CLUSTERED ([Id] ASC)
        );

    """
)

