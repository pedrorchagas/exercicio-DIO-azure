from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os
import uuid

load_dotenv()

connection_string = os.getenv("BLOB_CONNECTION_STRING")
ACCOUNT_NAME = "exerciciolabdio"


blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container = blob_service_client.get_container_client(container="fotos")


#def get_product_image(product_name):
#    blob = container.get_blob_client(bl)


def upload_image(file):
    blob_name = f"{uuid.uuid4()}.jpeg"
    blob_client = container.get_blob_client(blob_name)  
    blob_client.upload_blob(file.read(), overwrite=True)
    image_url = f"https://{ACCOUNT_NAME}.blob.core.windows.net/fotos/{blob_name}"
    return image_url

