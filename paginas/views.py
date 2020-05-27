from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class CurosView(TemplateView):
    template_name = 'Cursos.html'

class ContatoView(TemplateView):
    template_name = 'Contato.html'

class GraficoView(TemplateView):
    template_name = 'grafico.html'

#--------Cursos----------------
class PythonView(TemplateView):
    template_name = 'curso_python.html'

class SqlserverView(TemplateView):
    template_name = 'curso_sqlserver.html'

class ExcelView(TemplateView):
    template_name = 'Cursos_Excel.html'

class HtmlView(TemplateView):
    template_name = 'pagina_HTML.html'

class JavaView(TemplateView):
    template_name = 'Java.html'