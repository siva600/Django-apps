from rest_framework.pagination import LimitOffsetPagination


# overwriting the max limit for the responses generated for a single API request
class LimitOffsetPaginationWithMaxLimit(LimitOffsetPagination):
    max_limit = 10
