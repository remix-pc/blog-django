from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from posts.models import Post
from django.db.models import Q, Count, Case, When

# Create your views here.


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 2
    context_object_name = 'posts'
    ordering = ['-id']

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(publishPost=True)
        qs = qs.annotate(
            commentNumber = Count(
                Case(
                    When(comment__publishComment=True, then=1)
                )
            )
        )

        return qs



class PostSearch(PostIndex):
    template_name = 'posts/post_search.html'

    def get_queryset(self):
        qs =  super().get_queryset()

        term = self.request.GET.get('termo')

        if not term:
            return qs

        qs = qs.filter(
            Q(titlePost__icontains=term) |
            Q(author__first_name__iexact=term) |
            Q(content__icontains=term) |
            Q(excerpt__icontains=term) |
            Q(category__name_cat__iexact=term)
        )


        return qs

class PostCategory(PostIndex):
    template_name = 'posts/post_category.html'

    def get_queryset(self):
        qs = super().get_queryset()

        categorie = self.kwargs.get('category', None)

        if not categorie:
            return qs

        qs = qs.filter(category__name_cat__iexact=categorie)

        return qs

class PostDetails(UpdateView):
    pass