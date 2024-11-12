def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    for word in open('wordlist'):
        engine.queue(target.req, word.rstrip())


def handleResponse(req, interesting):
    # filter responses based on request Time
    if req.time > 500000:
        table.add(req)
