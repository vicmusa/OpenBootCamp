import pandas as ps

archivo = 'C:/Users/usuario/Downloads/test.xlsx'

df = ps.read_excel(archivo)

list = []
for index, row in df.iterrows():
    aux = {}
    correo = row[0]
    aux = correo
    list.append(aux)


filteredList = set(list)

print(filteredList)