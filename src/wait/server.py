
from fastmcp import FastMCP
import asyncio
import pyodbc
from azure.identity import ClientSecretCredential

import os
import json
from dotenv import load_dotenv

load_dotenv()

app = FastMCP("mpl_mcp_datatools")

notes = {}


@app.tool("fetch-budget-for-file")
async def fetch_budget_for_file(fileId: str):
    # SQL auth credentials from environment variables
    sql_server = os.environ["SQL_SERVER"]  # e.g. 'myserver.database.windows.net'
    sql_database = os.environ["SQL_DATABASE"]
    sql_username = os.environ["SQL_USERNAME"]
    sql_password = os.environ["SQL_PASSWORD"]
    sql_query = "SELECT * FROM [Manuport Logistics NV$LQS Budget Service$a766ef34-2c2a-4e7f-bc3f-99c51d0e90cd] WHERE [Order No_] = ?"  # Change table/query as needed

    # Build ODBC connection string for SQL auth
    conn_str = (
        f"Driver={{ODBC Driver 18 for SQL Server}};"
        f"Server={sql_server};"
        f"Database={sql_database};"
        f"UID={sql_username};"
        f"PWD={sql_password};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=yes;"
    )

    # Connect and execute query
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_query, fileId)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        result = []
        for row in rows:
            row_dict = {}
            for col, val in zip(columns, row):
                if isinstance(val, bytes):
                    row_dict[col] = val.hex()
                elif hasattr(val, 'isoformat'):
                    row_dict[col] = val.isoformat()
                else:
                    row_dict[col] = val
            result.append(row_dict)
    return result

if __name__ == "__main__":
    app.run(transport="sse", host="0.0.0.0", port=8000)