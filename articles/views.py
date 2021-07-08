from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Article
from .forms import ArticleForm

class StaffRequiredMixin(object):
    """
    Este mixin requerira que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class ArticleListView(ListView):

    model = Article


class ArticleDetailView(DetailView):

    model = Article

@method_decorator(staff_member_required, name='dispatch')
class ArticleCreate( CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('articles:articles')

    
@method_decorator(staff_member_required, name='dispatch')
class ArticleUpdate(UpdateView):

    model = Article

    form_class = ArticleForm

    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('articles:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:articles')