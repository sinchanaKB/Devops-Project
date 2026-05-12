from flask import Flask, jsonify
import pyodbc
import os

app = Flask(__name__)

# To connect from a Linux Docker container, this gets overridden by docker-compose.yml to 'host.docker.internal'.
# When running locally on Windows, it defaults to your actual server name!
DB_SERVER = os.environ.get('DB_SERVER', r'host.docker.internal,1433')
DB_NAME = os.environ.get('DB_NAME', 'bus_system')

def get_db_connection():
    import os

    db_server = os.environ.get('DB_SERVER')
    db_name = os.environ.get('DB_NAME', 'bus_system')
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')

    print("DEBUG DB_SERVER:", db_server)  # optional

    if db_user and db_pass:
        conn_str = f'''
        DRIVER={{ODBC Driver 17 for SQL Server}};
        SERVER=host.docker.internal;
        DATABASE=bus_system;
        UID=sa;
        PWD=StrongPassword@123;
        TrustServerCertificate=yes;
        '''
    else:
        conn_str = f'''
        DRIVER={{ODBC Driver 17 for SQL Server}};
        SERVER={db_server};
        DATABASE={db_name};
        Trusted_Connection=yes;
        '''

    return pyodbc.connect(conn_str)

@app.route('/')
def home():
    return "SQL Server Reader App is Running! Visit http://localhost:5000/buses to view data."

@app.route('/buses')
def get_buses():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Execute the read operation on your new table[cite: 1]
        cursor.execute("SELECT * FROM Buses")
        
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return jsonify({"status": "success", "data": data})
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Binds to 0.0.0.0 so Docker can map it outwards to localhost
    app.run(host='0.0.0.0', port=5000)
