from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import forecast.views
# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("weather/data", forecast.views.data, name="data"),
    path("weather/summarize", forecast.views.summarize, name="summarize"),
    
    path("weather/seed", forecast.views.seed, name="seed"),
    path("weather/count", forecast.views.count_data, name="count_data"),
    path("*",forecast.views.defaultResponse, name="defaultResponse")
    #path("admin/", admin.site.urls),
]
