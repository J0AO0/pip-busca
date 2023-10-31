import mysql.connector
import openpyxl

conn = mysql.connector.connect(
    host='192.168.**.***',
    user='root',
    password='*************',
    database='********'
)

cursor = conn.cursor()

consulta = "SELECT teste0, teste1 FROM teste"
cursor.execute(consulta)

resultados = cursor.fetchall()

workbook = openpyxl.Workbook()
sheet_teste = workbook.active
sheet_teste['A1'] = 'ID'
sheet_teste['B1'] = 'testeABC'

for row_num, (teste0, teste1) in enumerate(resultados, start=2):
    sheet_abastecimentos[f'A{row_num}'] = teste0
    sheet_abastecimentos[f'B{row_num}'] = teste1

workbook.save('teste.xlsx')

cursor.close()
conn.close()
