from django.db import models
import json



# Create your models here.

MESSAGE_FILE = 'messages.json'

def get_messages():
    fhandler = open(MESSAGE_FILE, 'rt')
    cxt = fhandler.read()
    fhandler.close()
    return json.loads(cxt)


def save_messages(publish_date, username, title, content):
    messages = get_messages()
    messages.append({'publish_date':publish_date, 'username':username, 'title':title, 'content':content})
    fhandler = open(MESSAGE_FILE, 'wt')
    fhandler.write(json.dumps(messages))
    fhandler.close()