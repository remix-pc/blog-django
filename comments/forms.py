from django.forms import ModelForm
from .models import Comment
import requests

class FormComment(ModelForm):

    def clean(self):
        rawData = self.data 

        recaptchaResponse = rawData.get('g-recaptcha-response')

        if not recaptchaResponse:
            self.add_error('comment', 'Por favor, marque a caixa "Não sou um robo"')


        recaptchaRequest = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
            'secret': 'yourkey_recaptcha',
            'response': recaptchaResponse,
        })


        recaptchaResult = recaptchaRequest.json()

        if not recaptchaResult.get('success'):
            self.add_error('comment', 'Desculpe Mr. Robot mas ocorreu um erro')


        cleanedData = self.cleaned_data
        name = cleanedData.get('nameComment')
        email = cleanedData.get('emailComment')
        comment = cleanedData.get('comment')

        if len(name) < 3:
            self.add_error('nameComment', 'Nome precisa ter mais de 2 caracteres')
        

    class Meta:
        model = Comment
        fields = ('nameComment', 'emailComment', 'comment')