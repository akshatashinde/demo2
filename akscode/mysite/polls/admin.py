from django.contrib import admin
from .models import Question, Choice,Person,Album,Musician,Fruit,Example




class ChoiceInline(admin.TabularInline):
	model=Choice
	extra=3
		
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date')
	fieldsets=[
		('Text of Question',{'fields':['question_text']}),
		('Date information', {'fields': ['pub_date'],'classes':['collapse']}),
	]
	search_fields=['question_text']
	inlines=[ChoiceInline]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Person)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Fruit)
admin.site.register(Example)

