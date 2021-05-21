from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Branch, Bank, BranchSerializer, BankSerializer
from rest_framework.response import Response
from django.db.models import Q
from .utils import Utils
import math

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
        total_page_count = int(math.ceil(filtered_queryset.count() / limit))
        queryset = self.filter_queryset(filtered_queryset[offset:(offset+limit)])

        serializer = self.get_serializer(queryset, many=True)
        final_data = {'total_page_count': total_page_count, 'result': serializer.data};
        return Response(final_data)


class IFSCViewSet(viewsets.GenericViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    http_method_names = ['get']

    def list(self, request):
        q = request.query_params['q']
        ifscs = q.split(',')
        filter = Q(ifsc = ifscs[0])
        for i in range(1, len(ifscs)):
            filter = filter | Q(ifsc = ifscs[i])
        queryset = self.filter_queryset(self.get_queryset().filter(filter))

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)