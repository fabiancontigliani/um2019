

# Create your views here.


from django.shortcuts import render

from .models import Djeet

def feed(request):
  userids = []
 
  for mfuser in request.user.microblprofile.follows.all():
    userids.append(mfuser.id)
  
  userids.append(request.user.id)
  djeets = Djeet.objects.filter(user_id__in=userids)[0:25]

  return render(request, 'feed.html', {'djeets': djeets})
