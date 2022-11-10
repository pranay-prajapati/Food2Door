import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


class DatabaseConfig:
    username = os.environ.get('PG_USER')
    password = os.environ.get('PG_PASSWORD')
    host = os.environ.get('PG_HOST')
    port = os.environ.get('PG_PORT', 5432)
    database_name = os.environ.get('PG_NAME')
    charset = os.environ.get("PG_CHARSET", "utf8")
    pool_size = os.environ.get("PG_POOLSIZE", 5)
    mongodb_name = os.environ.get('MONGODB_NAME')
    mongodb_port = os.environ.get('MONGODB_PORT', 27017)

    if not host:
        print(f"Database Host is not found")
    if not username:
        print(f"Database User is not found")
    if not password:
        print(f"Database Password is not found")
