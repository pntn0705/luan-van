from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = 'insects'

urlpatterns = [
    path('insect/<slug>', views.insect_slug, name='slug'),
    path('', views.home, name='home'),
    path('image/<str:image>', views.image, name="image"),
    path('get_all_insect/', views.getAllInsect, name='get_all_insect'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register')
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
