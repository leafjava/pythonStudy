from django.urls import path,re_path
from . import views

urlpatterns = [
  path('year/<int:year>',views.article_year),
  re_path(r'^article/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$',views.article_month),
  path('article/<int:year>/<int:month>/<slug:flag>',views.article_flag),
  path('current',views.get_current_datetime),
  path('list/',views.list)

]