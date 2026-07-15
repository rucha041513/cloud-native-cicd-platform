import os
import zipfile
import boto3
from datetime import datetime, timedelta

# ==========================
# Paths
# ==========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))

LOG_FOLDER = os.path.join(PROJECT_DIR, "logs")

BACKUP_FOLDER = os.path.join(PROJECT_DIR, "archives")

os.makedirs(BACKUP_FOLDER, exist_ok=True)

# ==========================
# AWS S3
# ==========================

BUCKET_NAME = "rucha-devops-project-213348783655"

s3 = boto3.client("s3")

# ==========================
# Create Backup Name
# ==========================

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

zip_filename = f"logs_backup_{timestamp}.zip"

zip_path = os.path.join(BACKUP_FOLDER, zip_filename)

# ==========================
# Compress Logs
# ==========================

print("Compressing logs...")

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:

    for root, dirs, files in os.walk(LOG_FOLDER):

        for file in files:

            file_path = os.path.join(root, file)

            arcname = os.path.relpath(file_path, LOG_FOLDER)

            zipf.write(file_path, arcname)

print("ZIP created:")
print(zip_path)

# ==========================
# Upload to S3
# ==========================

print("Uploading to S3...")

try:

    s3.upload_file(
        zip_path,
        BUCKET_NAME,
        zip_filename
    )

    print("Upload Successful!")

except Exception as e:

    print("Upload Failed")
    print(e)

# ==========================
# Delete Old Backups
# ==========================

print("Checking old backups...")

cutoff = datetime.now() - timedelta(days=7)

for file in os.listdir(BACKUP_FOLDER):

    file_path = os.path.join(BACKUP_FOLDER, file)

    if os.path.isfile(file_path):

        modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))

        if modified_time < cutoff:

            os.remove(file_path)

            print(f"Deleted old backup: {file}")

print("Backup Completed Successfully!")