from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.utils import timezone

def index(request):
	session_id=request.session.session_key

	# Get the current URL
	current_url = request.build_absolute_uri()

	# new_data=isiweb(nama_session=session_id,halaman=current_url)
	# new_data.save()
	current_timestamp = timezone.now()
	return render(request, 'index.html', {'session_id': session_id, 'current_url': current_url, 'current_timestamp':current_timestamp})