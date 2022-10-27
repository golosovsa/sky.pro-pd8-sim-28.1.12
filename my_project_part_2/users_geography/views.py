from django.db.models import Prefetch, Count, Subquery
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


        cities = self.object_list
        cities.prefetch_related(
            Prefetch(
                "user_set",
                queryset=User.objects.only("id", "city_id").values("city_id").annotate(count=Count("id"))
            )
        )
        response = []
        for city in cities:
            users = city.user_set
            response.append({
                "id": city.id,
                "name": city.name,
                "status": city.status,
                "users": users,
                "users_percent": users / users_count,
            })
        return JsonResponse(response, safe=False)

