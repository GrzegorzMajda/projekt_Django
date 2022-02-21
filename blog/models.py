from django.db import models
from django.utils import timezone

# zbudowanie odnośnika do Model w klasie Post
# wszystkie zmienne - pola będą odnośnić do wszystkich modeli wbudowanych w Django
class Post(models.Model):
    # pobranie użytkownika
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # wprowadzenie tytułu max 200 znaków
    title = models.CharField(max_length=200)
    # wprowadzanie tekstu, artykułu
    text = models.TextField()
    # pobranie aktualnego czasu, daty
    created_date = models.DateTimeField(default=timezone.now)
    # możliwość uzupełnienia w późniejszym czasie
    publish_date = models.DateTimeField(blank=True, null=True)
    
    # definicja, która będzie zajmować się publikacją artykułu
    # ale zrobi to jeżeli artykuł będzie miał przypisany czas i godzinę
    def publish(self):
        self.publish_date = timezone.now()
        # zapisanie artykułu
        self.save()
        
    # funkcja wbudowana w python
    # funkcja zwraca tytuł a następenie przekazuje ją do klasy, która wyśle do bazy
    def __str__(self):
        return self.title
    
    
    
    
    
    
    
