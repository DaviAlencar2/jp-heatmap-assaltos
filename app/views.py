from app.main import app
from flask import render_template,url_for,jsonify,request,redirect
from data.dados import porcentagem_bairros,data_com_mais_assaltos,data,carregar_dados_por_ano,data_adicionar_assalto,csv_to_dataframe

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/estatisticas')
def estatisticas():
    return render_template("estatisticas.html", porcentagem_bairros=porcentagem_bairros(), dicionario_fatiado=data_com_mais_assaltos())

@app.route('/adicionar_assalto', methods=['GET', 'POST'])
def adicionar_assalto():
    if request.method == 'POST':
        data_adicionar_assalto(request.form['bairro'],request.form['latitude'],request.form['longitude'],request.form['data'])
        return redirect(url_for('home'))
    return render_template("adicionar_assalto.html")

@app.route('/dados_json')
def dados_json():
    dados_json = data[['Latitude', 'Longitude', 'Bairro']].to_dict(orient='records')
    return jsonify(dados_json)

@app.route('/dados/<int:ano>')
def ano(ano):
    return jsonify(carregar_dados_por_ano(ano))