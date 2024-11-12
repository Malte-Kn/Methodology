def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    for word in open('wordlist'):
        engine.queue(target.req, word.rstrip())


def handleResponse(req, interesting):
    # Attempt to decode JSON response
    try:
        response_json = json.loads(req.response.decode('utf-8'))
    except json.JSONDecodeError:
        return
    # Extract the message from the JSON response
    msg = response_json.get("msg", "")
    pattern = "Not Found User Info!"
    # Check if the pattern matches the message
    if pattern in msg:
        table.add(req)
