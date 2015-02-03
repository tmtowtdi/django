
import datetime

from django.db import models
from django.utils import timezone

class Question( models.Model ):
    ### max_length = INT is required for CharField()s.
    question_text   = models.CharField( max_length=200 )
    pub_date        = models.DateTimeField( 'date published' )

    """
    The 'date published' up there is the human-readable name of the column.  
    It's used in a few places and doubles as documentation.  Optional; if it's 
    not included, Django just uses the attribute name instead.
    """

    def __str__( self ):
        return self.question_text

    def was_published_recently( self ):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    """
    On the admin page, columns are sortable by clicking the column header.  
    Except when you're including a custom method as one of the columns (we're 
    including was_published_recently).  So that column can't be sorted on its 
    own, but we can force it to sort based on the values of another column.  
    """
    was_published_recently.admin_order_field = 'pub_date'

    """
    While we're at it, that column is named, by default, titlecase( s/_/ /g ), 
    so "was_published_recently" => "Was Published Recently", and it displays 
    the actual value, so either "True" or "False".

    All well and good, but let's change the column name to be a little nicer, 
    and set it to display a little icon (green checkmark for True, red 
    strikethrough for false), instead of the text "True" or "False".
    """
    was_published_recently.short_description = 'Published recently?'
    was_published_recently.boolean = True


class Choice( models.Model ):
    question    = models.ForeignKey( Question )
    choice_text = models.CharField( max_length=200 )
    ### default = VAL is optional for all fields
    votes       = models.IntegerField( default=0 )

    def __str__( self ):
        return self.choice_text

