from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/test", methods=['GET', "POST"])
def test_page():
    name = request.values.get('name')
    return f"Вы ввели имя {name}"


app.run()

#Запустите этот код, отправьте с помощью Postman:

#– GET запрос с URL http://127.0.0.1:5000/test?name="Алиса"

#– POST запрос с URL http://127.0.0.1:5000 и данными в теле запроса name = Алиса