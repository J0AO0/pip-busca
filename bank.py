import mysql.connector
import openpyxl

conn = mysql.connector.connect(
    host='192.168.10.144',
    user='root',
    password='f4c1l',
    database='testegralha'
)

cursor = conn.cursor()

consulta = "SELECT RevestimentoId, RevestimentoDescricao FROM revestimento"
cursor.execute(consulta)

resultados = cursor.fetchall()

workbook = openpyxl.Workbook()
sheet_abastecimentos = workbook.active
sheet_abastecimentos['A1'] = 'ID'
sheet_abastecimentos['B1'] = 'Abastecimento Importado'

for row_num, (RevestimentoId, RevestimentoDescricao) in enumerate(resultados, start=2):
    sheet_abastecimentos[f'A{row_num}'] = RevestimentoId
    sheet_abastecimentos[f'B{row_num}'] = RevestimentoDescricao

workbook.save('revestimento.xlsx')

cursor.close()
conn.close()