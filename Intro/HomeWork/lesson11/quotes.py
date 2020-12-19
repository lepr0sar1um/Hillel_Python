import csv
import requests

get_url = "http://api.forismatic.com/api/1.0/"
params = {"method": "getQuote", "lang": "ru", "format": "json"}
file = "quotes.csv"


def get_full_quotes_list(url: str):
    raw_list = []
    for _ in range(500):
        response = requests.get(url, params)
        raw_list.append(response.json())
    return raw_list


def sort_key(tmp_list):
    return tmp_list['quoteAuthor']


def get_cleared_quotes(quotes):
    unique_quotes_with_author = list({v['quoteText']: v for v in quotes if v['quoteAuthor'] != ''}.values())
    list_without_extra_keys = [{k: v for k, v in d.items() if k != 'senderName' and k != 'senderLink'} for d in
                               unique_quotes_with_author]
    sorted_list = sorted(list_without_extra_keys, key=sort_key)
    return sorted_list


def write_quotes_to_csv(url):
    full_quotes = get_full_quotes_list(url)
    sorted_quotes = get_cleared_quotes(full_quotes)
    headers = sorted_quotes.pop(0)
    with open(file, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, dialect='excel', fieldnames=headers)
        writer.writeheader()
        writer.writerows(sorted_quotes)
    print(f"File {file} has successfully been written")


write_quotes_to_csv(get_url)
