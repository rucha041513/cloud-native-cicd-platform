import boto3
import json

client = boto3.client(
    "secretsmanager",
    region_name="eu-north-1"
)

response = client.get_secret_value(
    SecretId="flask-db-password"
)

secret = json.loads(response["SecretString"])

print("DB_PASSWORD:", secret["DB_PASSWORD"])