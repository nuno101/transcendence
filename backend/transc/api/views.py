from django.http import HttpResponse, JsonResponse, Http404
from django.core.serializers import serialize
from .models import User

def index(request):
	return HttpResponse("Hello, world. You're at the transcendence index.")

def test(request):
	return JsonResponse({'foo':'bar'})

def user_list(request):
	if request.method == 'GET':
		users = User.objects.order_by("name")
		data = serialize('json', list(users), fields=('id','name','fullname'))
		return JsonResponse({'users': data})

	if request.method == 'POST':
		# https://www.youtube.com/watch?v=i5JykvxUk_A
		return JsonResponse({'TODO':'1'})

#FIXME
def user_detail(request, user_id):
	try:
		user = User.objects.get(pk=user_id)
		data = serialize('json', [user], fields=('id','name','fullname','created_at', 'updated_at'))
	except User.DoesNotExist:
		raise Http404()
	return JsonResponse({'user': data})
