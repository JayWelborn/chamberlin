# Django imports
from django.views import generic
from django.utils import timezone

# Relative imports
from .models import Entry, Tag
from home.models import Contact


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_list'
    model = Entry
    paginate_by = 5

    def get_context_data(self, **kwargs):
        """
        Get most recent contact object for social media links
        """
        context = super(IndexView, self).get_context_data(**kwargs)
        context['contact'] = Contact.objects.latest('pub_date')
        return context

    def get_queryset(self):
        """
        Return blog entries sorted by date
        """
        entries = Entry.objects.distinct()
        return entries.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


class DetailView(generic.DetailView):
    """
    View single blog entry
    """
    model = Entry
    template_name = 'blog/detail.html'


class TagDetailView(generic.DetailView):
    model = Tag
    template_name = 'blog/tag_detail.html'
    context_object_name = 'tag'
