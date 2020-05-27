from .views import IndexView, CurosView, ContatoView, GraficoView, PythonView, SqlserverView, ExcelView, HtmlView, JavaView
from django.urls import path


urlpatterns = [
    #pahth('endereco/', minhaviews.as_view(), name='nome-da-url'),
    path('', IndexView.as_view(), name='inicio'),
    path('curso/', CurosView.as_view(), name='curso'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('grafico/', GraficoView.as_view(), name='grafico'),
    
    #----------CURSOS------------------

    path('curso/python/', PythonView.as_view(), name='cursopython'),
    path('curso/sqlserver/', SqlserverView.as_view(), name='cursosqlserver'),
    path('curso/excel/', ExcelView.as_view(), name='cursoexcel'),
    path('curso/java/', JavaView.as_view(), name='cursojava'),
    path('curso/html/', HtmlView.as_view(), name='cursohtml'),

    
    
]