from django.shortcuts import render
from django.http import HttpResponse
from battle_log.models import BattleLogCSV

def download(request):

    if not request.META['QUERY_STRING']:
        return HttpResponse('404', content_type='text')
    key = request.META['QUERY_STRING']
    try:
        csv_log = BattleLogCSV.objects.get(title=key)
    except BattleLogCSV.DoesNotExist:
        return HttpResponse('404', content_type='text')
    
    response = HttpResponse(csv_log.data, content_type='text')
    # response['Content-Disposition'] = 'attachment; filename="{}"'.format(csv_log.title+'.csv')
    return response
