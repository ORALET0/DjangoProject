# DjangoProject
Django Project Meeting Planner

1. Terminale gelerek aşağıda ki PowerShell kodunu çalıştırarak django web framework projemize indiriyoruz.
    (venv) PS C:\Users\XXX\XXX\DjangoProject> python -m pip install django

2. Terminalden üzerinden aşağıda ki kodu çalıştırın. BU kod vasıtasıyla projemizin omurgasını oluşturan gerekli py dosyalarını projemize dahil edilecektir. Bu dosyalara core, kernel yani çekirdek dosyalar diyebiliriz.
    (venv) PS C:\Users\XXX\XXX\DjangoProject> django-admin startproject meeting_planner

3. Porjemizi ayağı kladırmak için core dosyalarımızın bulunduğu klasöre yürüyoruz.
    (venv) PS C:\Users\XXX\XXX\DjangoProject> cd meeting_planner

 4. Uygulamamızı ayağı kaldıralım
    (venv) PS C:\Users\XXX\XXX\DjangoProject\meeting_planner> python manage.py runserver


 5. projemizde sabit yapılarımızı yada bir başka değiş ile sabit sayfalarımızı yönetmek için bir application oluşturuyoruz.
    (venv) PS C:\Users\XXX\XXX\DjangoProject\meeting_planner> python manage.py startapp website

 6. meeting_planner => settings.py => InstalledApps listesine aşağıdaki kodu ekleyin.
    'INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'website' # sadece bu satır eklenilecek
]

 7. website içerisinde bulunan "admin.py, apps.py, models.py, test.py" dosyalarını ve "migrations" klasörünü sildik.


 8. website => views.py dosyasına aşağıda ki kodları ekleyin
    from django.http import HttpResponse

    def welcome(request):
	    return HttpResponse('Welcome to the Meeting Planer App')

9. meeting_planner => url.py dosyasına aşağıdaki kodları ekleyin
    from website.views import welcome

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('welcome.html', welcome) # bu satırı listeye ekle
    ]

10. yukarada farklı klasörde bulunan bir py dosyasını meeting_planner içerisinde kullanmaya çalıştık. website altında bulunan views.py dosyasının altında bulunan welcome() fonksiyonun tam yolunu uzun uzun yazmamak için ana meeting_planner klasörümüze sağ tıklayarak Mark Directory as dedikten sonra Source Root seçeneğini seçtik böylelikle farklı klasörlerde bulunan py dosyalarımıza erişmek için uzun uzun dosya yollarını yazmak durumunda kalmayacağız.


11. Migrations
Admin tarafında bulunan varlıkları (entities) veri tabanına göç (migrations) ettireceğiz. ORM mantığı gereği uygulama tarafında ki (app side entities) objeler ile veri tabanında ki tabloların bire bir aynı olması gerektiği bize söylenir. Bu yüzden admin tarafının sahip olduğu varlıkları veri tabanına göç ettiriyoruz. ORM mantığında göç işleminin farklı yapıları bulunmaktadır. Bunlar code first, database first. Code first bizim en sevdiğimiz ve kullandığız yapıdır. Uygulama tarafında projede ihtiyaç duyulan varlıkları class'lar aracılığı ile yaratarak veri tabanına göç ettiriyoruz. database first yaklaşımında ise veri tabında ki tabloları uygulama tarafına çıkararak onları class'lar olarak uygulamaya ekliyoruz.

12. migrations işlemi ile veri tabanına gönderilecek varlıkların listesini görmek için aşağıdaki terminal kodunu çalıştırın
    (venv) PS C:\Users\XXX\XXX\DjangoProject\meeting_planner> python manage.py showmigrations

