import pandas as pd
import sqlite3

# Desde CSV
df_csv = pd.read_csv('ventas.csv')
print("Desde CSV:")
print(df_csv.head())

# Desde Excel (hoja específica)
df_excel_ventas = pd.read_excel('datos.xlsx', sheet_name='Ventas')
df_excel_clientes = pd.read_excel('datos.xlsx', sheet_name='Clientes')
print("\nDesde Excel - Ventas:")
print(df_excel_ventas.head())

# Desde JSON
df_json = pd.read_json('productos.json')
print("\nDesde JSON:")
print(df_json)

# Desde SQLite
conn = sqlite3.connect('ventas.db')
df_sql = pd.read_sql('SELECT * FROM pedidos', conn)
conn.close()
print("\nDesde SQLite:")
print(df_sql)

print("\nTodas las extracciones completadas y validadas.")

# ===========================================
# EXPORTACIÓN A ARCHIVO UTF-8 (salida.txt)
# ===========================================
with open("salida.txt", "w", encoding="utf-8") as f:
    f.write("=== EXTRACCIÓN COMPLETA ===\n\n")

    f.write("--- CSV ---\n")
    f.write(df_csv.to_string())
    f.write("\n\n")

    f.write("--- Excel (Ventas) ---\n")
    f.write(df_excel_ventas.to_string())
    f.write("\n\n")

    f.write("--- Excel (Clientes) ---\n")
    f.write(df_excel_clientes.to_string())
    f.write("\n\n")

    f.write("--- JSON ---\n")
    f.write(df_json.to_string())
    f.write("\n\n")

    f.write("--- SQLite ---\n")
    f.write(df_sql.to_string())
    f.write("\n\n")

print("Archivo 'salida.txt' generado correctamente en UTF-8.")
