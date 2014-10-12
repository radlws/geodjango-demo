from django.http import HttpResponse
from polls.models import Question, BlogEntry
from polls.forms import BlogEntryForm

from django.views.generic import TemplateView

class BlogEntryView(TemplateView):

    template_name = 'polls/blog.html'

    def get_context_data(self, **kwargs):  # Exec 1st

        self.project_slug = self.kwargs.get('project_slug', '').lower()

        context = super(BlogEntryView, self).get_context_data(**kwargs)

        context['blog_entries'] = BlogEntry.objects.all()
        context['form'] = BlogEntryForm(self.request.POST or None)
        return context


blog_entry = BlogEntryView.as_view()

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question_text for p in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)