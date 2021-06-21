from django.shortcuts import render
from .forms import Order
from .models import Order as Orderdb


def honey(request):
    return render(request, "main.html")


def form_order(request):
    order = Order()
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        address = request.POST.get("address")
        social_web = request.POST.get("social_web")
        mail = request.POST.get("mail")
        number_phone = request.POST.get("number_phone")
        sort_honey = request.POST.get("sort_honey")
        count_honey = request.POST.get("count_honey")

        bd = Orderdb(name=name, surname=surname, address=address, mail=mail, number_phone=number_phone,
                   sort_honey=sort_honey, count_honey=count_honey, social_web=social_web)

        bd.save()

        message = "Форма успешно отправлена. С вами свяжется наш сотрудник."
        if sort_honey == "Гречишный":
            sh = 600
        elif sort_honey == "Липовый":
            sh = 900
        else:
            sh = 680
        price = int(count_honey) * sh
        return render(request, "redirect.html", {'message': message, 'price': price})
    else:
        return render(request, "order.html", {"form": order})


def contact(request):
    return render(request, "contact.html")


def sorts(request):
    return render(request, "sorts.html")


def about_us(request):
    return render(request, "about_us.html")