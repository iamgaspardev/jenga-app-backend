# Authenticated views.
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from backend.models.setups_models import Locations, Projects, Tasks
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


            projects = Projects(name=name, description=description)

            projects.save();
            return JsonResponse({'message': 'Project saved successfully'})
        
        elif request.method == 'GET':
          projects = Projects.objects.all()

          data = [
            {
                'id': project.id,
                'name': project.name,
                'description': project.description,
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


            locations = Locations(name=name, description=description, project_id=project_id)

            locations.save();
            return JsonResponse({'message': 'location saved successfully'})
        
        elif request.method == 'GET':
           locations = Locations.objects.all()

           data = [
            {
                'id': location.id,
                'name': location.name,
                'description': location.description,
                'project_id': location.project_id
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


            tasks = Tasks(name=name, description=description, project_id=project_id)

            tasks.save();
            return JsonResponse({'message': 'task saved successfully'})
        
        elif request.method == 'GET':
           tasks = Tasks.objects.all()

           data = [
            {
                'id': task.id,
                'name': task.name,
                'description': task.description,
                'project_id': task.project_id
            }
            for task in tasks
            ]
           return JsonResponse({'message': 'Successful', 'data': data, 'status': 200}, status=200)
    
        
        
    else:
        return JsonResponse({'message': 'Unauthorized', 'status': 401}, status=401)
    
     