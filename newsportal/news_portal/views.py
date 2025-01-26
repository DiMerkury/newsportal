from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post
from .filters import PostFilter
from .forms import PostForm



class NewsList(ListView):
    queryset = Post.objects.filter(type = 'NW')
    ordering = '-datetime_in'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

class PostList(ListView):
    model = Post
    ordering = '-datetime_in'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class SearchPost(ListView):
    model = Post
    ordering = '-datetime_in'
    template_name = 'search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

#def create_post(request):
#    if request.method == 'POST':
#        form = PostForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/news/')
#    form = PostForm()
#    return render(request, 'post_edit.html', {'form': form})

class PostCreate(CreateView):
    permission_required = ('news_portal.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        if 'articles/create' in self.request.path:
            post.type = 'AR'
        return super().form_valid(form)

class PostUpdate(UpdateView, LoginRequiredMixin):
    permission_required = ('news_portal.update_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

#class IndexView(LoginRequiredMixin, TemplateView):
#    template_name = 'index.html'