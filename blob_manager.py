from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

load_dotenv()

connection_string = os.getenv("BLOB_CONNECTION_STRING")

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container = blob_service_client.get_container_client(container="fotos")
blob = container.list_blobs()
for i in blob:
    print(i.values())

#def get_product_image(product_name):
#    blob = container.get_blob_client(bl)
