from __future__ import annotations

import requests
from ngsildclient.rest import status
import json
class Rest:
    def __inti__():
        pass
        
    @classmethod
    def get(
        cls, 
        url,
        headers,
        **options,
        ):
        response = requests.get(url = url, headers = headers)
        return json.loads(response.text)

    @classmethod
    def post(
            cls, 
            body, 
            url,
            headers,
            **kargs
            ):
        response = requests.post(url = url, data = json.dumps(body), headers = headers)
        return status.handle_result(response.status_code, response.text)
    
    @classmethod
    def patch(
            cls,
            body,
            url ,
            headers,
            *kargs
    ):
        response = requests.patch(url=url, data= json.dumps(body), headers= headers)
        return status.handle_result(response.status_code, response.text)
    
    @classmethod
    def delete(
        cls, 
        url,
        headers ,
        **kargs
        ):
        response = requests.delete(url = url , headers= headers)
        return status.handle_result(response.status_code, response.text)