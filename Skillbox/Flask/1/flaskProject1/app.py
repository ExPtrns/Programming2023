import os
import random

from flask import Flask
import datetime

app = Flask(__name__)
cars_list = "Chevrolet, Renault, Ford, Lada"
cats_list = ("корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин", "к")


@app.route('/hello_world')
def hello_world():
    return 'Hello World!'


@app.route('/cars')
def cars():
    return cars_list


@app.route('/cats/<name>')
def cats(name):
    some_cat = random.choice(cats_list)
    some_cat = some_cat
    return some_cat + ". Name - " + name


@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now()
    return f"Точное время: {current_time}"


@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
    return f"Точное время через час будет {current_time_after_hour}"


@app.route('/file_exist/<path:file_path>')
def file_exist(file_path):
    file_existing = os.path.exists(file_path)

    if file_existing:
        result = 0
        input_file = open(file_path, 'r')
        data = input_file.readlines()[1:]
        for line in data:
            words = line.split()
            result += int(words[5])
        lengths = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
        pointer = 0
        count = result
        while result > 1023:
            result = result / 1024
            pointer += 1

        return f"{count}->{int(result)} {lengths[pointer]}"
    else:
        return "not found"


if __name__ == '__main__':
    app.run(debug=True)
