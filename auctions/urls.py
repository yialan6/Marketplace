from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('listing', views.listing, name='listing'),
    path('<int:item_id>', views.item, name='item'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('category/<str:category>', views.category, name='category'),
    path('user_listing', views.user_listing, name='user_listing'),
    path('winnings', views.winnings, name='winnings')
]
