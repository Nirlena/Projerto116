# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Isaac" # escreva seu nome
    idade = "13" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai

@app.route("/pai")
def meu_pai():

    nome = "José" # escreva seu nome
    idade = "40" # escreva sua idade

    return render_template('pai.html' , nome = nome , idade = idade)

# defina a rota para a página da mãe

@app.route("/mae")
def minha_mae():

    nome = "Nirlena" # escreva seu nome
    idade = "43" # escreva sua idade

    return render_template('mae.html' , nome = nome , idade = idade)

# defina a rota para a página do amigo

@app.route("/amigo")
def meu_amigo():

    nome = "Augusto" # escreva seu nome
    idade = "20" # escreva sua idade

    return render_template('amigo.html' , nome = nome , idade = idade)

# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
