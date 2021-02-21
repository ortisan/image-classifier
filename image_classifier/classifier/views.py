from django.shortcuts import render

import json


def __load_json__():
    classifier_data = None
    # read the json with data
    with open(f'./classifier/static/classify_data/data.json', 'r') as f:
        classifier_data = json.load(f)
    return classifier_data


def __write_json__(data):
    with open(f'./classifier/static/classify_data/data.json', 'w') as f:
        json.dump(data, f)


def index(request):
    classifier_data = __load_json__()
    # data = [item for classifier_data.data.items() if not len(data.label)]
    # context = {'title': 'Candlesticks', 'data': data}
    return render(request, 'index.html', classifier_data)


def classified(request):

    classifier_data = __load_json__()
    data = classifier_data['data']
    data_by_id = {}
    for image_data in data:
        data_by_id[image_data["id"]] = image_data

    for key, value in request.POST.items():
        if key.startswith("label_"):
            image_id = key.replace("label_", "")
            data_by_id[image_id]['label'] = value

    updated_data = [value for key, value in data_by_id.items()]
    classifier_data["data"] = updated_data    

    __write_json__(classifier_data)

    return index(request)
