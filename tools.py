import json

def botResponse(tokens):
    file=open("./data/data.json")
    data=json.load(file)
    file.close()

    file=open("./data/variables.json")
    variables=json.load(file)
    file.close()

    responses=[]

    for response in data:
        for identifier in response["identifier"]:
            if identifier in tokens:
                responses.append(response)

    for var in variables:
        if var["name"] in tokens:
            responses.append(
                {
                    "identitfiers":[var["name"]],
                    "response":var["value"],
                    "strength":1
                }
            )

    return responses