from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Branch, Bank, BranchSerializer, BankSerializer
from rest_framework.response import Response
from django.db.models import Q
from .utils import Utils

# Create your views here.
class AutocompleteViewSet(viewsets.GenericViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    http_method_names = ['get']

    def list(self, request):
        q = request.query_params['q']
        limit = int(request.query_params['limit'])
        offset = int(request.query_params['offset'])
        filtered_queryset = self.get_queryset().filter(branch__contains=q).order_by('ifsc')
        queryset = self.filter_queryset(filtered_queryset[offset:(offset+limit)])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BranchesViewSet(viewsets.GenericViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    http_method_names = ['get']

    def list(self, request):
        q = request.query_params['q']
        limit = int(request.query_params['limit'])
        offset = int(request.query_params['offset'])
        if(Utils.is_integer(q)):
            filtered_queryset = self.get_queryset().filter(bank_id=int(q)).order_by('ifsc')
        else:
            filtered_queryset = self.get_queryset().filter(Q(ifsc__iexact=q) | Q(branch__iexact=q) | Q(address__iexact=q) | Q(city__iexact=q) | Q(district__iexact=q) | Q(state__iexact=q) | Q(bank_name__iexact=q)).order_by('ifsc')
        queryset = self.filter_queryset(filtered_queryset[offset:(offset+limit)])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BankViewSet(viewsets.GenericViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    http_method_names = ['get']

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)