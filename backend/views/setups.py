# Authenticated views.
from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from backend.models.setups_models import Equipments, Locations, Projects, Tasks
from rest_framework.permissions import IsAuthenticated



# Create your views here.
@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def project(request):
    if request.user.is_authenticated:    
        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')


            projects = Projects(project_name=name, project_description=description)

            projects.save();
            return JsonResponse({'message': 'Project saved successfully'})
        
        elif request.method == 'GET':
          projects = Projects.objects.all()

          data = [
            {
                'id': project.id,
                'name': project.project_name,
                'description': project.project_description,
            }
            for project in projects
            ]
          return JsonResponse({'message': 'Successful', 'data': data, 'status': 200}, status=200)
    else:
        return JsonResponse({'message': 'Unauthorized', 'status': 401}, status=401)
    
    
@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])    
@csrf_exempt
def location(request):
    if request.user.is_authenticated:
        # User is authenticated. You can access the authenticated user using request.user
        user = request.user

        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            project_id = request.POST.get('project_id')
            budget = request.POST.get('budget')


            locations = Locations(location_name=name, location_description=description, project_id_id=project_id, budget=budget)

            locations.save();
            return JsonResponse({'message': 'location saved successfully'})
        
        elif request.method == 'GET':
           locations = Locations.objects.select_related('project_id')

           data = [
            {
                'id': location.id,
                'name': location.location_name,
                'description': location.location_description,
                'budget' : location.budget,
                'project': model_to_dict(location.project_id),
            }
            for location in locations
            ]
           return JsonResponse({'message': 'Successful', 'data': data, 'status': 200}, status=200)


        
    else:
        return JsonResponse({'message': 'Unauthorized', 'status': 401}, status=401)


@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def task(request):
    if request.user.is_authenticated:
        # User is authenticated. You can access the authenticated user using request.user
        user = request.user

        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            project_id = request.POST.get('project_id')


            tasks = Tasks(task_name=name, task_description=description, project_id_id=project_id)

            tasks.save();
            return JsonResponse({'message': 'task saved successfully'})
        
        elif request.method == 'GET':
           tasks = Tasks.objects.all()

           data = [
            {
                'id': task.id,
                'name': task.task_name,
                'description': task.task_description,
                'project': model_to_dict(task.project_id)
            }
            for task in tasks
            ]
           return JsonResponse({'message': 'Successful', 'data': data, 'status': 200}, status=200)
    
        
        
    else:
        return JsonResponse({'message': 'Unauthorized', 'status': 401}, status=401)
    
@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def equipment(request):
    if request.user.is_authenticated:
        # User is authenticated. You can access the authenticated user using request.user
        user = request.user

        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            task_id = request.POST.get('task_id')


            equipments = Equipments(equipment_name=name, equipment_description=description, task_id_id=task_id)

            equipments.save();
            return JsonResponse({'message': 'equipment saved successfully'})
        
        elif request.method == 'GET':
           equipments = Equipments.objects.all()

           data = [
            {
                'id': equipment.id,
                'name': equipment.equipment_name,
                'description': equipment.equipment_description,
                'task': model_to_dict(equipment.task_id)
            }
            for equipment in equipments
            ]
           return JsonResponse({'message': 'Successful', 'data': data, 'status': 200}, status=200)
    
        
        
    else:
        return JsonResponse({'message': 'Unauthorized', 'status': 401}, status=401)