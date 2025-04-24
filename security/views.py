from django.shortcuts import render
from django.http import JsonResponse
from .models import Incident

def home(request):
    return render(request, 'notifications/home.html')


def dashboard(request):
    return render(request, 'dashboard.html')  # Render a template for the dashboard


def report_incident(request):
    if request.method == 'POST':
        data = request.POST
        if 'report_type' in data and 'description' in data:
            incident = Incident.objects.create(
                report_type=data['report_type'],
                description=data['description']
            )
            return JsonResponse({'status': 'success', 'incident_id': incident.id})
        else:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def alert_dashboard(request):
    # Your logic for the alert dashboard goes here
    return render(request, 'dashboard.html')
