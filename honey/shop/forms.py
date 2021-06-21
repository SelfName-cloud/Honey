from django import forms


class Order(forms.Form):
    name = forms.CharField(label='Имя', max_length=30, initial="Ваше имя")
    surname = forms.CharField(label='Фамилия', max_length=30, initial="Ваша фамилия")
    address = forms.CharField(label='Адрес', max_length=100, initial="Адрес проживания")
    social_web = forms.URLField(label='Станица Вконтакте', max_length=100, initial="Ваша странца Вконтакте")
    mail = forms.EmailField(label='Майл', max_length=40, initial="Ваш Email")
    number_phone = forms.CharField(label="Номер телефона", max_length=12, initial="Ваш номер телефона")
    sort_honey = forms.ChoiceField(label='Сорт меда', choices=[('Гречишный', "Гречишный мед"), ('Липовый', "Липовый мед"), ('Цветочный', "Цветочный мед")])
    count_honey = forms.IntegerField(label="Количество(в кг)", initial=0)




