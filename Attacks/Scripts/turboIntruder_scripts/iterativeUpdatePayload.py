def queueRequests(target, wordlists):
    global res
    res = ""
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )
    firstWords = [line.rstrip() for line in open('worlist1')]
    secondWords = [line.rstrip() for line in open('worlist2')]

    for firstWord in firstWords:
        for secondWord in secondWords:
            temp = res + secondWord
            engine.queue(target.req, [firstWord, temp])

def handleResponse(req, interesting):
    global res
    # Check if the response status is 500
    if req.status == 500:
        # Get the second word from the request
        secondWord = req.request[1].replace(req.request[0], '')
        # Update the res variable
        res += secondWord
        # Requeue the request with updated res
        for firstWord in [line.rstrip() for line in open('wordlist1')]:
            engine.queue(target.req, [firstWord, res])
