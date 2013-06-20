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


"""
Jquery will deal with live updating of the favorites button image when it is clicked, but we  need something 
to handle the display on pageload. This can be done by passing in a variable, is_favorite, in the context for
whatever page will display the favoritable items. For example, the following code is a general idea of what to do
"""

#This assumes you've generated a list of all the favoritableItems you want to show
for favoritable in favoritableItems:
  if favoritable.favorited_by.all():
    favoritable.is_favorite = True
  else:
    favoriteable.is_favorite = False
    
    """
    favorites will be a list containing information about each favoritable item, passed in the context
    and allowing for information about each FavoritableItem to be rendered on the viewable page
    """
    favorites[favoritable.id] = {'is_favorite':m.is_favorite} #add other fields to be passed in favs portion of context
    
  data = {'favorites': favorites.items()} #... other fields to be passed in context
    
#Note: Check the html file to see how the context is used
  
