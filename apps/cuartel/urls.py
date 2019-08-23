from django.conf.urls import url
from apps.cuartel.views import CreateCuartel, UpdateCuartel, ListCuartel, DeleteCuartel, ReporteCuartelPDF
from apps.cuartel.views import CreateCompania, DeleteCompania, ListCompania, UpdateCompania, ReporteCompaniaPDF
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^cuartel/listar$', login_required(ListCuartel.as_view()), name='cuartel_listar'),
    url(r'^cuartel/nuevo$', login_required(CreateCuartel.as_view()), name='cuartel_crear'),
    url(r'^cuartel/editar/(?P<pk>[\d]+)/$', login_required(UpdateCuartel.as_view()), name='cuartel_editar'),
    url(r'^cuartel/eliminar/(?P<pk>[\d]+)/$', login_required(DeleteCuartel.as_view()), name='cuartel_eliminar'),
    url(r'^cuartel/reporte_cuartel_pdf/', login_required(ReporteCuartelPDF.as_view()), name='reporte_cuartel_pdf'),

    url(r'^compañia/listar$', login_required(ListCompania.as_view()), name='compania_listar'),
    url(r'^compañia/nuevo$', login_required(CreateCompania.as_view()), name='compania_crear'),
    url(r'^compañia/editar/(?P<pk>[\d]+)/$', login_required(UpdateCompania.as_view()), name='compania_editar'),
    url(r'^compañia/eliminar/(?P<pk>[\d]+)/$', login_required(DeleteCompania.as_view()), name='compania_eliminar'),
    url(r'^compañia/reporte_compañia_pdf/', login_required(ReporteCompaniaPDF.as_view()), name='reporte_compania_pdf'),
]
