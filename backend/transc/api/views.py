from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from .models import User
import json

def index(request):
	return HttpResponse("Hello, world. You're at the transcendence index.")

def test(request):
	return JsonResponse({'foo':'bar'})

def users(request):
	users = User.objects.order_by("name")
	data = serialize('json', list(users), fields=('id','name','fullname'))
	return JsonResponse({'users': data})

#FIXME
def show(request, user_id):
	##user = get_object_or_404(User, pk=user_id)
	try:
		user = User.objects.get(pk=user_id)
		data = serialize('json', list(user), fields=('id','name','fullname'))
	except User.DoesNotExist:
		raise Http404()
	return JsonResponse({'user': data})
