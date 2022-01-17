from django.urls import path
from . import views

app_name = "listings"

urlpatterns = [
    path("", views.index, name="index"),
    path("all_listings/", views.all_listings, name="all_listings"),
    path("new_listing/", views.new_listing, name="new_listing"),
    path("detail/<int:detail_id>/", views.detail, name="detail"),
    path("my_listings/", views.my_listings, name="my_listings"),
    path("edit_listing/<int:edit_id>/", views.edit_listing, name="edit_listing"),
    path(
        "delete_listing/<int:delete_id>/", views.delete_listing, name="delete_listing"
    ),
]
