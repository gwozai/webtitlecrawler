# config.py
from dotenv import load_dotenv
import os

load_dotenv()

MINIO_CONFIG = {
    "endpoint": os.getenv("MINIO_ENDPOINT"),
    "access_key": os.getenv("MINIO_ACCESS_KEY"),
    "secret_key": os.getenv("MINIO_SECRET_KEY"),
    "bucket": os.getenv("MINIO_Bucket"),

    "secure": os.getenv("MINIO_SECURE") in ["True", "true", "yes", "1"]

}

MYSQL_CONFIG = {
    "host": os.getenv("MYSQL_HOST"),
    "dbname": os.getenv("MYSQL_DBNAME"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD")
}

REDIS_CONFIG = {
    "host": os.getenv("REDIS_HOST"),
    "port": int(os.getenv("REDIS_PORT")),
    "dbid": int(os.getenv("REDIS_DBID")),
    "password": os.getenv("REDIS_PASSWORD")
}