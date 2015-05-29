from glob import glob
from binascii import hexlify, unhexlify

societies = {
    "res": "Research Society",
    "spo": "Sports Society",
    "lit": "Literary Society",
    "tec": "Technical Society",
    "cul": "Cultural Society",
    "aca": "Academic Society",
    "gen": "SAC"
}

months = [
    "-", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]

def get_entries_raw():
    return glob("posts/*")

def get_entries(filter_soc="", filter_clb=""):
    """Collect entries from /posts.
    Entries in posts are named yyyymmdd.soc.clb.md"""
    entries_raw = get_entries_raw()
    entries = []

    # We need the latest entries to be displayed first.
    for entry_raw in reversed(sorted(entries_raw)):

        # Collect meta-data from filename of entry.
        date, society, club = get_entry_mdata(entry_raw)
        if filter_soc != "" and filter_soc != society:
            continue
        if filter_clb != "" and filter_clb != club:
            continue

        with open(entry_raw) as doc:
            entries.append([hexlify(entry_raw),
                            doc.readline(),
                            societies[society],
                            date])

    return entries


def get_date(entry_raw):
    date_raw = entry_raw[6:14]
    year, month, day = date_raw[:4], months[int(date_raw[4:6])], date_raw[6:8]
    return month + " " + day + ", " + year

def get_society(entry_raw):
    return entry_raw[15:18]

def get_club(entry_raw):
    return entry_raw[19:22]

def get_entry_mdata(entry_raw):
    return [get_date(entry_raw), get_society(entry_raw), get_club(entry_raw)]
