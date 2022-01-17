from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Listings
from .forms import ListingForm
from .filters import ListingFilter


def index(request: HttpRequest):
    return render(request, "listings/index.html")


def all_listings(request: HttpRequest):
    all_listings = Listings.objects.order_by("-list_date")

    my_filter = ListingFilter(request.GET, queryset=all_listings)
    all_listings = my_filter.qs

    context = {"all_listings": all_listings, "my_filter": my_filter}
    return render(request, "listings/all_listings.html", context=context)


def new_listing(request: HttpRequest):
    if request.method != "POST":
        form = ListingForm()
    else:
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            instance: Listings = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("listings:my_listings")

    context = {"form": form}
    return render(request, "listings/new_listing.html", context)


def detail(request: HttpRequest, detail_id: int):
    listing = Listings.objects.get(pk=detail_id)
    context = {"detail": listing}
    return render(request, "listings/detail.html", context=context)


def my_listings(request: HttpRequest):
    if request.user.is_authenticated:
        listings = Listings.objects.filter(user=request.user).order_by("-list_date")
        context = {"listings": listings}
        return render(request, "listings/my_listings.html", context=context)
    return redirect("users:login")


def edit_listing(request: HttpRequest, edit_id: int):
    listing = Listings.objects.get(id=edit_id)

    if request.method != "POST":
        form = ListingForm(instance=listing)
    else:
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect("listings:my_listings")

    context = {"listing": listing, "form": form}
    return render(request, "listings/edit_listing.html", context)


def delete_listing(request: HttpRequest, delete_id: int):
    listing = Listings.objects.get(id=delete_id)
    if request.method == "POST":
        listing.delete()
        return redirect("listings:my_listings")
    context = {"listing": listing}
    return render(request, "listings/delete_listing.html", context)
