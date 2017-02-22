from django.db import models
from django.core.urlresolvers import reverse


# Custom Manager Class
class CoursesManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query))


# Classe de modelo do Curso.
class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição Simples', blank=True)
    about = models.TextField('Sobre o Curso', blank=True)
    start_date = models.DateField('Data de Início', null=True, blank=True)
    image = models.ImageField(
        upload_to='courses/images',
        verbose_name='Imagem',
        null=True, blank=True
        )
    created_at = models.DateTimeField('Criado em: ', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em: ', auto_now=True)
    objects = CoursesManager()

# Definição do método __str__ para que seja exibido o atibuto name do curso
    def __str__(self):
        return self.name

# Definição de método para resolver o redirecionamento de um curso específico
    def get_absolute_url(self):
        return reverse('courses:details', kwargs={'slug': self.slug})


# Classe para nome amigável ao site de administração
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']