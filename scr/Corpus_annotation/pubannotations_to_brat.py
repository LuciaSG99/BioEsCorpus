# -*- coding: utf-8 -*-
"""
@author: Lucía Sánchez González

This script transforms the JSON file with the PubAnnotation annotations and transforms them into the brat format

"""

# Import the libraries:
import json
import os 
import shutil


## CREATE THE ANNOTATION FILES FOR EACH ANNOTATOR:

files = {} # dict with annotators as keys and their json files with annotations as values
annotators_folder = os.listdir("../../Annotations/JSON") # list with the annotators JSON files


for folder in annotators_folder: #obtain the files for each annotator
    files[folder.split("_")[1]] = os.listdir("./Annotations/JSON/"+str(folder)) # store them in a dictionary

      
for annotator in files: 
    print("Creating annotation files in brat format from folder: "+ str(annotator))
    
    for json_file in files[annotator]:
        
        annotations_entities = {} # dict with the categories as keys and the terms annotated as values
        annotations_relations = {} # dict with the predicates of the relations as keys and the subject and object term annotated as values
        
        with open("../../Annotations/JSON/Anotaciones_"+ str(annotator)+"/"+str(json_file),'r', encoding = "utf-8") as file_annotations:
            file = json.load(file_annotations) #load the json file
            text = list(file['text']) #store the text of the clinic report as list of characters  
            file_name = file['text'].split("ID Texto: ")[1] # obtain text ID
            file_name = file_name.replace(".txt",".json")
            # Rename the json files with their original name:
            file_annotations.close()
            os.rename(r"../../Annotations/JSON/Anotaciones_"+ str(annotator)+"/"+str(json_file),r"../../Annotations/JSON/Anotaciones_"+ str(annotator)+"/"+str(file_name))
                
           
            ## Prepare entities:
            list_entities = file['denotations']            
            
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
                
                
                annotations_entities[entitie['id']].append(entitie['id']) # add the ID of the entitie
                annotations_entities[entitie['id']].append(tag) # add the category
                annotations_entities[entitie['id']].append(start_offset) # add start of the offset
                annotations_entities[entitie['id']].append(end_offset)   # add end of the offset           
                annotations_entities[entitie['id']].append(word) # add the term annotated
                
            
            ## Prepare relations:
            list_relations = file['relations'] 
           
            for relation in list_relations: # for relation in list of relations
                annotations_relations[relation['id']] = []                    
                
                annotations_relations[relation['id']].append(relation['id']) # add the ID of the relation
                annotations_relations[relation['id']].append(relation['pred'].replace(" ","_")) # add the category of the relation
                annotations_relations[relation['id']].append(relation['subj']) # add the ID of the subject term         
                annotations_relations[relation['id']].append(relation['obj'])  # add the ID of the object term       
            
           ### WRITE FILE IN BRAT FORMAT:
            #1. Add annotated entities:
            with open(str(file_name.split(".")[0])+".ann", 'w', encoding= "utf-8") as f:
                
                # adding the entities:
                for ent in annotations_entities.values():
                    f.write(str(ent[0])+"\t"+str(ent[1])+" "+str(ent[2])+" "+str(ent[3])+"\t"+str(ent[4]))
                    f.write("\n")
                 # adding the relations:
                for rel in annotations_relations.values():
                    f.write(str(rel[0])+"\t"+str(rel[1])+" "+"Arg1:"+str(rel[2])+" "+"Arg2:"+str(rel[3]))
                    f.write("\n")
                    
            shutil.move(str(file_name.split(".")[0])+".ann","../Annotations/brat_annotations/brat_"+str(annotator)+"/"+str(file_name.split(".")[0])+".ann")     
                    
    

       
                     
            
      
    
    