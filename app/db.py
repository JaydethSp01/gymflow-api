import os
from psycopg import connect

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    conn = connect(DATABASE_URL)
else:
    conn = None  # Use in-memory or mock
