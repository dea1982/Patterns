from wavy import render


def main_view(request):
    secret = request.get('secret_key', None)
    # Используем шаблонизатор
    return '200 OK', render('index.html', secret=secret)


def about_view(request):
    # Просто возвращаем текст
    return '200 OK', "About"

def products_view(request):
    secret = request.get('secret_key', None)
    # Так же используем шаблонизатор
    return '200 OK', render('products.html', secret=secret)
