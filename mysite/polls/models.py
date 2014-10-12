import datetime

from django.db import models
from django.utils import timezone
from filebrowser.fields import FileBrowseField


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):              # __unicode__ on Python 2
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # cool fields for sorting, etc..
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.choice_text

from filebrowser.base import FileObject
from filebrowser.settings import ADMIN_THUMBNAIL


class BlogEntry(models.Model):

    image = FileBrowseField("Image", max_length=200, directory="images/", extensions=[".jpg", ".png", ".gif"], blank=True, null=True)
    document = FileBrowseField("PDF", max_length=200, directory="documents/", extensions=[".pdf", ".doc"], blank=True, null=True)


# Question object has an attribute called choice_set , created automatically as a back ref from ffk model
# creates a question.choice_set (reference back relation to choices for thi question)  & create
#c = q.choice_set.create(choice_text='Just hacking again', votes=0)