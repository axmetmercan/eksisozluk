from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework import generics
from .models import *
from .serializers import CreateEntrySerializer, TagSerializer, TitleDetailSerializer, TitleSerialier, EntrySerializer, TitleDetailSerializerMany, BlogSerializer
from rest_framework import permissions
from .permissions import IsAuthenticatedAndBelongsToOrAdmin, IsAuthenticatedAndBelongsTo, TitleCreatePermission
from .pagination import SmallPagination, TitlesPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.parsers import MultiPartParser, FormParser



#Social Login
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
# Create your views here.

# Taglari Listele # Herkese
class TagViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# Titlelari Listele # Herkese
class TitlesList(generics.ListAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleDetailSerializer
    pagination_class = SmallPagination

#Title Create APIView #Statüsü Professional Olan Kişi Title Açabilir
class CreateTitleApiView(generics.ListCreateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerialier
    permission_classes = [TitleCreatePermission, permissions.IsAuthenticated]

# Title Detaylari ve Entryleri Listele
class TitleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleDetailSerializer
    permission_classes = [IsAuthenticatedAndBelongsToOrAdmin]
    pagination_class = TitlesPagination


# Entryleri Listele #Listelemek Herkesei, Silme Güncellemei, ve sahibine
class EntriesApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Explanation.objects.all()
    serializer_class = EntrySerializer
    lookup_url_kwarg = 'entry_pk'

    permission_classes = [IsAuthenticatedAndBelongsTo]


class EntriesDetailsApiView(generics.ListAPIView):
    serializer_class = EntrySerializer
    parser_classes = [permissions.AllowAny]
    lookup_url_kwarg = 'title_pk'
    pagination_class = TitlesPagination

    def get_queryset(self):
        title_pk = self.kwargs.get(self.lookup_url_kwarg)
        return Explanation.objects.filter(title = title_pk)

# Entry Oluştur
class EntryCreateApiView(generics.CreateAPIView):
    queryset = Explanation.objects.all()
    serializer_class = CreateEntrySerializer
    parser_classes = (MultiPartParser, FormParser)

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        userr = self.request.user
        title_pk = self.kwargs.get('title_pk')
        title = get_object_or_404(Title, pk = title_pk)
        serializer.save(title=title, user = userr)


class BlogCreateGenericView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        userr = self.request.user
        status = True
        like = 0

        serializer.save(user = userr, status = status, like = like)        



class BlogRUDGeneriApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticatedAndBelongsTo]


class BlogListApiView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    



class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter












# class TitleApiView(generics.ListAPIView):
#     queryset = Title.objects.all()
#     serializer_class = TitleSerialier
#     permission_classes = [permissions.AllowAny]
#     pagination_class = SmallPagination
    


# class TitleDetailApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Title.objects.all()
#     serializer_class = TitleDetailSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# # class EntryCreateApiView(generics.CreateAPIView):
# #     queryset = Explanation.objects.all()
# #     serializer_class = EntrySerializer
# #     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# #     def perform_create(self, serializer):
# #         title_pk = self.kwargs.get('title_pk')
# #         title = get_object_or_404(Title, pk=title_pk)
# #         serializer.save(title = title)

# class EntryDetailApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Explanation.objects.all()
#     serializer_class = EntrySerializer
#     permission_classes = [IsAuthenticatedAndBelongsToOrAdmin]   



# class TitleViewset(mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     queryset = Title.objects.all()
#     serializer_class = TitleSerialier
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    

