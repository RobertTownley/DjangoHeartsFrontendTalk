from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    category = models.CharField(
        max_length=63,
        choices=(
            ('Appetizer', 'Appetizer'),
            ('Soup or Salad', 'Soup or Salad'),
            ('Main Course', 'Main Course'),
            ('Dessert', 'Dessert'),
        ),
        db_index=True,
    )
    image_url = models.CharField(max_length=511, blank=True, null=True)
    description = models.TextField()
    price = models.FloatField()
    is_special = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Dishes'
