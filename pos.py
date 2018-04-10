import os
import spacy
import copy
import requests
nlp = spacy.load('en_core_web_lg')

def get_POS(sentence):
  doc = nlp(sentence)
  pos_array = []
  for token in doc: 
    pos_array.append(token.tag_)
  return pos_array

def get_pos_match(submission, question_id):
  submission_pos = get_POS(submission)
  url = os.environ['CMS_URL'] or 'http://localhost:3100' # Replace with context aware variable.
  r = requests.get(url + '/questions/' + question_id + '/responses')
  responses = r.json()
  responses_with_pos = []
  for response in responses:
    resp_w_pos = copy.deepcopy(response)
    resp_w_pos["pos"] = get_POS(resp_w_pos["text"])
    responses_with_pos.append(resp_w_pos)
  match = None;
  for response in responses_with_pos: 
    if (submission_pos == response["pos"]):
      match = response
  return match
  
  

