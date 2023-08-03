from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated

from backend.models.project_models import Requirements, TaskPerProject, Workers



@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def task_per_project(request):
    if request.user.is_authenticated:    
        if request.method == 'POST':
            project_id = request.POST.get('project_id')
            location_id = request.POST.get('location_id')
            task_id = request.POST.get('task_id')
            cost = request.POST.get('cost')

            tasksPerProj = TaskPerProject(project_id=project_id, location_id=location_id, task_id=task_id, cost=cost)

            tasksPerProj.save();
            return JsonResponse({'message': 'saved successfully'})
        
        elif request.method == 'GET':
          tasksPerProjs = TaskPerProject.objects.all()

          data = [
            {
                'id': tasksPerProj.id,
                'name': tasksPerProj.name,
                'description': tasksPerProj.description,
            }
            for tasksPerProj in tasksPerProjs
            ]
          return JsonResponse({'message': 'Successful', 'data': data, 'status': 200}, status=200)
    else:
        return JsonResponse({'message': 'Unauthorized', 'status': 401}, status=401)   


@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def workers(request):
    if request.user.is_authenticated:    
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            location_id = request.POST.get('location_id')
            task_id = request.POST.get('task_id')
            days = request.POST.get('days')
            payment = request.POST.get('payment')

            workers = Workers(first_name=first_name,last_name=last_name, location_id=location_id, task_id=task_id, days=days, payment=payment)

            workers.save();
            return JsonResponse({'message': 'saved successfully'})
        
        elif request.method == 'GET':
          workers = Workers.objects.all()

          data = [
            {
                'id': worker.id,
                'first_name': worker.first_name,
                'last_name': worker.last_name,
                'location_id': worker.location_id,
                'task_id': worker.task_id,
                'days': worker.days,
                'payment': worker.payment,
            }
            for worker in workers
            ]
          return JsonResponse({'message': 'Successful', 'data': data, 'status': 200}, status=200)
    else:
        return JsonResponse({'message': 'Unauthorized', 'status': 401}, status=401)
    

@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def requirements(request):
    if request.user.is_authenticated:    
        if request.method == 'POST':
            location_id = request.POST.get('location_id')
            task_id = request.POST.get('task_id')
            equipment_id = request.POST.get('equipment_id')
            quantity = request.POST.get('quantity')
            amount = request.POST.get('amount')

            requirements = Requirements(equipment_id=equipment_id,quantity=quantity, location_id=location_id, task_id=task_id, amount=amount)

            requirements.save();
            return JsonResponse({'message': 'saved successfully'})
        
        elif request.method == 'GET':
          requirements = Requirements.objects.all()

          data = [
            {
                'id': requirement.id,
                'name': requirement.name,
                'description': requirement.description,
            }
            for requirement in requirements
            ]
          return JsonResponse({'message': 'Successful', 'data': data, 'status': 200}, status=200)
    else:
        return JsonResponse({'message': 'Unauthorized', 'status': 401}, status=401)