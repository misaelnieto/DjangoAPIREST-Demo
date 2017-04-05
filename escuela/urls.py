from django.conf.urls import url
from escuela import views

urlpatterns = [
    url(r'^carreras/$', views.carrera_list),
    url(r'^carreras/(?P<pk>[0-9]+)/$', views.carrera_detail),
    url(r'^alumnos/$', views.alumno_list),
    url(r'^alumnos/(?P<pk>[0-9]+)/$', views.alumno_detail),
]