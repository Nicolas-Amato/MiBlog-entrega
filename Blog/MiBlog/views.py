from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

##redirecciona correcta###
from django.urls import reverse_lazy

##  Auth  ###
from django.contrib.auth.views import LoginView, LogoutView

#los decoradores sirvenn para vistas basadas en funciones
from django.contrib.auth.decorators import login_required
###ejemplo
###@decorador
###def funcion a protejker


#los decoradores sirvenn para vistas basadas en class
from django.contrib.auth.mixins import LoginRequiredMixin
###ejemplo
###class  classaprotejer(Mixinparaprotejer)


from .models import autor, avatar
from .forms import autorForm, SignUpForm, UserEditForm

def info_ankay(request):
   return render(request, 'info_ankay.html')


def index(request):
   return render(request, 'index.html')
   
######### BUSQUEDAS ########## ok
def buscar_autor(request):
   data = request.GET.get('nombre', '')
   error = ''

   if data:
      try:
         autores = autor.objects.get(nombre=data)
         return render(request, 'consulta_autor.html', {'autores': autores, 'nombre': data})
      except Exception as exc:
         error = 'no hay resultados'
   return render(request, 'consulta_autor.html', {'error': error})


######### INGRESOS  ########## ok
@login_required
def nuevo_autor(request):
   if request.method == 'POST':
      
      formulario_NA = autorForm(request.POST)
      if formulario_NA.is_valid():
         
         formulario_NA_limpio = formulario_NA.cleaned_data
         
         nuevo_autor = autor(nombre=formulario_NA_limpio['nombre'],
                             titulo=formulario_NA_limpio['titulo'],
                             email=formulario_NA_limpio['email'], 
                             subtitulo=formulario_NA_limpio['subtitulo'],
                             post=formulario_NA_limpio['post'])
         nuevo_autor.save()
         return render(request, 'index.html')

   else:
      formulario_NA = autorForm()
      
   return render(request, 'nuevo_autor.html', {'formulario_NA': formulario_NA})

######### MOSTRAR  ########## OK
def mostrar_autor(request):
   
   posts = autor.objects.all
   
   context = {'posts': posts}
   
   return render(request, 'mostrar_autor.html', context)
   
######### ELIMINAR  ########## ok
@login_required
def eliminar_autor(request, autor_nombre):
   
   autores = autor.objects.get(nombre=autor_nombre)
   
   autores.delete()
   ####vuelvo al menu   
   autores = autor.objects.all()
   
   context = {'autores': autores}   
   
   return render(request, 'mostrar_autor.html', context)
   
######### MODIFICAR  ########## ok
@login_required
def modif_autor(request, autor_nombre):
   
   autores = autor.objects.get(nombre=autor_nombre)
   
   if request.method == 'POST':
      
      formulario_NAM = autorForm(request.POST)
      
      if formulario_NAM.is_valid():
         
         formulario_NAM_limpio = formulario_NAM.cleaned_data
         
         autores.nombre = formulario_NAM_limpio['nombre'] 
         autores.titulo = formulario_NAM_limpio['titulo']
         autores.subtitulo = formulario_NAM_limpio['subtitulo']
         autores.post = formulario_NAM_limpio['post']
         
         
         autores.save()
         
         return render(request, 'index.html')

   else:
      formulario_NAM = autorForm(initial={'nombre': autores.nombre, 'titulo': autores.titulo, 'email':autores.email, 'fecha':autores.fecha, 'subtitulo':autores.subtitulo, 'post': autores.post })
      
   return render(request, 'modif_autor.html', {'formulario_NAM': formulario_NAM})

#### update admin ##### ok
@login_required
def editar_usuario(request):
   usuario = request.user

   if request.method == 'POST':

      usuario_form = UserEditForm(request.POST)
      if usuario_form.is_valid():
         
         informacion = usuario_form.cleaned_data
         
         usuario.username = informacion['username']
         usuario.email = informacion['email']
         usuario.password1 = informacion['password1']
         usuario.password2 = informacion['password2']
      usuario.save()

      return render(request, 'index.html')


   else:
      usuario_form = UserEditForm(initial={
         'username': usuario.username,
         'email': usuario.email,
         })

   return render(request , 'admin_update.html',{
      'form': usuario_form,
      'usuario': usuario
   })



class autorList(ListView):
   
   model = autor
   template_name = 'Miblog/autor_list.html'
   
   
class autorDetailView(DetailView, LoginRequiredMixin):
   model = autor
   template_name = 'MiBlog/autor_detalle.html'


class autorDeleteView(DeleteView, LoginRequiredMixin):
   model = autor
   success_url ='/autor_list'   


class autorUpdateView(UpdateView, LoginRequiredMixin):
   model = autor
   success_url ='/autor_list'   
   fields = ['nombre', 'titulo','email', 'fecha', 'subtitulo', 'post']


class autorCreateView(CreateView):
   model = autor
   success_url ='/autor_list'   
   fields =  ['nombre', 'titulo','email', 'fecha', 'subtitulo', 'post']
   
   
#####login...creasion de usuario#####

class signUpView(CreateView):
   form_class = SignUpForm
   success_url = reverse_lazy('home')
   template_name = 'registro.html'

 #####login...ingreso de secion#####  


class adminloginView(LoginView):
   template_name = 'login.html'


class adminLogoutView(LogoutView):
   template_name = 'logout.html'



