from django.shortcuts import render, redirect
from .models import Images, Answers, Questions
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from random import randint, sample, choice, shuffle
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'quizzapp/home.html')


def try_it(request):
    id = randint(1, 2)
    question = Questions.objects.filter(id=id)
    question = choice(question)
    question_points = question.points
    question_str = question.question
    n_image = question.n_image
    answers = Answers.objects.filter(question_id=id)
    possible_answers = [ans for ans in answers]
    possible_answers = sample(possible_answers, 4)
    answer = choice(possible_answers)
    answer_definition = answer.definition
    answer = answer.answer
    for i in range(0, len(possible_answers)):
        possible_answers[i] = possible_answers[i].answer
    shuffle(possible_answers)
    image = Images.objects.filter(**{question.category: answer})
    images = list(image)
    images = [im.image_name for im in images]
    images = sample(images, n_image)
    for i in range(0, len(images)):
        images[i] = str(images[i])
        images[i] = 'css/' + images[i] + '.jpg'
    return render(request, 'quizzapp/try.html', {"question": question_str, "question_points": question_points, "answer": answer, "answer_definition": answer_definition, "possible_answers": possible_answers, "images": images})


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account created for  ' + user)

            return redirect('login')
    context = {'form': form}
    return render(request, 'quizzapp/register.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'quizzapp/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def quizz(request):
    return render(request, 'quizzapp/choice.html')


def microscopy(request):
    question = Questions.objects.filter(id=1)
    question = choice(question)
    question_points = question.points
    question_str = question.question
    answers = Answers.objects.filter(question_id=1)
    answer = choice(answers)
    answer_definition = answer.definition
    answer = answer.answer
    image = Images.objects.filter(**{question.category: answer})
    images = list(image)
    images = [im.image_name for im in images]
    images = sample(images, 3)
    for i in range(0, len(images)):
        images[i] = str(images[i])
        images[i] = 'css/' + images[i] + '.jpg'
    return render(request, 'quizzapp/microscopy.html', {"question": question_str,
                                                        "question_points": question_points,
                                                        "answers": answers,
                                                        "answer": answer,
                                                        "answer_definition": answer_definition,
                                                        "images": images,
                                                        "image": image})


def biological(request):
    question = Questions.objects.filter(id=2)
    question = choice(question)
    question_points = question.points
    question_str = question.question
    answers = Answers.objects.filter(question_id=2)
    possible_answers = [ans for ans in answers]
    possible_answers = sample(possible_answers,4)
    answer = choice(possible_answers)
    answer_definition = answer.definition
    answer = answer.answer
    for i in range(0, len(possible_answers)):
        possible_answers[i] = possible_answers[i].answer
    shuffle(possible_answers)
    image = Images.objects.filter(**{question.category: answer})
    images = list(image)
    images = [im.image_name for im in images]
    images = sample(images, 2)
    for i in range(0, len(images)):
        images[i] = str(images[i])
        images[i] = 'css/'+images[i]+'.jpg'
    return render(request, 'quizzapp/biological.html', {"question": question_str,
                                                        "question_points": question_points,
                                                        "answer": answer,
                                                        "answer_definition": answer_definition,
                                                        "possible_answers": possible_answers,
                                                        "images": images})


def explore(request):
    image = Images.objects.all()
    images = list(image)
    image_name = [im.image_name for im in images]
    for i in range(0, len(image_name)):
        image_name[i] = str(image_name[i])
        image_name[i] = 'css/'+image_name[i]+'.jpg'
    for i in range(0, len(images)):
        images[i].image_name = image_name[i]
    return render(request, 'quizzapp/explore.html', {"images": images})