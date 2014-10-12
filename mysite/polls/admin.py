from django.contrib import admin
from polls.models import Question, Choice, BlogEntry

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse', 'wide']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)


from filebrowser.base import FileObject
from filebrowser.settings import ADMIN_THUMBNAIL


class BlogEntryAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse', 'wide']}),
    # ]
    # inlines = [ChoiceInline]
    list_display = ('image', 'document', 'image_thumbnail')
    # list_filter = ['pub_date']
    # search_fields = ['question_text']

    def image_thumbnail(self, obj):
        if obj.image:
            image = FileObject(obj.image.path)
            if image.filetype == "Image":
                return '<img src="%s" />' % image.version_generate(ADMIN_THUMBNAIL).url
        else:
            return ""
    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "Thumbnail"


admin.site.register(BlogEntry, BlogEntryAdmin)