13. yukarıda ki adımda listelediğimiz varlıkları aşağıda ki termial kodu ile veri tabanına göç (migration) ettiriyoz.
    (venv) PS C:\Users\XXX\XXX\DjangoProject\meeting_planner> python manage.py migrate


 14. Aşağıdaki kodu terminalde çalıştırarak veri tabanına erişebilir ve SQL sorguları yazabilirsiniz
    (venv) PS C:\Users\XXX\XXX\DjangoProject\meeting_planner> python manage.py dbshell

15. veri tabanında hali hazırda bulunan tabloları görmek için
    sqlite> .tables

16. veri tabanında bulunan django_migrations tablosunda ki kayıtları görüntüleme
    sqlite> select * from django_migrations

17. Projemizde ki varlıklarımızın CRUD operasyonlarını yönetmek için porjemize yeni bir app ekliyoruz.
    (venv) PS C:\Users\XXX\XXX\DjangoProject\meeting_planner> python manage.py startapp meetings


18. meeting_planner => settings.py dosyasınd aşağıdaki değişikliği yapın
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'meetings' # sadece bu satır eklenilecek
]

19. meetings => model.py dosyasına aşağıda ki kodları ekleyerek uygulama tarafında ki varlıkları (entities) yaratalım

class Room(models.Model):
	name = models.CharField(max_length=50)
	floor = models.CharField(max_length=50)
	room_number = models.IntegerField()

	def __str__(self):
		return f'{self.name}: room' \
		       f'{self.room_number} on floor' \
		       f'{self.floor}'


class Meeting(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateField()
	start_time = models.TimeField(default=time(9))
	duration = models.IntegerField(default=1)

	room = models.ForeignKey(Room, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.title} at' \
		       f'{self.start_time} on' \
		       f'{self.date}'


20. Terminal ekranında aşağıdaki shell kodunu çalıştırarak göç işemini yaptırın ve yukarıda yazdığımız class'lar yani oluşturduğumuz model veri tabanınında tablo olarak oluşturulsun.
    (venv) PS C:\Users\XXX\XXX\DjangoProject\meeting_planner> python manage.py makemigrations

    (venv) PS C:\Users\XXX\XXX\DjangoProject\meeting_planner> python manage.py migrate

21. Admin tarafına gidebilmemiz için authorization geçmemiz gerekmektedir yani login olmamız gerekmektedir. Bunun için bir superuser yaratamak gerekiyor.
    (venv) PS C:\Users\XXX\XXX\DjangoProject\meeting_planner> python manage.py createsuperuser

22. meetings => admin.py içerisine aşağıda ki kodları ekleyin. Burada ki mantık admin tarafında bu entity'leir kullanmaktır yani bu varlıklar üzerinde crud operasyonu yapabilmektir.
    admin.site.register(Meeting)
    admin.site.register(Room)


23. website => templates adında bir klasör açıyoruz.
24. website => templates => website adında bir klasör açıyoruz
25. website => templates => website => welcome.html dosyası açılır.

26. website => view.py dosyasında ki var olan welcome fonskiyonunu modifiye et.
def welcome(request):
	return render(request,
	              'website/welcome.html',
	              {
		              'message': 'Welcome to the Meeting Planer App',
		              'num_meeting': Meeting.objects.count()
				  })
27. website => template => website => welcome.html dosyasında tasarıma uygun olarak aşağıda ki kodları ekle
    <p>{{ message }}</p>
    <p>There are currently {{ num_meeting }} meetings in the database.</p>


28. meetings => views.py dosyasına aşağıda ki kodları ekleyin
    def detail(request, id):
	    meeting = get_object_or_404(Meeting, pk=id)

	    return render(request,
	                'meetings/detail.html',
	                {'meeting': meeting})

29. meeting_planner => urls.py altında bulunan url_patterns listesinde değişiklik yap
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('welcome.html', welcome),
        path('about', about),
        path('date', date),
        path('meetings/<int:id>', detail)  # sadece bu satır eklenecek
    ]

