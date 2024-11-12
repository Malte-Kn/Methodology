def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    for word in open('wordlist'):
        engine.queue(target.req, word.rstrip())


def handleResponse(req, interesting):
    # filter responses based on request Time or some error in response
    pattern = re.compile(r'\b(error|Error|syntax|Syntax)\b')
    if req.time > 40000000 or bool(pattern.search(req.response.encode('utf8'))):
        table.add(req)
