from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ...forms import EjercicioForm
from ...models.Ejercicio import Ejercicio
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.shortcuts import render


class EjercicioListView(ListView):
    model = Ejercicio
    template_name = 'ejercicio/list.html'
    context_object_name = 'ejercicios'
    extra_context = {'titulo': 'Ejercicios',
                     'crear': 'blog:ejercicio_create'
                     }

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Ejercicio.objects.get(pk=request.POST['id']).toJson()
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data)


# Crear un Ejercicio
class EjercicioCreateView(CreateView):
    model = Ejercicio
    form_class = EjercicioForm
    template_name = 'ejercicio/form.html'
    success_url = reverse_lazy('blog:ejercicio_list')
    extra_context = {'titulo': 'Ejercicios Crear',
                     }

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = EjercicioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        return render(request, self.template_name, {'titulo': 'Ejercicios Crear',
                                                    'form': form
                                                    })


# Actualizar un Ejercicio
class EjercicioUpdateView(UpdateView):
    model = Ejercicio
    template_name = 'ejercicio/form.html'
    fields = '__all__'  # Cambia esto si deseas incluir campos específicos
    success_url = reverse_lazy('ejercicio_list')


# Eliminar un Ejercicio
class EjercicioDeleteView(DeleteView):
    model = Ejercicio
    template_name = 'ejercicio/confirm_delete.html'
    success_url = reverse_lazy('ejercicio_list')


# Detalle de un Ejercicio
class EjercicioDetailView(DetailView):
    model = Ejercicio
    template_name = 'ejercicio/detail.html'
    context_object_name = 'ejercicio'
