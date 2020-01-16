from flask import Flask, render_template, flash, request
from flask import Flask
import random


app = Flask(__name__)

@app.route("/4")
def task_4():
    x1 = random.randint(-10, 10)
    y1 = random.randint(-10, 10)
    x2 = random.randint(-10, 10)
    y2 = random.randint(-10, 10)
    x3 = random.randint(-10, 10)
    y3 = random.randint(-10, 10)
    x4 = random.randint(-10, 10)
    y4 = random.randint(-10, 10)
    times = random.randint(1, 10)
    x_res = x1 + x2*times + x3*times + x4*times
    y_res = y1 + y2*times + y3*times + y4*times
    alg = ('Чертёжнику был дан для исполнения следующий алгоритм: \n\tСместиться на ('+ str(x1)+','+str(y1) +')'
    +' \n\tПовтори ' +str(times) + ' раз \n\tСместиться на ('+ str(x2)+','+str(y2)+')'
    +' \n\tСместиться на (' + str(x3)+','+str(y3) +')'+' \n\tСместиться на ('+ str(x4)+','+str(y4) +')'+' \nКонец')
    answer = (x_res,y_res)
    return alg, answer
        return render_template('4.html', alg=alg, answer=answer)

if __name__ == "__main__":
        app.run()
