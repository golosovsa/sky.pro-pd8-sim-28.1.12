from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from along_neva_channels.models import Tour


# TODO Здесь необходимо реализовать CBV в соответствии со спецификацией
class TourListView(ListView):
    model = Tour

    def get(self, *args, **kwargs):
        super(TourListView, self).get(*args, **kwargs)

        tours = self.object_list
        response = []
        for tour in tours:
            points = [{"name": point.name} for point in tour.points.all()]
            response.append({
                "id": tour.id,
                "name": tour.name,
                "starts_at": tour.starts_at,
                "ends_at": tour.ends_at,
                "points": points,
            })

        return JsonResponse(response, safe=False)


class TourDetailView(DetailView):
    model = Tour

    def get(self, *args, **kwargs):
        super(TourDetailView, self).get(*args, **kwargs)

        tour = self.object
        points = [{"name": point.name} for point in tour.points.all()]
        response = {
            "id": tour.id,
            "name": tour.name,
            "starts_at": tour.starts_at,
            "ends_at": tour.ends_at,
            "points": points,
        }
        print(response)
        return JsonResponse(response)
