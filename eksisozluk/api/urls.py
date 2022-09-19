from django.urls import path
from django.urls import include
#from .views import EntryCreateApiView, TitleApiView, TitleDetailApiView, CreateTitleApiView, EntryDetailApiView
from .views import EntriesApiView
from .views import TitlesList, TagViewset, TitleDetail, CreateTitleApiView, EntryCreateApiView, EntriesDetailsApiView,FacebookLogin, BlogCreateGenericView, BlogRUDGeneriApiView, BlogListApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()




urlpatterns = [
    path('', include(router.urls)),

    path("titles/", TitlesList.as_view(), name="titles"),
    path("titles/<int:entry_pk>/", EntriesDetailsApiView.as_view(), name="title-detail"),
    path("create-title/", CreateTitleApiView.as_view(), name="create-title"),

    # path("entries/<int:pk>/", EntriesApiView.as_view(), name="title-detail"),

    path("entries/<int:entry_pk>/", EntriesApiView.as_view(), name="title-entries" ),
    path('create-entry/<int:title_pk>', EntryCreateApiView.as_view(), name='entry-create'),

    path("blog/create", BlogCreateGenericView.as_view(), name='create-blog' ),  
    path("blog/<int:id>", BlogRUDGeneriApiView.as_view(), name='create-crud' ),
    path("blogs/", BlogListApiView.as_view(), name='list-blogs' ),
    

    path('user/', include('dj_rest_auth.urls')),
    path('user/registration/', include('dj_rest_auth.registration.urls')),
    path('user/login/fb', FacebookLogin.as_view(),name='fb_login'),


]