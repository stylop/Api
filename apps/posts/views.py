from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm



class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'posts/post_form.html'
    form_class = PostForm
    success_url = reverse_lazy('post-create')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    # paginate_by = 3

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('blog-home')
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostUpdateView, self).form_valid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('blog-home')






#
# def post_create(request):
#
#
#     form = PostForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         instance.save()
#         # message success
#         messages.success(request, "Successfully Created")
#         return HttpResponseRedirect(instance.get_absolute_url())
#     context = {
#         "form": form,
#     }
#     return render(request, "posts/post_form.html", context)

