
from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInLine( admin.TabularInline ):
    model = Choice
    extra = 3

class QuestionAdmin( admin.ModelAdmin ):

    ### By default, the Question object's str() is displayed on the "list of 
    ### questions" page.  Tell it to display a little more data.
    list_display = ( 'question_text', 'pub_date', 'was_published_recently' )

    ### This adds a sidebar div to the right that lets the user filter the 
    ### displayed questions - only show those published today, this week, this 
    ### month, etc.
    list_filter = [ 'pub_date' ]

    ### Adds a search box up top
    search_fields = [ 'question_text' ]

    ### The questions displayed will be automatically paginated, by default 
    ### 100 per page.  We can change that number per page to whatever we want.
    list_per_page = 50

    ### See polls/models.py for some settings on how we're controlling display 
    ### and sorting of the was_published_recently column.


    ### Re-order the fields as they display on the admin page, adding a 
    ### fieldset.
    fieldsets = [
        (None,                  { 'fields': ['question_text']                           }),
        ('Date Information',    { 'fields': ['pub_date' ],     'classes': ['collapse']  }),
    ]
    inlines = [ ChoiceInLine ]


admin.site.register( Question, QuestionAdmin )
