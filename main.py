from flask import Flask, render_template
import requests
from deep_translator import GoogleTranslator

app = Flask(__name__)

# Функция для запроса случайной цитаты с API
def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        return response.json()
    else:
        return {"content": "Не удалось получить цитату", "author": "Неизвестный"}

# Функция для перевода текста на русский
def translate_to_russian(text):
    try:
        translated_text = GoogleTranslator(source='auto', target='ru').translate(text)
        return translated_text
    except Exception as e:
        return "Ошибка перевода"

# Маршрут для главной страницы
@app.route('/')
def index():
    quote = get_random_quote()
    translated_content = translate_to_russian(quote['content'])
    return render_template('index.html', content=translated_content, author=quote['author'])

if __name__ == '__main__':
    app.run(debug=True)
