from flask import Flask, render_template, request, session

import random
from datetime import datetime, timedelta


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


app = Flask(__name__)
app.secret_key = "your_secret_key_here"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_of_people_input = int(request.form['num_of_people_input']) 
        dates = generate_dates(num_of_people_input)
        match_chance = calc_match_chance(num_of_people_input)
        match_chance = f'{round(match_chance*100, 2)}%'
        duplicates = find_duplicates(dates)
        return render_template("index.html", match_chance=match_chance, result=dates, duplicates=duplicates)

    return render_template("index.html")



    







if __name__ == '__main__':
    app.run(debug=True, port=8001)