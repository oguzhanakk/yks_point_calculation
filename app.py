from flask import Flask, request, jsonify
from score_calculation import PuanHesaplari

app = Flask(__name__)

@app.route('/puan_hesapla', methods=['POST'])
def puan_hesapla():
    data = request.get_json()
    obp = data['obp']
    tr_net = data.get('tr_net', 0)
    sosyal_net = data.get('sosyal_net', 0)
    mat1_net = data.get('mat1_net', 0)
    fen_net = data.get('fen_net', 0)
    
    mat2_net = data.get('mat2_net', 0)
    fizik_net = data.get('fizik_net', 0)
    kimya_net = data.get('kimya_net', 0)
    biyo_net = data.get('biyo_net', 0)
    edb_net = data.get('edb_net', 0)
    tarih1_net = data.get('tarih1_net', 0)
    cog1_net = data.get('cog1_net', 0)
    tarih2_net = data.get('tarih2_net', 0)
    cog2_net = data.get('cog2_net', 0)
    felsefe_net = data.get('felsefe_net', 0)
    din_net = data.get('din_net', 0)
    
    dil_net = data.get('dil_net', 0)

    hesapla = PuanHesaplari(obp, tr_net, sosyal_net, mat1_net, fen_net, mat2_net, fizik_net, kimya_net, biyo_net,
                            edb_net, tarih1_net, cog1_net, tarih2_net, cog2_net, felsefe_net, din_net, dil_net)

    try:
        hesapla.validate_inputs()
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    tyt_ham, tyt_yer = hesapla.tyt_puan_hesapla()
    say_ham, say_yer = hesapla.say_puan_hesapla()
    ea_ham, ea_yer = hesapla.e_agirlik_puan_hesapla()
    sozel_ham, sozel_yer = hesapla.sozel_puan_hesapla()
    dil_ham, dil_yer = hesapla.dil_puan_hesapla()

    result = {
        'tyt_ham': tyt_ham,
        'tyt_yer': tyt_yer,
        'say_ham': say_ham,
        'say_yer': say_yer,
        'ea_ham': ea_ham,
        'ea_yer': ea_yer,
        'sozel_ham': sozel_ham,
        'sozel_yer': sozel_yer,
        'dil_ham': dil_ham,
        'dil_yer': dil_yer
    }

    return jsonify(result)

@app.route('/')
def home():
    return 'Succesfuly'

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)