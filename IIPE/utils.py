import os


def clean_file_names(lst):
    """returns a list of tuples<reference, date>"""
    cleaned = [
        name.replace("Reports_Plain text_", "").replace(".txt", "")
        for name in os.listdir()
        if name.endswith(".txt")
    ]
    splitted = [name.split("_") for name in cleaned]
    references = [lst[0] for lst in splitted]
    dates = ["-".join(name[1:][::-1]) for name in splitted]
    return [(r, d) for r, d in zip(references, dates)]


def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
