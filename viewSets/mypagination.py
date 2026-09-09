from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination,CursorPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'
    page_size_query_param = 'records'
    max_page_size = 7 

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 6
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 4

class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'id'