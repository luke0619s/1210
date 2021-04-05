from django.shortcuts import render
from django.http import HttpResponse
import json
from random import randrange
from pyecharts.charts import Bar
from pyecharts import options as opts
from rest_framework.views import APIView
from idlelib.iomenu import encoding
from .models import location
from _threading_local import local
from pyasn1.compat.octets import null
def main(request):
    
    return render(request, 'main/index.html', locals())
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
    years = range(1970, 2021)
    months = range(1, 13)
    days = range(1, 31)
    location1 = location.objects.filter(year=30)
    
    return render(request, 'main/government_data.html', locals())

def realtime(request):
    local = location.objects.all()
    return render(request, 'main/realtime.html', locals())

def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response

def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)

def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)

JsonResponse = json_response
JsonError = json_error

def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["2014", "2016", "2017", "2018", "2019", "2020"])
        .add_yaxis("臺北監測站(溫度)", [30,25,27,36,32,41])
        .set_global_opts(title_opts=opts.TitleOpts(title="測試", subtitle="測試副標題"))
        .dump_options_with_quotes()
    )
    return c
def bar_base2() -> Bar:
    c = (
        Bar()
        .add_xaxis(["2015", "2016", "2017", "2018", "2019", "2020"])
        .add_yaxis("新莊監測站(溫度)", [30,25,27,36,32,41])
        .set_global_opts(title_opts=opts.TitleOpts(title="測試", subtitle="測試副標題"))
        .dump_options_with_quotes()
    )
    return c
def bar_base3() -> Bar:
    c = (
        Bar()
        .add_xaxis(["2015", "2016", "2017", "2018", "2019", "2020"])
        .add_yaxis("南港監測站(溫度)", [30,25,27,36,32,41])
        .set_global_opts(title_opts=opts.TitleOpts(title="測試", subtitle="測試副標題"))
        .dump_options_with_quotes()
    )
    return c
def bar_base4() -> Bar:
    c = (
        Bar()
        .add_xaxis(["2015", "2016", "2017", "2018", "2019", "2020"])
        .add_yaxis("中山監測站(溫度)", [22,23,21,45,38,66])
        .set_global_opts(title_opts=opts.TitleOpts(title="測試", subtitle="測試副標題"))
        .dump_options_with_quotes()
    )
    return c
def bar_base5() -> Bar:
    c = (
        Bar()
        .add_xaxis(["2015", "2016", "2017", "2018", "2019", "2020"])
        .add_yaxis("信義監測站(溫度)", [77,55,67,56,52,21])
        .set_global_opts(title_opts=opts.TitleOpts(title="測試", subtitle="測試副標題"))
        .dump_options_with_quotes()
    )
    return c
def bar_base6() -> Bar:
    c = (
        Bar()
        .add_xaxis(["2015", "2016", "2017", "2018", "2019", "2020"])
        .add_yaxis("永春監測站(溫度)", [11,45,77,56,22,41])
        .set_global_opts(title_opts=opts.TitleOpts(title="測試", subtitle="測試副標題"))
        .dump_options_with_quotes()
    )
    return c

class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base()))

class ChartView2(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base2()))
class ChartView3(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base3()))
class ChartView4(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base4()))
class ChartView5(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base5()))
class ChartView6(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base6()))

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/luke.html')
