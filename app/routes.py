from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return (render_template("index.html"))

@app.route("/<country>/season/<season>")
def seasonal(country, season):
    data = {

        "mexico": {
            "summer": {
                "title": "¡Verano para disfrutar!",
                "message": "Comparte momentos especiales con ofertas vibrantes y experiencias inolvidables.",
                "theme": "mexico",
                "button": "Descubrir ofertas",
                "image": "mexico_summer.jpg"
            },

            "winter": {
                "title": "Invierno en familia",
                "message": "Celebra la temporada con calidez, alegría y promociones especiales.",
                "theme": "mexico",
                "button": "Ver promociones",
                "image": "mexico_winter.jpg"
            }
        },

        "germany": {
            "summer": {
                "title": "Sommerangebote",
                "message": "Praktische Angebote für die Saison. Qualität und Klarheit an erster Stelle.",
                "theme": "germany",
                "button": "Angebote ansehen",
                "image": "germany_summer.jpg"
            },

            "winter": {
                "title": "Winteraktionen",
                "message": "Zuverlässige Produkte und strukturierte Angebote für die kalte Jahreszeit.",
                "theme": "germany",
                "button": "Mehr erfahren",
                "image": "germany_winter.jpg"
            }
        }
    }

    page = data[country][season]

    return render_template(
        "seasonal.html",
        country=country,
        season=season,
        title=page["title"],
        message=page["message"],
        theme=page["theme"],
        button=page["button"],
        image=page["image"]
    )


from app import app
from flask import render_template, session, redirect, request