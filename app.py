from flask import Flask, render_template, request, url_for
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import random
from datetime import datetime, timedelta
import os


def generate_dates(n):
    start_date = datetime.strptime("1980-01-01", '%Y-%m-%d')
    end_date = datetime.strptime("2000-01-01", '%Y-%m-%d')

    random_dates = []
    for _ in range(n):
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        random_date = start_date + timedelta(days=random_days)
        just_day_month = datetime.strftime(random_date, "%m-%d")
        random_dates.append(just_day_month)
    
    return random_dates


def calc_match_chance(n):
    # number of possible combinations
    combinations = n*(n-1)/2
    # chance for match
    match_chance = 1-(364/365)**combinations
    return match_chance


def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates


def create_line_plot(n):
    plt.clf()
    num_of_people = list(range(1,366))
    probability = [calc_match_chance(x)*100 for x in num_of_people]

    probability_for_n = calc_match_chance(n)*100
    plt.plot(num_of_people, probability, color='black')
    plt.scatter(n, calc_match_chance(n)*100, color='red')
    plt.xlabel('Number of people')
    plt.ylabel('Probability')

    y_offset = 10 if n >= 9 else -10
    plt.annotate(f'{round(probability_for_n, 2)}% chance for matching birthdays',  
        xy=(n, probability_for_n), 
        xytext=(n+10 if n <= 75 else 130, probability_for_n-y_offset),  
        arrowprops=dict(facecolor='black', arrowstyle='->')) 

    plot_name = 'line_chart.png'
    plot_path = os.path.join(app.config['UPLOAD_FOLDER'], plot_name)
    plt.savefig(plot_path)
    plot_url = url_for('static', filename=f'images/{plot_name}')

    return plot_url


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'

@app.route('/', methods=['GET', 'POST'])
def index():
    number = ''
    if request.method == 'POST':
        num_of_people_input = int(request.form['num_of_people_input']) 
        number = num_of_people_input
        dates = generate_dates(num_of_people_input)
        match_chance = calc_match_chance(num_of_people_input)
        match_chance = f'{round(match_chance*100, 2)}%'
        duplicates = find_duplicates(dates)

        plot = create_line_plot(num_of_people_input)
        

        return render_template(
            "index.html",
            match_chance=match_chance,
            result=dates,
            duplicates=duplicates,
            plot_url=plot,
            number=number
            )

    return render_template("index.html")


if __name__ == '__main__':
    # app.run(debug=True, port=8001)
    app.run(host='0.0.0.0', port=5001)