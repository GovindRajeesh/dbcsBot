import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from tools import botResponse

# Download necessary NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Preprocess the responses
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token)
              for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stop_words]

    # print(tokens)
    return " ".join(tokens)


def get_response(user_input):
    user_input = preprocess(user_input)

    print(user_input)

    responses = botResponse(user_input)

    resStr=""

    # if len(responses)>1:
    #     for response in responses:
    #         if response["strength"]==1:
    #             responses.remove(response)
    #             break

    gStrngth=list(map(lambda e:e["strength"],responses))
    gStrngth.sort(reverse=True)

    try:
        gStrngth=gStrngth[0]
    except:
        return ""

    for response in filter(lambda r:r["strength"]==gStrngth,responses):
        if len(response["response"])==1:
            resStr+=f"{response['response'][0]}"
        elif "resType" in list(response.keys()) and response["resType"]=="random":
            resStr+=f"{random.choice(response['response'])}"
        else:
            for res in response["response"]:
                resStr+=res

                if (len(responses)>1 and response!=responses[-1]) or (res!=response["response"][-1]):
                    resStr+="\n\n"

        resStr+="\n"
            
    return resStr


def run_chatbot():
    print("ChatBot: Hello! How can I assist you? (type 'exit' to end)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("ChatBot: Goodbye!")
            break

        # Get the chatbot's response based on user input
        response = get_response(user_input)
        print("ChatBot:", response, sep="\n")


# if __name__ == "__main__":
#     run_chatbot()
