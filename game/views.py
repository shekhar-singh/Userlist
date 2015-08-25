from django.shortcuts import render_to_response,render

from django.http import HttpResponse

from game.forms import CategoryForm

from models import Category
# Create your views here.
#from django.views.generic import TemplateView
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
        # Note the key boldmessage is the same as {{ boldmessage }} in the template!
  
    a=Category.objects.all()
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render_to_response('index.html', {'a':a})


def detail(request, question_id):
    return HttpResponse("hi %s." % question_id)


#class AboutView(TemplateView):
 #   template_name = "about.html"

 

def add_user(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'add_user.html', {'form': form})


