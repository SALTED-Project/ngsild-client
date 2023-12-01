import json
def handle_result(
        status_code, 
        msg = None 
        )->dict:
    if msg == None or msg == " " or msg == "":
         return {"status_code" : status_code}   
    return {"status_code" : status_code, "body" : json.loads(msg)}