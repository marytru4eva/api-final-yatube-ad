# from django.db import models


# Категории
# class Category(models.Model):
    # is_published = models.BooleanField(
    #  default=True,
    # verbose_name='Опубликовано'
    #)
    #title = models.CharField(
      #  max_length=256,
     #   verbose_name='Название'
    #)
    #slug = models.SlugField(
       # max_length=64,
      #  unique=True,
     #   verbose_name='Слаг'
    #)
   # output_order = models.PositiveSmallIntegerField(
  #      default=100,
 #       verbose_name='Порядок отображения'
#    )

  #  class Meta:
 #       verbose_name = 'категорию'
#        verbose_name_plural = 'Категории'

 #   def __str__(self):
#        return self.title


# Топпинги
#class Topping(models.Model):
    #is_published = models.BooleanField(
     #   default=True,
    #    verbose_name='Опубликовано'
    #)
    #title = models.CharField(
      #  max_length=256,
        #verbose_name='Название'
    #)
    #slug = models.SlugField(
   #     max_length=64,
  #      unique=True,
 #       verbose_name='Слаг'
#    )

  #  class Meta:
 #       verbose_name = 'топпинг'
#        verbose_name_plural = 'Топпинги'

 #   def __str__(self):
#        return self.title


# Обёртки
#class Wrapper(models.Model):
    #is_published = models.BooleanField(
     #   default=True,
    #    verbose_name='Опубликовано'
   # )
  #  title = models.CharField(
 #       max_length=256,
#        verbose_name='Название'
#    )

  #  class Meta:
 #       verbose_name = 'обёртку'
#        verbose_name_plural = 'Обёртки'

 #   def __str__(self):
#        return self.title


# Сорта мороженого
#class IceCream(models.Model):
    #is_published = models.BooleanField(
      #  default=True,
     #   verbose_name='Опубликовано'
    #)
    #is_on_main = models.BooleanField(
      #  default=False,
     #   verbose_name='На главную'
    #)
    #title = models.CharField(
     #   max_length=256,
     #   verbose_name='Название'
    #)
    #description = models.TextField(
     #   verbose_name='Описание'
    #)
    #price = models.DecimalField(
   #     max_digits=10,
  #      decimal_places=2,
 #       verbose_name='Цена'
#    )

    #category = models.ForeignKey(
    #    Category,
   #     on_delete=models.CASCADE,
  #      verbose_name='Категория',
 #       related_name='ice_creams'
#    )

   # toppings = models.ManyToManyField(
  #      Topping,
 #       verbose_name='Топпинги'
#    )

    #wrapper = models.OneToOneField(
      #  Wrapper,
     #   on_delete=models.SET_NULL,
    #    null=True,
   #     blank=True,
  #      verbose_name='Обёртка',
 #       related_name='ice_cream'
#    )


  #  class Meta:
 #       verbose_name = 'мороженое'
#        verbose_name_plural = 'Мороженое'


   # def __str__(self):
       # return self.title
