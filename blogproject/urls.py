# urls.py
from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.index, name="index"),
    path('<int:blog_id>/', blogapp.views.detail, name="detail"),
    path('write/', blogapp.views.write, name="write"),
    path('create/', blogapp.views.create, name="create"),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('signup/', accounts.views.signup, name="signup"),
    path('signin/', accounts.views.signin, name="signin"),
    path('logout/', accounts.views.logout, name="logout"),
    path('accounts/', include('allauth.urls')),
    path('map', blogapp.views.map, name="map"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
