import json

filename = "data.json"

## get the message count from
## json file
def get_message_count():

    ## open json file as read only
    with open('data.json') as f:
        data = json.load(f)

        ## get message count from data file
        return int(data["messages"]["count"])

## write message count to the
## json file
def set_message_count(count):

    ## open json file with write opt
    with open('data.json', "r+") as f:
        data = json.load(f)

        ## store count with provided one
        data["messages"]["count"] = int(count)

        ## write to the file
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

## compare current messages with the provided
## param
def compare_messages(param):
    current_count = get_message_count()

    if current_count != param:
        set_message_count(param)
        print('You have an unread message!')

## get the mention count from
## json file
def get_mention_count():

    ## open json file as read only
    with open('data.json') as f:
        data = json.load(f)

        ## get message count from data file
        return int(data["mentions"]["count"])

## write mention count to the
## json file
def set_mention_count(count):

    ## open json file with write opt
    with open('data.json', "r+") as f:
        data = json.load(f)

        ## store count with provided one
        data["mentions"]["count"] = int(count)

        ## write to the file
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

## compare current mentions with the provided
## param
def compare_mentions(param):
    current_count = get_mention_count()

    if current_count != param:
        set_mention_count(param)
        print('You have been mentioned!')