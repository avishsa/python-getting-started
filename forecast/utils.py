import datetime
def date_formatter(date_csv):
    #2021-04-02T13:00:00
    print(date_csv)
    return datetime.datetime.strptime(date_csv, "%Y-%m-%dT%H:%M:%S")