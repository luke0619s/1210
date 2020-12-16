from django.shortcuts import render
def main(request):
    return render(request, 'main/index.html')
def station(request):
    return render(request, 'main/station.html')
def sort(request):
    return render(request, 'main/sort.html')
def sign(request):
    return render(request, 'main/sign.html')
def station_history(request):
    return render(request, 'main/station_history.html')
def setting(request):
    return render(request, 'main/setting.html')
def upgrade_member(request):
    return render(request, 'main/upgrade_member.html')
def government(request):
    return render(request, 'main/government_data.html')
def realtime(request):
    return render(request, 'main/realtime.html')