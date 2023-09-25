from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from mfalcon.models import route
import json
from django.views.decorators.csrf import csrf_exempt
import mfalcon.r2d2


# Default mfaclon Onboard Computer view
def index(request):
    return render(request, 'mfcomputer.html')


# Upload file view
@csrf_exempt
def upload_file(request):

    if request.method == 'POST' and request.FILES.get('falcon') and request.FILES.get('empire'):
        print("Falcon file detected")
        uploaded_file = request.FILES['falcon']
        
        # Falcon JSON file parsing + verification
        try:
            falcon_data = json.loads(uploaded_file.read())
            for key in ['autonomy', 'departure', 'arrival', 'routes_db']:
                assert key in falcon_data.keys()
        except AssertionError:
            return JsonResponse({'message': 'Invalid Falcon data'})
        print(falcon_data)

        print("Empire file detected")
        uploaded_file = request.FILES['empire']
        
        # Falcon JSON file parsing + verification
        try:
            empire_data = json.loads(uploaded_file.read())
            for key in ['countdown', 'bounty_hunters']:
                assert key in empire_data.keys()
        except AssertionError:
            return JsonResponse({'message': 'Invalid Empire data'})
        print(empire_data)

        # Compute odds of survival
        r2 = mfalcon.r2d2.R2D2(falcon_data, empire_data)
        odds = r2.give_odds()
        
        return JsonResponse({'message': str(odds) + '% of survival.'})
    else:
        return JsonResponse({'message': 'No file uploaded'}, status=400)

