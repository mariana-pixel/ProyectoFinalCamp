import os
from flask import Flask,send_file
import plotly.express as px
import pandas as pd


app = Flask(__name__)

@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/cargarfuentedatos")
def cargarfuentedatos():
    with open("energy.csv","r") as archivo:   # Abrir el archivo y preparar variables
        mitabla = "<table id='t_datos' class='table table-hover'>"
        mitabla += "<thead>"
        mitabla += "    <tr>"
        mitabla += "        <th>País</th>"
        mitabla += "        <th>Código</th>"
        mitabla += "        <th>Año</th>"
        mitabla += "        <th>Ahorro</th>"
        mitabla += "    </tr>"
        mitabla += "</thead>"
        mitabla += "<tbody>"
        paises = set()  # Usaremos un conjunto para evitar duplicados
        for linea in archivo:  # Leer línea por línea el archivo
            elemento = linea.split(",")  # Eliminar espacios y dividir por comas
            paises.add(elemento[0])  # Agregar país al conjunto
            mitabla += "<tr>"
            mitabla += "    <td>" + elemento[0] + "</td>"
            mitabla += "    <td>" + elemento[1] + "</td>"
            mitabla += "    <td>" + elemento[2] + "</td>"
            mitabla += "    <td>" + elemento[3] + "</td>"
            mitabla += "</tr>"
        mitabla += "</tbody></table>"



# Crear el <select> para los países únicos
    select_paises = "<select id='sl_paises' class='form-control'>"
    for pais in paises:  # Ordenar los países alfabéticamente
        select_paises =select_paises+ "<option value='" + pais + "'>" + pais + "</option>"
    select_paises =select_paises+ "</select>"
    
    select_grafico = "<select id='sl_grafico' class='form-control'>"
    select_grafico =select_grafico+ "<option value='Linea'>Linea</option>"
    select_grafico =select_grafico+ "<option value='Torta'>Torta</option>"
    select_grafico =select_grafico+ "<option value='Barras'>Barras</option>"
    select_grafico =select_grafico+ "<option value='Area'>Area</option>"
    select_grafico =select_grafico+ "</select>"
    
    todo="<div class='row'>"
    todo=todo+"<div class='col-md-7'>"+select_paises+"</div>"
    todo=todo+"<div class='col-md-3'>"+select_grafico+"</div>"
    todo=todo+"<div class='col-md-2'><button onclick='mostrarGrafico()' class='btn btn-success'>Graficar</button></div>"
    todo=todo+"</div>"

    return todo +"<hr>"+  mitabla 