30. meetings => templates adında klasör oluştur.
31. meetings => templates => meetings adında klasör oluştur.
32. meetings => templates => meetings => detail.html adında dosya oluştur ve tasarıma uygun olarak aşağıda ki kodları ekle

    <h4>{{ meeting.title }}</h4>
    <p>
        This meeting has been scheduled on {{ meeting.date }}, at {{ meeting.start_time }} in <strong>{{ meeting.room }}</strong>
    </p>

 33. welcome sayfasında toplantıları listeliyoruz ve bir toplantıya tıklanıldığında onun detayına gidiyoruz.
 34. website => views.py => welcome() fonksiyonunda değişiklik yap
 def welcome(request):
	return render(request,
	              'website/welcome.html',
	              {
		              'message': 'Welcome to the Meeting Planer App',
		              'num_meeting': Meeting.objects.count(),
		              'meetings': Meeting.objects.all() # bu satırı ekledik. veri tabında ki bütün toplantıları bize liste olarak döndü
				  })

34. website => templates => website => welcome.html sayfasına aşağıda ki kodları ekle

    <h4>Meetings</h4>
    <ul>
        {% for meeting in meetings %}
            <li>
                <a href="{% url 'detail' meeting.id %}">{{ meeting.title }}</a>
            </li>
        {% endfor %}
    </ul>

 35. meeting_planer => urls => urlpatterns listesinde ki detail url deseninde değişiklik yap
 urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('about', about),
    path('date', date),
    path('meetings/<int:id>', detail, name='detail')  # sadece "name" parametresi ekle
]


36. meetings => views.py içerisine aşağıda ki kodları ekleyin

def room_list(request):
	return render(request,
	              'meetings/room_list.html',
	              {'rooms': Room.objects.all()})


37. meetings => templates => meetings => room_list.html dosyası açın ve tasarımsal olarak aşağıdaki kodları ekleyin

    <h5>Rooms</h5>
    <ul>
      {% for room in rooms  %}
        <li>{{ room }}</li>
      {% endfor %}
     </ul>

38. meeting_planner => urls => urlpatterns listesine aşağıdaki kodu ekleyin
    path('rooms', room_list, name='rooms')


39. meetings => urls.py dosyası açılır.
    from django.urls import path
    from meetings.views import detail, room_list

    urlpatterns = [
        path('meetings/<int:id>', detail, name='detail'),
        path('rooms', room_list, name='rooms')
    ]

40. meetings_planner => urls.py dosyasında aşağıdaki değişikliği yapın

    from django.urls import path, include # include eklenir
    from website.views import welcome, about, date

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', welcome, name='welcome'),
        path('about', about),
        path('date', date),
        path('meetings/<int:id>', detail, name='detail'), # bu satır silinir
	    path('rooms', room_list, name='rooms') # bu satır silinir
        path('', include('meetings.urls'))  # bu satır eklenir
    ]


    41. meetings => forms.py dosyası açılır.

        from django.forms import ModelForm, TextInput, DateInput, TimeInput
        from .models import Meeting
        from datetime import date
        from django.core.exceptions import ValidationError
        from string import punctuation


        class MeetingForm(ModelForm):
            class Meta:
                model = Meeting
                fields = '__all__'
                widgets = {
                    'title': TextInput(attrs={'type': 'text'}),
                    'date': DateInput(attrs={'type': 'date'}),
                    'start_time': TimeInput(attrs={'type': 'time'}),
                    'duration': TextInput(attrs={'type': 'number', 'min': '1', 'max': '4'})
                }

            def clean_date(self):
                """
                Burada geçmiş zamanda toplantı set edilmesini engeliyoruz.
                :return: date
                """
                d = self.cleaned_data.get('date')

                if d < date.today():
                    raise ValidationError('Meeting cannot set for the past time!')
                return d

            def clean_title(self):
                """
                Burada title içerisinde noktalama işareti olmasını engelliyoruz
                :return: string
                """
                title = self.cleaned_data.get('title')

                for character in title:
                    if character in punctuation:
                        raise ValidationError('Meeting cannot contains punctuation!')
                return title


