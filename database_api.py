from flask import Flask, request, send_from_directory, make_response
from flask_restful import Resource, Api
import database
import os

app = Flask(__name__)
        
@app.route('/database/<string:data_type>', methods=['GET'])
def get(data_type):
    if data_type == 'oxygen':
        return database.getO2data()
    elif data_type == 'bp':
        return database.getBPdata()
    elif data_type == 'pulse':
        return database.getPulsedata()
    else:
        return 'invalid data type'

@app.route('/store_data', methods=['GET'])
def put():
    if str(request.form['name']) == 'oxygen':
        return database.storeO2data(request.form['values'])
    elif str(request.form['name']) == 'bp':
        return database.storeBPdata(request.form['values'])
    elif str(request.form['name']) == 'pulse':
        return database.storePulsedata(request.form['values'])
    else:
        return 'store data failed'
    
@app.route('/get_wholedata/<string:filename>', methods=['GET'])
def get_data(filename):
    try:
         with open(os.path.join('', filename)) as f:
             s=f.read()
             f.close()
         return str(s)

    except Exception as e:
        print('----------------')
        return e

if __name__ == '__main__':
    database.createO2table()
    database.createBPtable()
    database.createPulsetable()
    app.run(debug=True)