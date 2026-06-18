from django.http import HttpResponse


def nowa_strona(request):
    return HttpResponse("To jest moja nowa strona")


def nowa_strona2(request):
    return HttpResponse("To jest moja nowa strona2")

# def home(request):
#     html = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <meta charset="utf-8">
#         <title>Strona główna</title>
#     </head>
#     <body>
#
#         <h1>Strona główna</h1>
#
#         <h2>Księga gości</h2>
#
#         <form method="POST">
#             <input type="text" name="imie" placeholder="Imię"><br><br>
#             <input type="text" name="wiadomosc" placeholder="Wiadomość"><br><br>
#             <button type="submit">Wyślij</button>
#         </form>
#
#     </body>
#     </html>
#     """
#     return HttpResponse(html)



# def home(request):
#     if request.method == "POST":
#         imie = request.POST.get("imie")
#         wiadomosc = request.POST.get("wiadomosc")
#         print(imie, wiadomosc)
#
#     return render(request, "home.html")


from django.shortcuts import render
from guestbook.models import Wpis

def home(request):

    if request.method == "POST":
        imie = request.POST.get("imie")
        wiadomosc = request.POST.get("wiadomosc")

        Wpis.objects.create(
            imie=imie,
            wiadomosc=wiadomosc
        )

    wpisy = Wpis.objects.order_by("-data")

    return render(
        request,
        "home.html",
        {"wpisy": wpisy}
    )