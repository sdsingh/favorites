"""Add the following to any existing views.py file which supports the django login module"""
from django.contrib.auth.decorators import login_required


"""Warning: If the page containing your FavoritedItems makes use of data in request.GET, 
make sure to add the following to the controller for that page, substituting the correct names:

def favorited_items_page(request):
  if request.is_ajax():
      if INSERT_ANY_VARIABLES_USED_HERE in request.GET:
        #Do whatever it was you were doing previously
"""


@login_required
def favorite(request):
    if request.POST.has_key('id'):
        id = request.POST['id']
        id = id.rsplit('_')
        id = int(id[1])
        m = Media.objects.get(pk=id)
        m.favorited_by.add(request.user.get_profile())
        m.save()
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if request.META.has_key('HTTP_REFERRER'):
      #return HttpResponseRedirect('user/')
    	return HttpResponseRedirect(request.META['HTTP_REFERRER'])
    return HttpResponseRedirect('/')


@login_required
def delete_favorite(request):
    if request.POST.has_key('id'):
        id = request.POST['id']
        id = id.rsplit('_')
        id = int(id[1])
        m = Media.objects.get(pk=id)
        m.favorited_by.remove(request.user.get_profile())
        m.save()
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if request.META.has_key('HTTP_REFERRER'):
        return HttpResponseRedirect(request.META['HTTP_REFERRER'])
    return HttpResponseRedirect('/')
