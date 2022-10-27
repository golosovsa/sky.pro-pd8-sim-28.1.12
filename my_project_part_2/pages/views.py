from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.generic import ListView

from my_project import settings
from pages.models import City

# TODO максимальное число записей на одной странице не должно превышать 5 элементов
TOTAL_ON_PAGE = 5


# TODO внесите необходимые изменения в код ниже
class CityListView(ListView):
    model = City
    queryset = City.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        page_number = request.GET.get("page")
        total_on_page = settings.TOTAL_ON_PAGE

        paginator = Paginator(self.object_list, total_on_page)
        page = paginator.get_page(page_number)

        cities = []
        for city in page:
            cities.append({
                "id": city.id,
                "name": city.name,
                "status": city.status,
            })

        return JsonResponse({
            "items": cities,
            "total": paginator.count,
            "num_pages": paginator.num_pages,
        })
