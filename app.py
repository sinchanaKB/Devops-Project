from flask import Flask, jsonify
import pyodbc
import os

app = Flask(__name__)

# Read environment variables
DB_SERVER = os.environ.get('DB_SERVER', 'host.docker.internal,1433')
DB_NAME = os.environ.get('DB_NAME', 'bus_system')
DB_USER = os.environ.get('DB_USER', 'sa')
DB_PASS = os.environ.get('DB_PASS', 'StrongPassword@123')


def get_db_connection():

    print("DEBUG DB_SERVER:", DB_SERVER)
    print("DEBUG DB_NAME:", DB_NAME)

    conn_str = f'''
    DRIVER={{ODBC Driver 17 for SQL Server}};
    SERVER={DB_SERVER};
    DATABASE={DB_NAME};
    UID={DB_USER};
    PWD={DB_PASS};
    TrustServerCertificate=yes;
    '''

    return pyodbc.connect(conn_str, timeout=30)


@app.route('/')
def home():
    return '''
    <h2>SQL Server Reader App is Running!</h2>
    <p>Visit <a href="/buses">/buses</a> to view bus data.</p>
    '''


@app.route('/buses')
def get_buses():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Fetch all rows from Buses table
        cursor.execute("SELECT * FROM Buses")

        columns = [column[0] for column in cursor.description]

        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(columns, row)))

        cursor.close()
        conn.close()

        return jsonify({
            "status": "success",
            "data": data
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
