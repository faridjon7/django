import logging

from django.conf import settings
from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import translation

from products.models import Product, Purchase

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


def details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        Purchase.objects.create(
            user=request.user, product=product, count=request.POST.get("count")
        )
        return redirect("cart")
    return render(request, "details.html", {"product": product})


def cart(request):
    purchases = Purchase.objects.filter(user=request.user, status="IN_CART")
    return render(request, "purchases.html", {"purchases": purchases})


def language(request):
    lang = request.GET.get("lang", "ru")
    translation.activate(lang)
    response = redirect(request.META.get("HTTP_REFERER", "index"))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    return response
