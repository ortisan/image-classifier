from django.shortcuts import render

import json
from random import randint


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
    labels = classifier_data['labels']
    idx_label = randint(0, len(labels) - 1)
    label = labels[idx_label]
    classifier_data['label'] = label
    return render(request, 'index.html', classifier_data)


def classified(request):
    classifier_data = __load_json__()
    data = classifier_data['data']
    
    images_id = request.POST["images_id"].split(";")
    label = request.POST["label"]
    print("ABCLKJ", images_id)

    data_by_id = {}
    for image_data in data:
        data_by_id[image_data["id"]] = image_data

    for image_id in images_id:
        if len(image_id) > 0:
            data_by_id[image_id]['label'] = label

    updated_data = [value for key, value in data_by_id.items()]
    classifier_data["data"] = updated_data
    __write_json__(classifier_data)

    return index(request)
