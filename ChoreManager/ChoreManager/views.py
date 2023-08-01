from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from .models import User, ChoreList, Chore
from .serializers import UserSerializer, ChoreListSerializer, ChoreSerializer
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
@parser_classes([JSONParser])
@csrf_exempt
def index(request):
    return JsonResponse({'message': 'This is an apartment chore manager'})

@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse({'users': serializer.data}, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)


@api_view(['GET', 'DELETE'])
@parser_classes([JSONParser])
def user_detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    elif request.method =='DELETE':
        user.delete()
        return JsonResponse(status=204)


@api_view(['POST','GET'])
@parser_classes([JSONParser])
@csrf_exempt
def chore_lists(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChoreListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == 'GET':
        chore_lists = ChoreList.objects.all()
        serializer = ChoreListSerializer(chore_lists, many=True)
        return JsonResponse({'chore_lists': serializer.data})

@api_view(['GET','DELETE'])
@parser_classes([JSONParser])
@csrf_exempt
def chore_list_detail(request, chore_list_id):
    try:
        chore_list = ChoreList.objects.get(pk=chore_list_id)
    except ChoreList.DoesNotExist:
        return JsonResponse({'error': 'ChoreList not found'}, status=404)

    if request.method == 'GET':
        serializer = ChoreListSerializer(chore_list)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        chore_list.delete()
        return JsonResponse({'message': 'Chore list deleted successfully'})

@api_view(['POST','GET'])
@parser_classes([JSONParser])
def chore(request):
    if request.method == 'GET':
        chores = Chore.objects.all()
        serializer = ChoreSerializer(chores, many=True)
        return JsonResponse({'chores': serializer.data})
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@api_view(['GET', 'DELETE', 'PUT'])
@parser_classes([JSONParser])
def chore_detail(request, chore_id):
    try:
        chore = Chore.objects.get(pk=chore_id)
    except Chore.DoesNotExist:
        return JsonResponse({'error': 'Chore not found'}, status=404)
    if request.method == 'GET':
        serializer = ChoreSerializer(chore)
        return JsonResponse(serializer.data)
    elif request.method =='DELETE':
        chore.delete()
        return JsonResponse(status=204)
    elif request.method == 'PUT':
        serializer = ChoreSerializer(chore, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'message': 'Chore updated successfully'})
