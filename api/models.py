from django.db import models

# Create your models here.
class Item(models.Model):
    RATINGS = (
        ('5 Stars', '5 Stars'),
        ('4 Stars', '4 Stars'),
        ('3 Stars', '3 Stars'),
        ('2 Stars', '2 Stars'),
        ('1 Stars', '1 Stars'),
    )

    title = models.CharField(max_length=120)
    stock_quantiy = models.IntegerField(default=1)
    rating = models.CharField(max_length=10, choices=RATINGS)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
