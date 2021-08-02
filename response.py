# not functional, will use later. basically pseudocode right now

class ChatthewResponse():
    def __init__(self):
        pass

def parse_request(message):
    pass

def is_chattew_request(message):
    '(optional)greeting' chatthew (request)
    chatthew_rgx = '^(.*)*(chatthew)(.*)$' #todo: something more clever without going into NLP
    if re.match('', message.content, re.IGNORECASE):
        return True
    return False

def process_request(message):
    response = ChatthewResponse()
    request = parse_message(message)
