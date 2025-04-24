from django.db import models

from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Lien avec User
    age = models.IntegerField()
    class_name = models.CharField(max_length=50)  # Nom de la classe (ex: Terminale S)

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)  # Matière enseignée

    def __str__(self):
        return self.user.username
    

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[("sent", "Sent"), ("seen", "Seen")], default="sent")

    def __str__(self):
        return f"De {self.sender.username} à {self.receiver.username}"


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)  # 📌 Expéditeur
    content = models.TextField()  # 📌 Contenu du message
    timestamp = models.DateTimeField(auto_now_add=True)  # 📌 Date d’envoi

    def __str__(self):
        return f"Message de {self.sender.username} le {self.timestamp}"