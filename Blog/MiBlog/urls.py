from django.urls import path
from . import views
from .forms import autorForm, SignUpForm, UserEditForm


urlpatterns = [
    path('', views.index, name= 'home'),
    path('info_ankay/', views.info_ankay, name='info ankay'),
    path('buscar_autor/', views.buscar_autor, name='buscar Autor'),
    path('nuevo_autor/', views.nuevo_autor, name='Nuevo Autor'),
    path('mostrar_autor/', views.mostrar_autor, name='mostrar Autor'),
    path('eliminar_autor/<autor_nombre>', views.eliminar_autor, name='eliminar Autor'),
    path('modif_autor/<autor_nombre>', views.modif_autor, name='Editar Autor'),
    path('autorForm/', autorForm),
    path('autor_list/', views.autorList.as_view(), name='List'),
    path('autor_detalle/<pk>', views.autorDetailView.as_view(), name='Detail'),
    path('autor_conf_delete/<pk>', views.autorDeleteView.as_view(), name='Delete'),
    path('autor_form/<pk>', views.autorUpdateView.as_view(), name='Update'),
    path('autors_form/', views.autorCreateView.as_view(), name='Create'),
    path('signup/', views.signUpView.as_view(), name='Sign Up'),
    path('login/', views.adminloginView.as_view(), name='Login'),
    path('logout/', views.adminLogoutView.as_view(), name='Logout'),
    path('editar_usuario/', views.editar_usuario, name='Editar usuario')
]
