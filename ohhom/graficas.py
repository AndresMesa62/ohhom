import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

class Grafica:

    def mapaCalor( df ):
        
        # Calcular puntaje promedio por departamento
        puntajes_departamento = df.groupby('DepartamentooDondeSeRealizoLaSolicitud')['PuntajeInterno'].mean()
        departamentos = df.groupby('DepartamentooDondeSeRealizoLaSolicitud')
        # Calcular puntaje promedio por municipio
        puntajes_municipio = df.groupby(['DepartamentooDondeSeRealizoLaSolicitud', 'MunicipioDondeSeRealizoLaSolicitud'])['PuntajeInterno'].mean()
        municipios=df.groupby(['DepartamentooDondeSeRealizoLaSolicitud', 'MunicipioDondeSeRealizoLaSolicitud'])
        # Crear gráfico de barras para puntajes por departamento
        fig_departamento = go.Figure(data=go.Bar(x=departamentos, y=puntajes_departamento))
        fig_departamento.update_layout(title='Puntajes de Riesgo por Departamento')

        # Crear subplots para puntajes por municipio
        fig_municipio = make_subplots(rows=len(departamentos), cols=4, subplot_titles=departamentos)
        fila=1
        columna=1
        for i, departamento in enumerate(departamentos):
            puntajes = puntajes_municipio[departamento]
            fig_municipio.add_trace(go.Bar(x=municipios, y=puntajes, name=departamento), row=fila , col=columna)
            columna+=1
            if (columna%5==0):
                columna=1
                fila+=1
        fig_municipio.update_layout(title='Puntajes de Riesgo por Municipio', showlegend=False)
        
        # Mostrar gráficos
        fig_departamento.show()
        fig_municipio.show()




