from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

#---------------------------------------------------#
def login_view(request):
    return HttpResponse('Tela de login')

def logout_view(request):
    return HttpResponse('Tela de logout')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rota_protegida(request):
    return Response({'message':'Você está autenticado!'})