from asyncio import start_server
from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_table
from pywebio import start_server

async def bmi():
    height = await input("Input your height(cm)：", type=FLOAT, validate=FLOAT, placeholder="This should be numeric value")
    weight = await input("Input your weight(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_table([
                ['Hight', 'Weight', 'BMI'],
                [height, weight, BMI]
                ])
            put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
            break

start_server(bmi, auto_open_webbrowser=True)
