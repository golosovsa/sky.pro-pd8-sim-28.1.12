from django.http import JsonResponse
from django.views import View

from counting_rhyme.models import City, User


# TODO внесите необходимые изменения в код ниже
class CountView(View):
    def get(self, request):

        cities = City.objects.count()
        users = User.objects.count()

        return JsonResponse({
            "cities": cities,
            "users": users,
        })
