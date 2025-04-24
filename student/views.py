from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatMessage, User, Message
from.forms import MessageForm

@login_required  # L'utilisateur doit être connecté pour accéder au chat
def chat_list(request):
    messages = ChatMessage.objects.filter(receiver=request.user)  # Messages reçus
    messages = Message.objects.all().order_by("-timestamp")  # 📌 Récupérer tous les messages triés par date

    if request.method == "POST":  # 📌 Vérifier si l’utilisateur envoie un message
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)  # 📌 On crée le message mais on ne le sauvegarde pas encore
            message.sender = request.user  # 📌 Associer le message à l’utilisateur connecté
            message.save()  # 📌 Sauvegarde du message
            return redirect("chat_list")  # 📌 Recharger la page pour afficher le nouveau message

    else:
        form = MessageForm()  # 📌 Afficher un formulaire vide si ce n'est pas une requête POST

    return render(request, "chat_list.html", {"messages": messages, "form": form})



@login_required
def send_message(request):
    if request.method == "POST":
        receiver_username = request.POST["receiver"]
        content = request.POST["content"]

        try:
            receiver = User.objects.get(username=receiver_username)
            ChatMessage.objects.create(sender=request.user, receiver=receiver, content=content)
        except User.DoesNotExist:
            return render(request, "send_message.html", {"error": "Utilisateur non trouvé."})

    return redirect("chat_list")

from django.contrib.auth import login

def home(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte automatiquement après inscription
            return redirect("home")  # Redirige vers la page d'accueil
    
    return render(request, "index.html", {"form": form})
    


from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # 📌 Redirige vers la page de connexion
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def logout(request):
    return render(request, "logout.html")


def login(request):
    return render(request,"login.html")