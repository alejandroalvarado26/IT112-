from flask import Flask, request, render_template_string, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artists.sqlite3'
db = SQLAlchemy(app)
api = Api(app)

class artists(db.Model):
    id = db.Column('artist_id', db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50))
    formationYear = db.Column(db.Integer)
    genre = db.Column(db.String(50))

    def __init__(self, name, formationYear, genre):
        self.name = name
        self.formationYear =  formationYear
        self.genre = genre

artist_args = reqparse.RequestParser()
artist_args.add_argument('name', type=str, required=True, help="Invalid name")
artist_args.add_argument('formationYear', type=int, required=True, help="Invalid year")
artist_args.add_argument('genre', type=str, required=True, help="Invalid genre")

artistsFields = {
    'id':fields.Integer,
    'name':fields.String,
    'formationYear':fields.Integer,
    'genre':fields.String,
}

class artistsResource(Resource):
    @marshal_with(artistsFields)
    def get(self):
        artistList = artists.query.all()
        return artistList

    @marshal_with(artistsFields)
    def post(self):
        try:
            args = artist_args.parse_args()
            newArtist = artists(name=args["name"], formationYear=args["formationYear"], genre=args["genre"])
            db.session.add(newArtist)
            db.session.commit()
            return newArtist, 200
        except Exception:
            db.session.rollback()
            abort(500)


api.add_resource(artistsResource, '/api/artists/')

"""
with app.app_context():
    db.create_all()
    
    metallica = artists(name="Metallica", formationYear=1981, genre="Thrash Metal")
    slayer = artists(name="Slayer", formationYear=1981, genre="Thrash Metal")
    sepultura = artists(name="Sepultura", formationYear=1984, genre="Thrash Metal")
    bathory = artists(name="Bathory", formationYear=1983, genre="Black Metal")

    db.session.add_all([metallica, slayer, sepultura, bathory])
    db.session.commit()
"""

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

@app.route("/artistlist")
def artistList():
    return render_template("artistlist.html")

@app.route("/metallica")
def metallicaDetail():
    artist = artists.query.filter_by(name="Metallica").first()
    return f"The band {artist.name}, ID number {artist.id}, was founded in {artist.formationYear} and plays {artist.genre}"

@app.route("/slayer")
def slayerDetail():
    artist = artists.query.filter_by(name="Slayer").first()
    return f"The band {artist.name}, ID number {artist.id}, was founded in {artist.formationYear} and plays {artist.genre}"

@app.route("/sepultura")
def sepulturaDetail():
    artist = artists.query.filter_by(name="Sepultura").first()
    return f"The band {artist.name}, ID number {artist.id}, was founded in {artist.formationYear} and plays {artist.genre}"

@app.route("/bathory")
def bathoryDetail():
    artist = artists.query.filter_by(name="Bathory").first()
    return f"The band {artist.name}, ID number {artist.id}, was founded in {artist.formationYear} and plays {artist.genre}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)