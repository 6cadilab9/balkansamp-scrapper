import json

filename = "data.json"

def get_message_count():

    ## open json file as read only
    with open('data.json') as f:
        data = json.load(f)

        ## get message count from data file
        return int(data["messages"]["count"])


def set_message_count(count):

    ## open json file with write opt
    with open('data.json', "r+") as jsonFile:
        data = json.load(jsonFile)

        ## store count with provided one
        data["messages"]["count"] = int(count)

        ## write to the file
        jsonFile.seek(0)
        json.dump(data, jsonFile, indent=4)
        jsonFile.truncate()