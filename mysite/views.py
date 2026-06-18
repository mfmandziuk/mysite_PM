from django.http import HttpResponse

def nowa_strona(request):
    return HttpResponse("To jest moja nowa strona")


def nowa_strona2(request):
    return HttpResponse("To jest moja nowa strona2")

def home(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Strona główna</title>
    </head>
    <body>

        <h1>Strona główna</h1>

        <h2>Księga gości</h2>

        <form method="POST">
            <input type="text" name="imie" placeholder="Imię"><br><br>
            <input type="text" name="wiadomosc" placeholder="Wiadomość"><br><br>
            <button type="submit">Wyślij</button>
        </form>

    </body>
    </html>
    """
    return HttpResponse(html)