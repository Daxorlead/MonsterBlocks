from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    alignment = models.CharField(max_length=20)
    img = models.ImageField(default="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.istockphoto.com%2Fvectors%2Fblack-comic-cute-monster-vector-vector-id1049255230%3Fk%3D6%26m%3D1049255230%26s%3D612x612%26w%3D0%26h%3D_lgPNrC5ruj24DSadsFFP24r1lxaLSjKY6UVtqUZDXk%3D&f=1&nofb=1")
    ac = models.CharField(max_length=20)
    hp = models.CharField(max_length=20)
    speed = models.CharField(max_length=20)
    str = models.CharField(max_length=20)
    dex = models.CharField(max_length=20)
    con = models.CharField(max_length=20)
    int = models.CharField(max_length=20)
    wis = models.CharField(max_length=20)
    cha = models.CharField(max_length=20)
    skills = models.TextField(max_length=2000, default="")
    senses = models.TextField(max_length=2000)
    languages = models.TextField(max_length=2000, default="")
    cr = models.CharField(max_length=20)
    passives = models.TextField(max_length=2000, default="")
    actions = models.TextField(max_length=2000)
    legendary = models.TextField(max_length=2000, default="")