42. meetings => views.py dosyasına aşağıdaki kodları ekleyin.

    def create(request):
        if request.method == 'POST':
            form = MeetingForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('welcome')
        else:
            form = MeetingForm()

        return render(request,
                      'meetings/create.html',
                      {'form': form})


43. meetings => templates => meetings => create.html sayfası oluşturulur.

    {% extends 'base.html' %}

    {% block title %}
        Create New Meeting
    {% endblock %}

    {% block content %}
        <div class="row mt-2">
            <div class="col-sm-2">
                <div class="card">
                    <div class="card-header">
                        <h5 class="card-title">Schedule New Meeting</h5>
                    </div>
                    <form method="POST">
                        {% csrf_token %}
                        <div class="card-body">
                            {{ form }}
                        </div>
                        <div class="card-footer">
                            <a href="{% url 'welcome' %}" class="btn btn-sm btn-outline-primary me-2 ms-2 float-end">Back Home</a>
                            <button type="submit" class="btn btn-sm btn-outline-success me-2 ms-2 float-end">Create</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    {% endblock %}


44. Create-Update-Delete form sayfalarımıza bootstrap yedirebilmek için aşağıdaki adımları uygulayın
    44.1. pip install django-bootstrap5
    44.2. website => templates => base.html içerisine aşağıdaki kodu ekleyin
        {% load django_bootstrap5 %}  # head bloğuna eklenir
    44.3. meeting_planner => settings.py
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'website',
            'meetings',
            'django_bootstrap5',  # eklenir
        ]
    44.4. ihtiyaç duyulan sayfalarda aşağıdaki kod eklenir
        {% load django_bootstrap5 %}

45. Update iş mantığı çözümlenir
    45.1. meetings => views.py => update() fonksiyonunu yaz
    45.2. meetings => templates => meetings => update.html yarat
    45.3. meetings => urls.py => update işlemi için path() fonksiyonu yaz


46. Delete iş mantığı çözümlenir
    45.1. meetings => views.py => delete() fonksiyonunu yaz
    45.2. meetings => templates => meetings => delete.html yarat
    45.3. meetings => urls.py => delete işlemi için path() fonksiyonu yaz


47. 'rooms' adında yeni app projeye eklenir.
    (venv) PS C:\Users\XXX\XXX\DjangoProject\meeting_planner> python manage.py startapp rooms

48. meeting_planner => settings.py => INSTALLED_APPS listesine rooms apini ekliyoruz.
49. rooms => urls.py oluşturuldu.
50. meeting_planner => urls.py => rooms.py path() fonksiyonu eklenir.
51. rooms => templates klasörü açılır.
52. rooms => templates => rooms klasörü açılır.
53. rooms => views.py => room_list() fonksiyonu yazılır.
54. rooms => urls.py => room_list path() fonksiyonu yazılır.
55. rooms => templates => rooms => room_list.html dosyası açılır.
56. rooms => views.py => detail() fonksiyonu yazılır.
57. rooms => templates => rooms => detail.html dosyası eklenir.
58. rooms => urls.py => detail path() fonksiyonu yazılır.
59. rooms => view.py => create() fonksiyonu yazılır.
60. rooms => forms.py açılır.
61. rooms => forms.py => RoomForm.py dosyası hazırlanır.
62. rooms => templates => rooms => create.html yaratılır.
63. rooms => urls.py => create url path() fonksiyonu yazlır.
64. rooms => view.py => update() fonksiyonu yazılır.
65. rooms => templates => rooms => update.html dosyası eklenir.
66. rooms => urls.py => update url path() fonksiyonu yazlır.
67. rooms => view.py => delete() fonksiyonu yazılır.
68. rooms => templates => rooms => delete.html dosyası eklenir.
69. rooms => urls.py => delete url path() fonksiyonu yazlır.
