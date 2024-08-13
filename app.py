from flask import Flask, redirect, render_template, request, url_for
import pypyodbc as odbc

app =Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html') 

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    # Connect to the database
    connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:finanacedata.database.windows.net,1433;Database=findata;Uid=jaya;Pwd={Krishna@2244};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
    cursor.execute("INSERT INTO login (email, password) VALUES (?, ?)", (email, password))

    conn.commit()
    cursor.close()
    conn.close()   
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)