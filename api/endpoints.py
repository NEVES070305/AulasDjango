from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def getData(request):
    if request.method == 'GET':
      fruta = {'nome': 'Mirtilo', 'citrico': True}
    elif request.method == 'POST':
      fruta = {'nome': 'Melancia', 'citrico': False}
    elif request.method == 'PUT':
      fruta = {'nome': 'Limão', 'citrico': True}
    elif request.method == 'PATCH':
      fruta = {'nome': 'Banana', 'citrico': False}
    elif request.method == 'DELETE':
      fruta = {'nome': 'Tangerina', 'citrico': True}
    return Response(fruta)

@api_view([])