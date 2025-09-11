from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)
 
# MySQL configuration
db_config = {
    'host': 'tp4-sql',
    'user': 'root',
    'password': 'foo',
    'database': 'demosql'
}
@app.route('/')
def index():
    try:
        # Connexion MySQL à chaque requête
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        query = "SELECT * FROM myTable"
        cursor.execute(query)
        data = cursor.fetchall()
    
    except Error as e:
        print("Erreur MySQL :", e)
        return "Erreur interne", 500

    finally:
        cursor.close()
        conn.close()
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # important pour Docker

