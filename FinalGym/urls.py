from django.urls import path
from FinalGym import views
from django.contrib.auth.views import LogoutView



urlpatterns = [

    path("addClases/", views.agregarClase, name='addClases'),
    path("addEntrenador/", views.agregarEntrenador, name="addEntrenadores"),
    path("addUsuario/", views.agregarUsuario, name='addUsuarios'),
    path("", views.inicio, name='Inicio'),
    path("busquedaCamada/", views.busquedaCamada, name="BusquedaCamada"),
    path("buscar/", views.buscar),
    path("listaentrenadores", views.listaEntrenadores, name="ListaEntrenadores"),
    path("borrarentrenador/<entrenador_nombre>", views.borrarEntrenadores, name="BorrarEntrenador"),
    path("editarentrenador/<entrenador_nombre>", views.editarEntrenadores, name="EditarEntrenador"),
    path('about-us/', views.Aboutus, name="About-us" ),
    path('clase/lista', views.ClaseList.as_view(), name='ListClases'),
    path(r'^(?P<pk>\d+)$', views.ClaseDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ClaseCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ClaseUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ClaseDelete.as_view(), name='Delete'),
    path('login', views.login_request, name = 'Login'),
    path('logout', LogoutView.as_view(template_name='FinalGym/logout.html'), name='Logout'),
    path('register', views.register, name = 'Register'),
    path("editarUsuario", views.editarUsuario, name="EditarUsuario"),
    path('usuario/lista', views.UsuarioList.as_view(), name='ListUsuario'),
    path('agregarImagen/', views.agregarImagen, name='Subir Avatar'),
    




  
]
    


    
