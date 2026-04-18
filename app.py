from flask import Flask, request, jsonify
import subprocess
import sqlite3

app = Flask(__name__)

# !! ATTENTION : Ce code contient des vulnérabilités intentionnelles !!
# Elles seront détectées par nos outils de scan.

@app.route('/ping')
def ping():
    # Vulnérabilité 1 : Injection de commande
    host = request.args.get('host')
    result = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return result

@app.route('/user/<int:user_id>')
def get_user(user_id):
    # Vulnérabilité 2 : Injection SQL
    conn = sqlite3.connect('example.db')
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor = conn.execute(query)
    user = cursor.fetchone()
    conn.close()
    return jsonify(user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
