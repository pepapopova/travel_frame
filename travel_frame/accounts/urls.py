from django.urls import path

from travel_frame.accounts.views import LoginTravelView, RegisterTravelView, LogoutTravelView, \
    UserDetailsView, UserEditView, UserDeleteView, UserFavoritesView

urlpatterns = (
    path('login/', LoginTravelView.as_view(), name='login user'),
    path('register/', RegisterTravelView.as_view(), name='register user'),
    path('logout/', LogoutTravelView.as_view(), name='logout user'),
    path('profile/<int:pk>/details/', UserDetailsView.as_view(), name='details user'),
    path('profile/<int:pk>/favourites/', UserFavoritesView.as_view(), name='user favourites'),
    path('profile/<int:pk>/edit/', UserEditView.as_view(), name='edit user'),
    path('profile/<int:pk>/delete/', UserDeleteView.as_view(), name='delete user'),
)