@app.route('/EnergiaHidro')
def EnergiaHidro():
    content = "<!DOCTYPE html>"
    content += "<html lang='es'>"
    content += "<head>"
    content += "<meta charset='UTF-8'>"
    content += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
    content += "<title>Energía Hidroeléctrica</title>"
    content += "<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'>"
    content += "<style>"
    content += "body { font-family: 'Arial', sans-serif; background-color: #eafaf1; margin: 0; padding: 0; }"
    content += ".section-title { color: #28a745; margin-top: 20px; font-weight: bold; }"
    content += ".content-wrapper { padding: 20px; }"
    content += ".header { text-align: center; padding: 40px; color: white; background-image: url('/static/images/encabezado.jpg'); background-size: cover; background-position: center; position: relative; }"
    content += ".header h1, .header p { position: relative; z-index: 2; }"
    content += ".header::after { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 128, 0, 0.5); z-index: 1; }"
    content += ".advantages, .disadvantages, .history, .uses { padding: 20px; background-color: white; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); margin-bottom: 15px; }"
    content += ".image { max-width: 100%; height: auto; border-radius: 8px; margin-bottom: 15px; }"
    content += ".list-item { margin-bottom: 10px; color: #155724; }"
    content += "a { color: #28a745; text-decoration: none; }"
    content += "a:hover { color: #155724; text-decoration: underline; }"
    content += "</style>"
    content += "</head>"
    content += "<body>"
    content += "<div class='header'>"
    content += "<h1>Energía Hidroeléctrica</h1>"
    content += "<p>Descubre las ventajas, desventajas e historia de esta fuente de energía renovable en Colombia.</p>"
    content += "</div>"
    content += "<div class='container content-wrapper'>"

    # Sección: ¿Qué es la energía hidroeléctrica?
    content += "<div class='row'>"
    content += "<div class='col-md-12'>"
    content += "<h2 class='section-title'>¿Qué es la energía hidroeléctrica?</h2>"
    content += "<p>La energía hidroeléctrica es una fuente de energía renovable que utiliza el agua en movimiento (generalmente en ríos o embalses) para generar electricidad. Esta energía se obtiene mediante el aprovechamiento de la fuerza del agua, ya sea a través de centrales hidroeléctricas que utilizan presas o instalaciones más pequeñas llamadas microco céntrales hidroeléctricas.</p>"
    content += "<div style='text-align: center;'>"; #Contenedor para centrar la imagen
    #content += "<img src='https://github.com/mariana-pixel/ImagenesProyecto/blob/main/imagen1.jpg?raw=true' ";
    #content += "style='width: 300px; height: auto; margin: 20px auto; display: block;' "; #Estilo para tamaño y posición
    #content += "alt='Energía hidroeléctrica'>";
    #content += "</div>";
    content += "</div>"
    content += "</div>"

    # Sección: Ventajas y Desventajas
    content += "<div class='row mt-4'>"
    content += "<div class='col-md-6 advantages'>"
    content += "<h3 class='section-title'>Ventajas</h3>"
    content += "<ul>"
    content += "<li class='list-item'>Energía renovable e inagotable.</li>"
    content += "<li class='list-item'>Bajas emisiones de gases contaminantes.</li>"
    content += "<li class='list-item'>Alta eficiencia en generación eléctrica.</li>"
    content += "<li class='list-item'>Capacidad de almacenamiento mediante presas.</li>"
    content += "</ul>"
    content += "</div>"
    content += "<div class='col-md-6 disadvantages'>"
    content += "<h3 class='section-title'>Desventajas</h3>"
    content += "<ul>"
    content += "<li class='list-item'>Impacto ambiental en ecosistemas acuáticos.</li>"
    content += "<li class='list-item'>Altos costos iniciales de construcción.</li>"
    content += "<li class='list-item'>Dependencia de condiciones climáticas.</li>"
    content += "</ul>"
    content += "</div>"
    content += "</div>"

    # Sección: Historia en Colombia
    content += "<div class='row mt-4'>"
    content += "<div class='col-md-12 history'>"
    content += "<h3 class='section-title'>Historia de la energía hidroeléctrica en Colombia</h3>"
    content += "<p>La energía hidroeléctrica en Colombia comenzó en el siglo XIX, destacando la planta El Charquito en 1900, con importantes expansiones durante el siglo XX. Es una fuente clave en la matriz energética del país.</p>"
    content += "<img src='/images/imagen1.jpg' class='image' alt='Historia de la energía hidroeléctrica en Colombia'>"
    content += "</div>"
    content += "</div>"

    # Sección: Usos de la Energía Hidroeléctrica
    content += "<div class='row mt-4'>"
    content += "<div class='col-md-12 uses'>"
    content += "<h3 class='section-title'>Usos de la energía hidroeléctrica</h3>"
    content += "<p>La energía hidroeléctrica se utiliza principalmente para generar electricidad, pero también se emplea en sistemas de riego, control de inundaciones y recreación en embalses.</p>"
    content += "<img src='/static/images/usos.jpg' class='image' alt='Usos de la energía hidroeléctrica'>"
    content += "</div>"
    content += "</div>"

    # Pie de página
    content += "<footer class='text-center mt-4'>"
    content += "<p>© 2024 Energías Renovables | <a href='#'>Más información</a></p>"
    content += "</footer>"

    content += "</div>"
    content += "</body>"
    content += "</html>"
    return content

@app.route('/graficar/<pais>/<grafico>')
def graficar(pais, grafico):
        df = pd.read_csv("energy.csv", header=None)     # Cargar el archivo en un DataFrame
        df.columns = ["País", "Código", "Año", "Ahorro"]  # Asegurar nombres de columnas

        # Filtrar los datos por el país proporcionado
        df_filtrado = df[df["País"] == pais]

        if df_filtrado.empty:
            return f"<h3>No hay datos disponibles para el país: {pais}</h3>"

        # Crear el gráfico según el tipo seleccionado
        if grafico == "Linea":
            fig = px.line(df_filtrado,
                          x="Año",
                          y="Ahorro",
                          title=f"Ahorro de energía en {pais} (Línea)",
                          markers=True)
        elif grafico == "Torta":
            # Para un gráfico de torta, usamos un único valor por categoría, ejemplo: total por año
            df_agg = df_filtrado.groupby("Año").sum().reset_index()
            fig = px.pie(df_agg,
                         names="Año",
                         values="Ahorro",
                         title=f"Ahorro de energía en {pais} (Torta)")
        elif grafico == "Barras":
            fig = px.bar(df_filtrado,
                         x="Año",
                         y="Ahorro",
                         title=f"Ahorro de energía en {pais} (Barras)",
                         text_auto=True)
        elif grafico == "Area":
            fig = px.area(df_filtrado,
                          x="Año",
                          y="Ahorro",
                          title=f"Ahorro de energía en {pais} (Área)")
        else:
            return f"<h3>Tipo de gráfico '{grafico}' no reconocido.</h3>"
        # Convertir el gráfico a HTML
        graph_html = fig.to_html(full_html=False)
        return graph_html

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
