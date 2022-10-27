from django.http import JsonResponse
from django.views.generic import DetailView, ListView

from discounts.models import Discount, Tour


# TODO здесь необходимо реализовать СBV которые
# TODO бы возвращали данные в соответствии со спецификацией
class DiscountListView(ListView):
    model = Discount

    def get(self, *args, **kwargs):
        super().get(*args, **kwargs)

        json_list = []
        discount_list = self.get_queryset()
        for discount in discount_list:
            tour = discount.tour
            json_list.append({
                "id": discount.id,
                "tour": tour.id,
                "category": discount.category,
                "discount": discount.discount,
                "code": discount.code,
                "starts_at": discount.starts_at,
                "ends_at": discount.ends_at,
            })

        return JsonResponse(json_list, safe=False)


class DiscountDetailView(DetailView):
    model = Discount

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        discount: Discount = self.object

        return JsonResponse({
            "id": discount.id,
            "tour": discount.tour.id,
            "category": discount.category,
            "discount": discount.discount,
            "code": discount.code,
            "starts_at": discount.starts_at,
            "ends_at": discount.ends_at,
        })

