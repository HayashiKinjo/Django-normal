from django.contrib import admin

# Register your models here.

from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    #Choice is edited on Question admin page by default
    inlines = [ChoiceInline]

    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fileds = ['question_test']

admin.site.register(Question,QuestionAdmin)
