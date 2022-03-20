import codecs
import json
import numpy as np
import data_embedder
import sentence_normalizer

obj_text = codecs.open('embedded_data.json', 'r', encoding='utf-8').read()
data = json.loads(obj_text)
ft_model = data_embedder.load_embedding_model()

def normalize(vec):
    norm = np.linalg.norm(vec)
    return norm

def cosine_similarity(A, B):
    normA = normalize(A)
    normB = normalize(B)
    sim = np.dot(A, B) / (normA * normB)
    return sim

def detect_intent(data, inp_vec):
    max_sim_score = -1
    max_sim_intent = ''
    max_score_avg = -1
    break_flag = 0
    for intent in data['intents']:
        scores = []
        intent_flag = 0
        tie_flag = 0
        for pattern in intent['patterns']:
            pattern = np.array(pattern)
            similarity = cosine_similarity(pattern, inp_vec)
            similarity = round(similarity, 6)
            scores.append(similarity)
            if similarity == 1.000000:
                intent_flag = 1
                break_flag = 1
                break
            elif similarity > max_sim_score:
                max_sim_score = similarity
                intent_flag = 1
            elif similarity == max_sim_score and intent_flag == 0:
                tie_flag = 1
        
        if tie_flag == 1:
            scores.sort()
            top = scores[:min(4, len(scores))]
            intent_score_avg = np.mean(top)
            if intent_score_avg > max_score_avg:
                max_score_avg = intent_score_avg
                intent_flag = 1

        if intent_flag == 1:
            max_sim_intent = intent['tag']
        if break_flag == 1:
            break
    if break_flag != 1 and ((tie_flag == 1 and intent_flag == 1 and max_score_avg < 0.06) or (intent_flag == 1 and max_sim_score < 0.6)):
        max_sim_intent = ""
    return max_sim_intent

def classify(inp):
    inp = sentence_normalizer.preprocess_main(inp)
    inp_vec = data_embedder.embed_sentence(inp, ft_model)
    output_intent = detect_intent(data, inp_vec)
    return output_intent