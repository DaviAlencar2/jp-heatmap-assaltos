from app.main import app
from flask import render_template,url_for,jsonify,request,redirect
from data.dados import porcentagem_bairros,data_com_mais_assaltos,data,carregar_dados_por_ano,data_adicionar_assalto,csv_to_dataframe
from geocode.geocode import geocode_address

API_KEY = "SUA_CHAVE_GOOGLE_API"

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/estatisticas')
def estatisticas():
    return render_template("estatisticas.html", porcentagem_bairros=porcentagem_bairros(), dicionario_fatiado=data_com_mais_assaltos())

@app.route('/adicionar_assalto', methods=['GET', 'POST'])
def adicionar_assalto():
    from geocode import geocode_address  # Importe a função
API_KEY = "YOUR_GOOGLE_API_KEY"

@app.route('/adicionar_assalto', methods=['GET', 'POST'])
def adicionar_assalto():
    if request.method == 'POST':
        bairro = request.form['bairro']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        data_extenso = request.form['data']

        # Se latitude e longitude não forem fornecidos, tenta geocodificar
        if not latitude or not longitude:
            latitude, longitude = geocode_address(bairro, API_KEY)

        if latitude and longitude:
            data_adicionar_assalto(bairro, latitude, longitude, data_extenso)
            return redirect(url_for('home'))
        else:
            return "Erro: Não foi possível determinar as coordenadas do endereço.", 400
    return render_template("adicionar_assalto.html")

@app.route('/dados_json')
def dados_json():
    dados_json = data[['Latitude', 'Longitude', 'Bairro']].to_dict(orient='records')
    return jsonify(dados_json)

@app.route('/dados/<int:ano>')
def ano(ano):
    return jsonify(carregar_dados_por_ano(ano))