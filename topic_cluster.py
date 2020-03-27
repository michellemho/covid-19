import nltk
import os
import json

comm_file_path = '../data/comm_use_subset/comm_use_subset'
articles = [] 

def getText():
    text_list = []
    for root,dirs,files in os.walk(comm_file_path):
        for i, file in enumerate(files):
            with open(root+'/'+file) as json_data:
                tmp = json.load(json_data)
                metadata = tmp['metadata']
                title = metadata['title']
                body_text = tmp['body_text']
                full_text = ''
                for paragraph in body_text:
                    full_text = full_text + paragraph['text'] + ' '
                text_list.append(full_text)
    return text_list