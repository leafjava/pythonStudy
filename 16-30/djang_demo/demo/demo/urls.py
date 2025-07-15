from django.contrib import admin
from django.urls import path,re_path,include
from app01.views import helloworld,article_year,article_month,article_flag

urlpatterns = [
    path('account/',include('account.urls')),
    path('article/',include('app01.urls')),
    # path('hello/',helloworld),
    # path('article/year/<year>',article_year),
    # re_path(r'^article/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$',article_month),
    # path('article/<int:year>/<int:month>/<slug:flag>',article_flag),
    path('admin/', admin.site.urls),
]
