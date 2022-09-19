from rest_framework import pagination



class SmallPagination(pagination.PageNumberPagination):
    page_size = 3
    page_query_param = 'sayfa'


class TitlesPagination(pagination.PageNumberPagination):
    page_size = 25
    page_query_param = "p"



# class EntryPagination(pagination.PageNumberPagination):
#     page_size = 1
#     page_query_param = "p"