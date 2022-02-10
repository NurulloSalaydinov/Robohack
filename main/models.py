from django.db import models
from ckeditor.fields import RichTextField

# contest model
class Contest(models.Model):
    banner_image = models.ImageField('Banner Uchun Rasm', upload_to='contes/images/banner/')
    card_image = models.ImageField('Card Uchun Rasm', upload_to='contes/images/card/')
    title = models.CharField('Sarlavha', max_length=255)
    language = models.CharField('Qaysi Tilda', max_length=100)
    address = models.CharField('Manzil', max_length=255)
    date = models.CharField('Sana', max_length=255, default='2022.02.25')
    time = models.CharField('Vaqt', max_length=255)
    description = RichTextField()
    slug = models.SlugField('*', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Musobaqalar'
        verbose_name_plural = 'Musobaqa'

# end contest
# usefull icon model
class UsefullIconContest(models.Model):
    which_contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=255)
    icon = models.CharField('Icon', max_length=255)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Musobaqa icons'
        verbose_name_plural = 'Musobaqa icon'

# end usefull icon model
# who_is_for model
class WhoIsForContest(models.Model):
    which_contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    img = models.ImageField('Rasm', upload_to='hackathon_images/')
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Musobaqa kimlar uchun'
        verbose_name_plural = 'Musobaqa kim uchun'

# end who_is_for model
# what_took model
class WhatTookContest(models.Model):
    which_contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    img = models.ImageField('Rasm', upload_to='hackhathon_took_images/')
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Musobaqa nima olasiz'
        verbose_name_plural = 'Musobaqa nimalar olasiz'

# end what_took model
# event model
class Event(models.Model):
    banner_image = models.ImageField('Banner Uchun Rasm', upload_to='contes/images/banner/')
    card_image = models.ImageField('Card Uchun Rasm', upload_to='contes/images/card/')
    title = models.CharField('Sarlavha', max_length=255)
    address = models.CharField('Manzil', max_length=255)
    date = models.CharField('Sana', max_length=255, default='2022.02.25')
    time = models.CharField('Vaqt', max_length=255)
    description = RichTextField()
    slug = models.SlugField('*', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tadbirlar'
        verbose_name_plural = 'Tadbir'

# end event model
# usefull icon model
class UsefullIconEvent(models.Model):
    which_contest = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=255)
    icon = models.CharField('Icon', max_length=255)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Tadbir icons'
        verbose_name_plural = 'Tadbir icons'

# end usefull icon model
# who_is_for model
class WhoIsForEvent(models.Model):
    which_contest = models.ForeignKey(Event, on_delete=models.CASCADE)
    img = models.ImageField('Rasm', upload_to='event_images/')
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Tadbir kimlar uchun'
        verbose_name_plural = 'Tadbir kim uchun'

# end who_is_for model
# what_took model
class WhatTookEvent(models.Model):
    which_contest = models.ForeignKey(Event, on_delete=models.CASCADE)
    img = models.ImageField('Rasm', upload_to='event_took_images/')
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Tadbirdan nima olasiz'
        verbose_name_plural = 'Tadbirdan nimalar olasiz'

# end what_took model
# contact model
class Contact(models.Model):
    name = models.CharField('Ism', max_length=255)
    phone = models.CharField('888 888 8888', max_length=255)
    message = models.TextField('Xabar matni')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contact'

# end contact model
# eventregister model
class EventRegister(models.Model):
    which_event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField('Ism Familiya', max_length=255)
    age = models.PositiveIntegerField('Yosh')
    experience = models.CharField('Tajribangiz necha oy/yil ?', max_length=255)
    phone = models.CharField('888 888 888', max_length=255)
    about = models.TextField("O'zingiz haqingizda qisqacha ...")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Tadbir Registeratsiyalar'
        verbose_name_plural = 'Tadbir Registeratsiya'

# end register model
# contestregister model

class ContestRegister(models.Model):
    which_contest = models.ForeignKey(Contest, on_delete=models.CASCADE, null=True)
    full_name = models.CharField('Ism Familiya', max_length=255)
    age = models.PositiveIntegerField('Yosh')
    experience = models.CharField('Tajribangiz necha oy/yil ?', max_length=255)
    phone = models.CharField('888 888 888', max_length=255)
    about = models.TextField("O'zingiz haqingizda qisqacha ...")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Musobaqa Registeratsiyalar'
        verbose_name_plural = 'Musobaqa Registeratsiya'
# eventquestion model
class EventQuestion(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    full_name = models.CharField('Ism Familiya', max_length=255)
    age = models.PositiveIntegerField('Yosh')
    phone = models.CharField('888 888 888', max_length=255)
    about = models.TextField("O'zingiz haqingizda qisqacha ...")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Tadbir Savollari'
        verbose_name_plural = 'Tadbir Savoli'

# end eventquestion model
# contestquestion model
class ContestQuestion(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField('Ism Familiya', max_length=255)
    age = models.PositiveIntegerField('Yosh')
    phone = models.CharField('888 888 888', max_length=255)
    about = models.TextField("O'zingiz haqingizda qisqacha ...")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Musobaqa Savollari'
        verbose_name_plural = 'Musobaqa Savoli'
 
# end contestquestion
# timeline model
class TimeLine(models.Model):
    which_contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    time = models.CharField('Vaqt', max_length=255)
    why_text = models.CharField('Nima boladi', max_length=255)
    left = models.BooleanField('Chap tomonga qoshish')

    def __str__(self):
        return f'{self.time} {self.which_contest}'

    class Meta:
        verbose_name = 'Musobaqa vaqt bolimlari'
        verbose_name_plural = 'Musobaqa vaqt bolimi'

# end timeline model
# time line event model
class TimeLineEvent(models.Model):
    which_contest = models.ForeignKey(Event, on_delete=models.CASCADE)
    time = models.CharField('Vaqt', max_length=255)
    why_text = models.CharField('Nima boladi', max_length=255)
    left = models.BooleanField('Chap tomonga qoshish')

    def __str__(self):
        return f'{self.time} {self.which_contest}'

    class Meta:
        verbose_name = 'Tadbir vaqt bolimlari'
        verbose_name_plural = 'Tadbir vaqt bolimi'

# end event timeline model
# images model
class Images(models.Model):
    title = models.CharField(max_length=355)
    img = models.ImageField('Rasm', upload_to='history_images/')

    def __str__(self):
        return f'{self.title} : {self.id}'

    class Meta:
        verbose_name = 'Rasmlar'
        verbose_name_plural = 'Rasm'

# end images model
# history image model
class HistoryImage(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    images = models.ManyToManyField(Images, verbose_name='Rasmlar')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Oldingi Musobaqadan eslatmalar'
        verbose_name_plural = 'Oldingi Musobaqadan eslatma'

# end history image model
