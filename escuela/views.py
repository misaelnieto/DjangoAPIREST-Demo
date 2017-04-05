from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from escuela.models import Alumno, Carrera
from escuela.serializers import AlumnoSerializer, CarreraSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """	
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json; charset=utf-8'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def alumno_list(request):
    """
    List all code alumno, or create a new alumno.
    """
    if request.method == 'GET':
        alumnos = Alumno.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AlumnoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def alumno_detail(request, pk):
    """
    Retrieve, update or delete a alumno.
    """
    try:
        alumno = Alumno.objects.get(pk=pk)
    except Alumno.DoesNotExist:
        return HttpResponse(status=404)    

    if request.method == 'GET':
        serializer = AlumnoSerializer(alumno)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AlumnoSerializer(alumno, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)    
    elif request.method == 'DELETE':
        alumno.delete()
        return HttpResponse(status=204)

@csrf_exempt
def carrera_list(request):
    """
    List all code carrera, or create a new carrera.
    """
    if request.method == 'GET':
        carreras = Carrera.objects.all()
        serializer = CarreraSerializer(carreras, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CarreraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def carrera_detail(request, pk):
    """
    Retrieve, update or delete a carrera.
    """
    try:
        carrera = Carrera.objects.get(pk=pk)
    except Carrera.DoesNotExist:
        return HttpResponse(status=404)    

    if request.method == 'GET':
        serializer = CarreraSerializer(carrera)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CarreraSerializer(carrera, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)    
    elif request.method == 'DELETE':
        carrera.delete()
        return HttpResponse(status=204)