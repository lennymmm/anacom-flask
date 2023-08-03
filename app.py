from flask import Flask, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

@app.route('/')
def index():
    # Carga las credenciales desde el archivo JSON
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('p1lennymmm-ed1135c4b7d8.json', scope)

    # Autentica y abre la hoja de cálculo
    client = gspread.authorize(creds)

    spreadsheet_id = "1fpS5_fJ9CSXH37tW9xLU2FXy89lZ-mHX0HMKP1YPIuE" 
    sheet = client.open_by_key(spreadsheet_id)

    # Trabajar con la hoja de cálculo
    worksheet = sheet.get_worksheet(0)

    # Lee los datos de la hoja de cálculo
    data = worksheet.get_all_records() 

    # Obtén la hoja de destino
    worksheet_dest = sheet.get_worksheet(5)

    # Escribe los datos en la hoja de destino
    for row in data:
        worksheet_dest.append_row(list(row.values()))

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)