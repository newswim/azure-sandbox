import os
import uuid

import dotenv

from azure.storage.blob import (
    BlobServiceClient,
    BlobClient,
    ContainerClient,
    __version__,
)

if __name__ == "__main__":
    dotenv.load_dotenv()

    connection_str = os.getenv("connection_str")

    blob_service_client: BlobServiceClient = BlobServiceClient.from_connection_string(
        connection_str
    )

    container_name = "dans-blob-experiment"

    #### only needed when first creating the container
    # container_client = blob_service_client.create_container(container_name)

    container = blob_service_client.get_container_client(container_name)

    with open("./example.txt", "rb") as data:
        container.upload_blob(name="my_cool_example.txt", data=data)
