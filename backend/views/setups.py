# Authenticated views.
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from backend.models.setups_models import Equipments, Locations, Projects, Tasks
from rest_framework.permissions import IsAuthenticated



# Create your views here.
@api_view(['POST','GET','DELETE'])
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
    
    
@api_view(['POST','GET','DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])    
@csrf_exempt
def location(request):
    if request.user.is_authenticated:
        # User is authenticated. You can access the authenticated user using request.user
        user = request.user

        if request.method == 'POST':
            name = request.POST.get('name')
            leader_name = request.POST.get('leader_name')
            supervisor = request.POST.get('supervisor')
            project_category = request.POST.get('project_category')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            budget = request.POST.get('budget')


            locations = Locations(location_name=name, leader_name=leader_name, supervisor=supervisor, budget=budget, project_category=project_category, start_date=start_date,end_date=end_date)
            print(locations)
            locations.save()
            return JsonResponse({'message': 'location saved successfully'})
        
        elif request.method == 'GET':
           locations = Locations.objects.all()

           data = [
            {
                'id': location.id,
                'name': location.location_name,
                'leader_name': location.leader_name,
                'budget' : location.budget,
                'supervisor': location.supervisor,
                'project_category': location.project_category,
                'start_date': location.start_date,
                'end_date': location.end_date,
                # 'project': model_to_dict(location.project_id),

            }
            for location in locations
            ]
           return JsonResponse({'message': 'Successful', 'data': data, 'status': 200}, status=200)
        
        elif request.method == 'DELETE':
           locations = Locations.objects.all()
           pk = request.POST.get('pk')
           locations = get_object_or_404(Locations, pk=pk)
           locations.delete()
           return JsonResponse({'message': 'Successful', 'data': data, 'status': 200}, status=200)


        
    else:
        return JsonResponse({'message': 'Unauthorized', 'status': 401}, status=401)


@api_view(['POST','GET','DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def location_delete(request, pk):
    
    if request.user.is_authenticated:
        if request.method == 'DELETE':
           locations = get_object_or_404(Locations, id=pk)
           locations.delete()
           return JsonResponse({'message': 'Successful Deleted', 'status': 200}, status=200)

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