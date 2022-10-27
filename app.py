# Importando biblioteca Flask
from flask import Flask, render_template, request

# Importando biblioteca Sqlite3
import sqlite3

# Criar banco de dados
db = sqlite3.connect('APP_DB1.db')

cursor = db.cursor()

# Função senha banco de dados
def valida_senha(dre, senha):

    conn = sqlite3.connect('APP_DB1.db') 
    c = conn.cursor()
    j = c.execute("SELECT * FROM cadastrados where dre = '"+dre+"' and senha ='"+senha+"'").fetchall()
                         
    conn.commit()
    
    print(j)
    
    if j:
        return render_template("calculapf.html")
    else:
        return render_template("index.html", erro="Login Incorreto")

# Criar o site
app = Flask(__name__)

# Criar a primeira página do site - LOGIN
@app.route("/login", methods =["POST"])
def login():

    if request.method == "POST":
        dre = request.form["dre"]
        senha = request.form["senha"]
        return valida_senha(dre,senha)

    else:
        print ("Deu ruim")
        return "RUIM"

# Criar a segunda página do site - CADASTRO
@app.route("/cadastro")
def cadastro():
    return "Faça seu cadastro"

# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)