from google.cloud import storage

bucket_name = "austin-transfer-test"
source_file_name = "/Users/amccracken/workspace/cloud-run-python-demo/test.xlsx"
destination_blob_name = "test-file"

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    bucket_name = "austin-transfer-test"
    
    # The path to your file to upload
    source_file_name = "/Users/amccracken/workspace/cloud-run-python-demo/test.xlsx"
    
    # The ID of your GCS object
    destination_blob_name = "test-file"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

upload_blob(bucket_name, source_file_name, destination_blob_name)