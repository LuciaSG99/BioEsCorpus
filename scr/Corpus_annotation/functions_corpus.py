# -*- coding: utf-8 -*-
"""

@author: Lucía Sánchez González

script with two functions to obtain a list with the entities and a list with the relations

"""

import json

# Function to obtain a list of the entities:
def list_term_label(url_json,entities_label): # it needs the url of the json file and empty list that will store the entities
    with open(url_json,'r', encoding = "utf-8") as file_annotations:
            file = json.load(file_annotations) #load the json file
            text = list(file['text']) #store the text of the clinic report as list of characters  
        
            list_entities = file['denotations']                
                  
            ## Identify the relations and entities:
            for entitie in list_entities:
           
                if entitie['obj'] == "-":
                    tag = "Signo"
                else:
                    tag = entitie['obj'].replace("https://es.dbpedia.org/page/","")
                        
                word ="".join(text[entitie['span']["begin"]:entitie['span']["end"]]) # identify the word in the text 
                
                #Coordenates:
                entities_label.append(str(word)+"_"+str(tag))  # add word_label to the list   
               
    return entities_label

# Function to obtain a list of the relations:
def create_list_relations(url_json,list_relations_final): # it needs the url of the json file and empty list that will store the relations
    with open(url_json,'r', encoding = "utf-8") as file_annotations:
            file = json.load(file_annotations) #load the json file
            text = list(file['text']) #store the text of the clinic report as list of characters  
        
            list_entities = file['denotations']                
            annotations_entities = {}
            
            ## Identify the relations and entities:
            for entitie in list_entities:
                annotations_entities[entitie['id']] = []
                
                if entitie['obj'] == "-":
                    tag = "Signo"
                else:
                    tag = entitie['obj'].replace("https://es.dbpedia.org/page/","")
                        
                word ="".join(text[entitie['span']["begin"]:entitie['span']["end"]]) # identify the word in the text 
                
                #Coordenates:
                start_offset = entitie['span']["begin"] # index of the first character of the annotated span
                end_offset = entitie['span']['end'] # index of the last character of the annotated span
                
                
                annotations_entities[entitie['id']].append(entitie['id'])
                annotations_entities[entitie['id']].append(tag)
                annotations_entities[entitie['id']].append(start_offset)
                annotations_entities[entitie['id']].append(end_offset)                
                annotations_entities[entitie['id']].append(word)
            
            
            ### IDENTIFY THE RELATIONS:
            list_relations = file['relations'] 
           
            for relation in list_relations: # for relation in list of relations                                                               
                
                subj =  annotations_entities[relation['subj']][4]                
                obj =  annotations_entities[relation['obj']][4]  
                pred = relation["pred"]                

                rel_total = str(subj)+"_"+str(obj)+"_"+ str(pred)
                list_relations_final.append(rel_total)
   
    return list_relations_final






