import functions


def handler(event, context):
    function = event['function']

    if function not in functions.supported:
        return {"status": 404, "response": f"Invalid function {function}"}

    payload = event['payload']

    return functions.supported[function](payload)
