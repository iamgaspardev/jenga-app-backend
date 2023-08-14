import json
from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated

from backend.models.project_models import Requirements, TaskPerProject, Workers
from backend.models.setups_models import Locations



@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def process_data_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = json.loads(request.body)
            
            location_id = data['location_id']
            print("Raw data received:", location_id)
            data = data["data"]
            location, created = Locations.objects.get_or_create(id=location_id)
            
            # Process and save tasks
            tasks = data.get('task', [])
            for task_data in tasks:
                task = TaskPerProject.objects.create(
                    location_id=location,
                    name=task_data["name"],
                    cost=task_data["cost"]
                )
                task_id = task.id  # Get the ID of the created task
                
                # Process and save equipment for this task
                equipment_list = data.get('equipment', [])
                for equipment_data in equipment_list:
                    # if "task_id" in equipment_data and equipment_data["task_id"] == task_id:
                    Requirements.objects.create(
                            location_id=location,
                            task_id=task,
                            name=equipment_data["equipment_name"],
                            quantity=equipment_data["quantity"],
                            amount=equipment_data["cost"],
                        )
                
                # Process and save workers for this task
                workers_list = data.get('workers', [])
                for worker_data in workers_list:
                    # if "task_id" in worker_data and worker_data["task_id"] == task_id:
                    Workers.objects.create(
                            location_id=location,
                            task_id=task,
                            full_name=worker_data["full_name"],
                            payment=worker_data["salary"],
                        )

            return JsonResponse({'message': 'Data processed successfully', 'status': 200}, status=200)

        elif request.method == 'GET':
            tasksPerProjs = TaskPerProject.objects.all()

            data = [
                {
                    'id': tasksPerProj.id,
                    'cost': tasksPerProj.cost,
                    'location': model_to_dict(tasksPerProj.location_id),
                    'task': model_to_dict(tasksPerProj.task_id),
                    'onprogress': tasksPerProj.onprogress
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
def task_per_location(request):
    if request.user.is_authenticated:    
        if request.method == 'POST':
            location_id = request.POST.get('location_id')
            task_id = request.POST.get('task_id')
            cost = request.POST.get('cost')

            tasksPerLoc = TaskPerProject(location_id_id=location_id, task_id_id=task_id, cost=cost)

            tasksPerLoc.save();
            return JsonResponse({'message': 'saved successfully'})
        
        elif request.method == 'GET':
          tasksPerProjs = TaskPerProject.objects.all()

          data = [
            {
                'id': tasksPerProj.id,
                'name': tasksPerProj.name,
                'cost': tasksPerProj.cost,
                'location': model_to_dict(tasksPerProj.location_id),
                'onprogress': tasksPerProj.onprogress
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

            workers = Workers(first_name=first_name,last_name=last_name, location_id_id=location_id, task_id_id=task_id, days=days, payment=payment)

            workers.save();
            return JsonResponse({'message': 'saved successfully'})
        
        elif request.method == 'GET':
          workers = Workers.objects.all()

          data = [
            {
                'id': worker.id,
                'full_name': worker.full_name,
                'location': model_to_dict(worker.location_id),
                'task': model_to_dict(worker.task_id),
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

            requirements = Requirements(equipment_id_id=equipment_id,quantity=quantity, location_id_id=location_id, task_id_id=task_id, amount=amount)

            requirements.save();
            return JsonResponse({'message': 'saved successfully'})
        
        elif request.method == 'GET':
          requirements = Requirements.objects.all()

          data = [
            {
                'id': requirement.id,
                'location': model_to_dict(requirement.location_id),
                'equipment': model_to_dict(requirement.equipment_id),
                'task': model_to_dict(requirement.task_id),
                'quantity': requirement.quantity,
                'amount': requirement.amount,
            }
            for requirement in requirements
            ]
          return JsonResponse({'message': 'Successful', 'data': data, 'status': 200}, status=200)
    else:
        return JsonResponse({'message': 'Unauthorized', 'status': 401}, status=401)