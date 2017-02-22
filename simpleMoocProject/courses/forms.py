from django import forms
from django.conf import settings
from simpleMoocProject.core.mail import send_mail_template


# Classe para manipular o formulario de contato sobre o curso
class ContactCourse(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Menssagem', widget=forms.Textarea)

# Método para concatenação e envio dos emails
    def send_mail(self, course):
        subject = '[%s] contato' % course

        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }

        template_name = 'courses/contact_email.html'
        send_mail_template(
            subject, template_name, context,
            [settings.CONTACT_EMAIL]
        )
