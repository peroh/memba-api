import factory

from ..models import CustomUser

class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser
        
    email = factory.Sequence(lambda n: 'person{0}@example.com'.format(n))
    first_name = factory.Faker('text', max_nb_chars=20)
    last_name = factory.Faker('text', max_nb_chars=20)