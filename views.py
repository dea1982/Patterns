from wavy import render
import os.path


def main_view(request):
    secret = request.get('secret_key', None)
    # Используем шаблонизатор
    return '200 OK', render('index.html', secret=secret)


def about_view(request):
    # Просто возвращаем текст
    return '200 OK', "About"


def contact_view(request):
    # Проверка метода запроса
    if request['method'] == 'POST':
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']
        file = "log.txt"
        #f = "hello world"
        if os.path.isfile(file):
            with open("log.txt", "a") as file:
                file.write(request + '\n')
            print(request)
            file.close()
        else:
            with open("log.txt", "w") as file:
                file.write(request + '\n')
            print(request)
            file.close()
#        print(
#            f'Нам пришло сообщение от {email} с темой {title} и текстом {text}')
#        return '200 OK', render('contact.html')
#    else:
#        return '200 OK', render('contact.html')
