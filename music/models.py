'''
from music.models import Album , Song
Album.objects.all()

a = Album(artist="Taylor Swift", albumTitle="Red" , genre="Pop", album_logo="https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.taylorguitars.com%2Fsites%2Fdefault%2Ffiles%2Ftg-logo-red-2x.jpg&imgrefurl=https%3A%2F%2Fwww.taylorguitars.com%2F&docid=z2UnAIPtpnTM_M&tbnid=7OjYFlBbi-LuRM%3A&vet=10ahUKEwjyxIKCkYbZAhWj0YMKHX46Ai4QMwg_KAAwAA..i&w=400&h=400&safe=active&bih=670&biw=1280&q=image%20logo%20taylore%20logo&ved=0ahUKEwjyxIKCkYbZAhWj0YMKHX46Ai4QMwg_KAAwAA&iact=mrc&uact=8")
a.save()
a.id
a.artist

b = Album()
b.artist = "Bruno Mars"
b.albumTitle = "Silver"
b.save()

Album.objects.filter(id=3)
Album.objects.filter(artist__startswith='Taylor')

a1 = Album.objects.get(pk=1)
s1 = Song()
s1.album = a1
s1.file_type = "mp3"
s1.song_title = "Live alone"
s1.save()

a1.song_set.all()
a1.song_set.create(song_title="westworld",file_type="mp3")

'''
from django.db import models

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=50)
    albumTitle = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    album_logo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.artist + ' - ' + self.albumTitle
    
    
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    file_type = models.CharField(max_length = 10)
    song_title = models.CharField(max_length = 20)

    
    def __str__(self):
        return self.song_title + ' - ' + self.file_type
    
