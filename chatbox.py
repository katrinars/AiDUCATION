import random
import json

import torch
import json

from model import NN

import nltk
nltk.download('punkt')
from langHelper import bag_of_words, tokenize
# numpy torch nltk
FILE = "model2.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NN(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()


with open('tagResponse.json', 'r') as json_data:
    intents = json.load(json_data)

    
def getReturnMsg(questions):
    sentence = tokenize(questions)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to('cpu')
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.85:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    else:
        return "Hmmm... I'm not sure what you mean..."