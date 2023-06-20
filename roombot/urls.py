from os import name
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home),
    path("findfood/", views.find_food),
    path("test/", views.test),
    path("diary/", views.diary),
    path("output/", views.query),
    path("register/", views.sign_up, name="register"),
    path("login/", views.sign_in, name="login"),
    path("logout/", views.log_out, name="logout"),
    path("comment/", views.comment),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    #path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("text/<int:pk>/", views.text_detail, name="pk"),
    path("text/<int:pk>/edit/", views.text_edit, name="pk"),
    path("text/add/", views.text_add),
    path("text/<int:pk>/delete/", views.text_delete, name="pk"),
    path("text/", views.text),
    path("404/", views.error_404),
    path("rwd/", views.rwd),
]

handler404 = "roombot.views.error_404"
handler500 = "roombot.views.error_500"


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
