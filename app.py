from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def name():
    return "This is my practice flask application for HW2"

@app.route("/about")
def about():
    return "My name is Alejandro Alvarado Mora, I am 22 years old"


form_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Fortune Teller</title>
</head>
<body>
    <h1>Fortune Teller</h1>
    <form method="POST" action="/fortune">
        <label for="user">Your Name:</label>
        <input type="text" id="user" name="user" required>

        <label for="color">Choose a Color:</label>
        <select id="color" name="color" required>
            <option value="">--Select Color--</option>
            <option value="red">Red</option>
            <option value="yellow">Yellow</option>
            <option value="blue">Blue</option>
            <option value="green">Green</option>
        </select>

        <label for="number">Choose a Number:</label>
        <select id="number" name="number" required>
            <option value="">--Select Number--</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
        </select>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
'''

def getFortune(color, number):
    if color == 'red' and number == '1':
        return "With integrity and consistency -- your credits are piling up."
    elif color == 'red' and number == '2':
        return "Reach out your hand today to support others who need you."
    elif color == 'red' and number == '3':
        return "It is not the outside riches bit the inside ones that produce happiness."
    elif color == 'red' and number == '4':
        return "How dark is dark?, How wise is wise?"
    elif color == 'yellow' and number == '1':
        return "We can admire all we see, but we can only pick one."
    elif color == 'yellow' and number == '2':
        return "The man who has no imagination has no wings."
    elif color == 'yellow' and number == '3':
        return "To courageously shoulder the responsibility of one's mistake is character."
    elif color == 'yellow' and number == '4':
        return "We can't help everyone. But everyone can help someone"
    elif color == 'blue' and number == '1':
        return "You discover treasures where others see nothing unusual."
    elif color == 'blue' and number == '2':
        return "Make all you can, save all you can, give all you can."
    elif color == 'blue' and number == '3':
        return "Understanding the nature of change, changes the nature."
    elif color == 'blue' and number == '4':
        return "You will be unusually successful in business."
    elif color == 'green' and number == '1':
        return "Your spirit of adventure leads you down an exiting new path."
    elif color == 'green' and number == '2':
        return "Genius is one percent inspiration and ninety-nine percent perspiration."
    elif color == 'green' and number == '3':
        return "You are the master of every situation."
    elif color == 'green' and number == '4':
        return "Cookies go stake. Fortunes are forever."
    else:
        return "Your power is in your ability to decide."



@app.route("/fortune", methods=["GET", "POST"])
def fortuneTeller():
    if request.method == "POST":
        user = request.form.get("user")
        color = request.form.get("color")
        number = request.form.get("number")
        fortune = getFortune(color, number)
        return f"Your name is {user}, and your fortune is: {fortune}"
    return render_template_string(form_html)

