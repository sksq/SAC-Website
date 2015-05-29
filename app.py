from flask import Flask, render_template, redirect, request

from binascii import hexlify, unhexlify
from markdown2 import markdown

from helpers import get_entries_raw, get_entries, get_entry_mdata, societies

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    entries = get_entries()
    return render_template("home.html", entries=entries)

@app.route("/lit")
def literary():
    entries = get_entries(filter_soc="lit")
    return render_template("literary.html", entries=entries)

@app.route("/sports")
def sports():
    entries = get_entries(filter_soc="spo")
    return render_template("sports.html", entries=entries)

@app.route("/tech")
def tech():
    entries = get_entries(filter_soc="tec")
    return render_template("tech.html", entries=entries)

@app.route("/cult")
def cultural():
    entries = get_entries(filter_soc="cul")
    return render_template("cult.html", entries=entries)

@app.route("/acad")
def academics():
    entries = get_entries(filter_soc="aca")
    return render_template("acad.html", entries=entries)

@app.route("/lit/info")
def literary_info():
    return render_template("literary_info.html")

@app.route("/acad/info")
def acad_info():
    return render_template("acad_info.html")

@app.route("/tech/info")
def tech_info():
    return render_template("tech_info.html")

@app.route("/sports/info")
def sports_info():
    return render_template("sports_info.html")

@app.route("/cult/info")
def cult_info():
    return render_template("cult_info.html")


@app.route("/literary/edls")
def literary_edls():
    entries = get_entries(filter_clb="edl")
    return render_template("literary.html", entries=entries)

@app.route("/literary/edls/info")
def literary_edls_info():
    return render_template("literary_edls_info.html")

@app.route("/entry")
def entry():
    entry_hex = request.args.get("id")
    entry_raw = unhexlify(entry_hex)

    entries_raw = get_entries_raw()
    entries = get_entries()
    if entry_raw in entries_raw:
        date, society, club = get_entry_mdata(entry_raw)
        with open(entry_raw) as doc:
            entry = [markdown(doc.read()), societies[society], date]

        print(entry)

        return render_template("entry.html",
                               entry=entry,
                               recent_entries=entries[:4])

    else:
        return "Problem with retrieving entry."

if __name__ == '__main__':
    app.run()
