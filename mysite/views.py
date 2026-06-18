from django.shortcuts import render
from guestbook.models import Wpis, Wpis_vehicle
from django.http import HttpResponse



def nowa_strona(request):

    if request.method == "POST":
        vahicle_name = request.POST.get("vahicle_name")
        vahicle_model = request.POST.get("vahicle_model")
        vahicle_rok = request.POST.get("vahicle_rok")
        print(vahicle_name, vahicle_model,vahicle_rok)
        Wpis_vehicle.objects.create(
            vahicle_name=vahicle_name,
            vahicle_model= vahicle_model,
            vahicle_rok=vahicle_rok
        )

    wpisy = Wpis_vehicle.objects.order_by("-id")
        #
    # wpisy = Wpis_vehicle.objects.order_by("-id")  # Pobranie wszystkich wpisów z bazy danych, posortowanych malejąco po id

    return render(
        request,
        "main.html",
        {"wpisy": wpisy}
    )



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





def home(request):

    if request.method == "POST":
        imie = request.POST.get("imie")
        wiadomosc = request.POST.get("wiadomosc")
        print(imie, wiadomosc)
        Wpis.objects.create(
            imie=imie,
            wiadomosc=wiadomosc
        )
    #
    wpisy = Wpis.objects.order_by("-id")  # Pobranie wszystkich wpisów z bazy danych, posortowanych malejąco po id

    return render(
        request,
        "home.html",
        {"wpisy": wpisy}
    )