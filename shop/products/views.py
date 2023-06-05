import logging

from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from products.models import Product

logger = logging.getLogger(__name__)


def index(request):
    title = request.GET.get("title")
    purchases__count = request.GET.get("purchases__count")

    result = cache.get(f"products-view-{title}-{purchases__count}-{request.user.id}")
    if result is not None:
        return result

    products = Product.objects.all()

    if title is not None:
        products = products.filter(
            Q(title__icontains=title) | Q(description__icontains=title)
        )

    if purchases__count is not None:
        products = products.filter(purchases__count=purchases__count)

    page_number = request.GET.get("page")
    paginator = Paginator(products, 12)
    products = paginator.get_page(page_number)
    return render(request, "index.html", {"products": products})
