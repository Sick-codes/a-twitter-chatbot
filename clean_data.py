import json
import re
import wget


def write_json(data, file):
    json.dump(data, file)
    return 'success'


def write_data(data, file):
    f = open(file, 'a', encoding='cp437', errors='ignore')
    f.write(data)


def clean_text(rgx_list, text):
    for i in rgx_list:
        sick_text = re.sub(fr'{i}\S+', '', text)
    return sick_text


def clean(rgx_list, infile, outfile):
    file = open(infile, 'r', encoding='cp437', errors='ignore')
    out = open(outfile, 'w', encoding='cp437', errors='ignore')
    for rgx_match in rgx_list:
        new_text = re.sub(rgx_match + r'?\S+', '', file.read())
        out.write(new_text + '\n')


def remove_single_chars(infile, outfile='clean.txt'):
    file = open(infile, 'r', encoding='cp437', errors='ignore')
    out = open(outfile, 'w', encoding='cp437', errors='ignore')
    newDoc = [x for x in file if len(x) > 3]
    for x in newDoc:
        out.write(x + '\n')


def remove_tags(data):
    return re.sub(r'@\S+', '', data)
    
    # lmao oops


def remove_special_chars(infile, outfile):
    file = open(infile, 'r', encoding='cp437', errors='ignore')
    out = open(outfile, 'w', encoding='cp437', errors='ignore')
    removeSpecialChars = file.read().translate({ord(c): "" for c in
                                        r'!@#$%^&*()[]{};:,./<>?\|`~-=_+12345678910""'})
    out.write(removeSpecialChars + '\n')


def filter_by_sub(sub, infile):
    data = open(infile, 'r', errors='ignore')
    outfile = open(f'{sub.upper()}.txt', mode='w', encoding='UTF-8',
                    errors='strict', buffering=1)
    for i in data:
        i = json.loads(i)
        if sub == i['subreddit']:
            sub_text = i['body']
            print(sub_text)
            outfile.write(sub_text + '\n')


# return sub_text


def get_data_from_url(url):
    text = wget.download(url)
    print(text)
