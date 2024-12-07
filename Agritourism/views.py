from django.shortcuts import render
from django.utils import translation

# Create your views here.
def index(request):
    return render(request, 'index.html')

def farmer_view(request):
    return render(request, 'farmer.html')

def register_farmer(request):
    return render(request, 'signup.html')

def courses_view(request):
    return render(request, 'courses.html')

def products_view(request):
    return render(request, 'products.html')
# views.py

from django.shortcuts import render
from .models import Farm

def lend_a_farm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        farm_name = request.POST.get('farm-name')
        location = request.POST.get('location')
        type_of_soil = request.POST.get('type-of-soil')
        type_of_crop = request.POST.get('type-of-crop')
        description = request.POST.get('description')
        
        # Create and save a new Farm instance
        farm = Farm.objects.create(
            name=name,
            email=email,
            phone=phone,
            farm_name=farm_name,
            location=location,
            type_of_soil=type_of_soil,
            type_of_crop=type_of_crop,
            description=description
        )
        farm.save()
        return redirect('centres')  # Redirect to a success page after submission
    else:
        return render(request, 'lendafarm.html')  # Render the form page for GET requests

def centres(request):
    # Fetch all farm objects from the database
    farms = Farm.objects.all()
    # Pass the farms variable to the template
    return render(request, 'centres.html', {'farms': farms})

# def agritourism_centres(request):
#     # Fetch all farm details from the database
#     farms = Farm.objects.all()
#     context = {
#         'farms': farms
#     }
#     return render(request, 'agritourism_centres.html', context)

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_farmer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return render(request, 'signup.html')
            
            # Create a new User instance
            user = User.objects.create_user(username=username, password=password)
            user.save()
            
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')  # Redirect to the login page after successful signup
        else:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')  # Return to the signup page with an error
    else:
        if request.user.is_authenticated:
            return redirect('index')  # Redirect to the farmer's page if already logged in
        else:
            return render(request, 'signup.html')


from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # User authentication successful, log in the user
            auth_login(request, user)
            return redirect('index')  # Redirect to farmer page after successful login
        else:
            # User authentication failed, show error message
            messages.error(request, 'Invalid username or password')
            return redirect('login')  # Redirect to login page with error message
    else:
        return render(request, 'login.html')   
    
from .models import Blog
def blog_view(request):
    # Fetch all blog objects from the database
    blogs = Blog.objects.all()
    # Pass the blogs variable to the template
    return render(request, 'blog.html', {'blogs': blogs})



# views.py
from django.shortcuts import render, redirect
from .models import Blog

def write_blog_view(request):
    if request.method == 'POST':
        title = request.POST.get('blog-title')
        content = request.POST.get('blog-content')
        
        # Ensure that both fields are provided
        if title and content:
            # Create a new Blog instance and save it to the database
            blog = Blog.objects.create(title=title, content=content)
            return redirect('blog')  # Redirect to the blog page after successful submission
        else:
            # Handle error case (e.g., display a message or re-render the form)
            return render(request, 'writeblog.html', {'error': 'Both title and content are required'})

    return render(request, 'writeblog.html')


from django.utils.translation import activate
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer, Comment
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import get_language
from django.utils.translation import activate
from django.shortcuts import render, redirect
from .models import Question


def community(request):
    questions = Question.objects.all()
    
    if request.method == 'POST' and 'language' in request.POST:
        lang = request.POST.get('language')
        translation.activate(lang)  # Change the language dynamically
        request.session['django_language'] = lang  # Save the language in session using 'django_language'
        return redirect('community')  # Redirect after language change to refresh the page with new language
    
    return render(request, 'community.html', {'questions': questions})


from django.shortcuts import render
from googletrans import Translator

def translate_text(request):
    translated_text = None
    if request.method == "POST":
        text = request.POST.get("text")
        language = request.POST.get("language")
        translator = Translator()
        translated_text = translator.translate(text, dest=language).text

    return render(request, "translate_text.html", {"translated_text": translated_text})




def resource(request):
    return render(request, 'resource.html')


def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'question_detail.html', {'question': question})

def add_answer(request, question_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Answer.objects.create(question_id=question_id, content=content)
    return redirect('community')

def fetch_answers(request, question_id):
    answers = Answer.objects.filter(question_id=question_id).values('content')
    return JsonResponse(list(answers), safe=False)

def add_question(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Question.objects.create(title=title, content=content)
            return redirect('community')
    return render(request, 'add_question.html')




