from datetime import datetime

presidents = {
    "Lyndon B Johnson": (1908, 8,  27),
    "Richard Nixon": (1924, 10, 1),
    "Gerald Ford": (1913, 7, 14),
    "Jimmy Carter": (1924, 10, 1),
    "Ronald Reagan": (1911, 2, 6),
    "George H W Bush": (1924, 6, 12),
    "Bill CLinton": (1946, 8, 19),
    "Barack Obama": (1961, 8, 4),
    "Donald Trump": (1946, 6, 14)
}

for president in presidents:
    dt = datetime(*presidents[president])
    formatted_date = dt.strftime("%A %D %B %Y")
    if dt.weekday() == 0:
        print (f"{president} {formatted_date}: this president has a birthday on a monday.")
    else:
        print (f"{president} {formatted_date}")



