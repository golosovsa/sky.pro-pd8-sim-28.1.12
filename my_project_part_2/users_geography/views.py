from django.db.models import Prefetch, Count, Subquery, Q
from django.http import JsonResponse
from django.views.generic import ListView

from users_geography.models import City, User


# TODO внесите необходимые изменения в код ниже
class CityRateView(ListView):
    model = City
    queryset = City.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        users_count = User.objects.count()

        cities = City.objects\
            .annotate(users_count=Count("users"))\
            .all()

        response = []

        for city in cities:
            count = city.users_count
            response.append({
                "id": city.id,
                "name": city.name,
                "status": city.status,
                "users": count,
                "users_percent": count / users_count,
            })

        return JsonResponse(response, safe=False)

