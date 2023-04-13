from django.forms import ModelForm
from .models import Comment


class FormComment(ModelForm):

    def clean(self):
        data = self.cleaned_data
        name = data.get('nameComment')
        email = data.get('emailComment')
        comment = data.get('comment')

        if len(name) < 3:
            self.add_error('nameComment', 'Nome precisa ter mais de 2 caracteres')
        

    class Meta:
        model = Comment
        fields = ('nameComment', 'emailComment', 'comment')