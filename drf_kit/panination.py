from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class Pagination(pagination.PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'pagination': OrderedDict([
                ('count', self.page.paginator.count),
                ('current_page', self.page.number),
                ('page_size', self.page_size),
                ('next', self.get_next_link()),
                ('previous', self.get_previous_link())
            ]),
            'results': data
        })
