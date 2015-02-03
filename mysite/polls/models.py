from django.db import models

class Question( models.Model ):
    question_text   = models.CharField( max_length=200 )
    pub_date        = models.DateTimeField( 'date published' )

    """
    The 'date published' up there is the human-readable name of the column.  
    It's used in a few places and doubles as documentation.  Optional; if it's 
    not included, Django just uses the attribute name instead.

    max_length = INT is required for CharField()s.

    default = VAL is optional for all fields (see `votes`, below).
    """

class Choice( models.Model ):
    question    = models.ForeignKey( Question )
    choice_text = models.CharField( max_length=200 )
    votes       = models.IntegerField( default=0 )

