# Django
from django.contrib import admin
from django.urls import path

# Platzigram
from platzigram import views as local_views

# Posts
from posts import views as posts_views


urlpatterns = [
    # Platzigram routes
    path('admin/', admin.site.urls),
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sorted_numbers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    # Posts routes
    path('posts/', posts_views.list_posts),
]