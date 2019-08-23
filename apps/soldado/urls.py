from django.conf.urls import url
from apps.soldado.views import CreateSoldado,DeleteSoldado,UpdateSoldado,ListSoldado, ReporteSoldadoPDF
from apps.soldado.views import UpdateCuerpo, ListCuerpo, DeleteCuerpo, CreateCuerpo, ReporteCuerpoPDF
from apps.soldado.views import UpdateServicio, ListServicio, DeleteServicio, CreateServicio, ReporteServicioPDF
from django.contrib.auth.views import login_required


urlpatterns = [
    url(r'^soldado/listar$', login_required(ListSoldado.as_view()), name='soldado_listar'),
    url(r'^soldado/nuevo$', login_required(CreateSoldado.as_view()), name='soldado_crear'),
    url(r'^soldado/editar/(?P<pk>[\d]+)/$', login_required(UpdateSoldado.as_view()), name='soldado_editar'),
    url(r'^soldado/eliminar/(?P<pk>[\d]+)/$', login_required(DeleteSoldado.as_view()), name='soldado_eliminar'),
    url(r'^soldado/reporte_soldado_pdf/', login_required(ReporteSoldadoPDF.as_view()), name='reporte_soldado_pdf'),

    url(r'^cuerpo/listar$', login_required(ListCuerpo.as_view()), name='cuerpo_listar'),
    url(r'^cuerpo/nuevo$', login_required(CreateCuerpo.as_view()), name='cuerpo_crear'),
    url(r'^cuerpo/editar/(?P<pk>[\d]+)/$', login_required(UpdateCuerpo.as_view()), name='cuerpo_editar'),
    url(r'^cuerpo/eliminar/(?P<pk>[\d]+)/$', login_required(DeleteCuerpo.as_view()), name='cuerpo_eliminar'),
    url(r'^cuerpo/reporte_cuerpo_pdf/', login_required(ReporteCuerpoPDF.as_view()), name='reporte_cuerpo_pdf'),

    url(r'^servicio/listar$', login_required(ListServicio.as_view()), name='servicio_listar'),
    url(r'^servicio/nuevo$', login_required(CreateServicio.as_view()), name='servicio_crear'),
    url(r'^servicio/editar/(?P<pk>[\d]+)/$', login_required(UpdateServicio.as_view()), name='servicio_editar'),
    url(r'^servicio/eliminar/(?P<pk>[\d]+)/$', login_required(DeleteServicio.as_view()), name='servicio_eliminar'),
    url(r'^servicio/reporte_servicio_pdf/', login_required(ReporteServicioPDF.as_view()), name='reporte_servicio_pdf'),

]