# -*- coding: utf-8 -*-

"""
@author: Lucía Sánchez González

Script to analyzes the number and frequencies of the entities and relations annotated

"""
# Import the libraries:
import os    

## Obtain the total number of terms annotated:
all_terms = {"Proteína":[],"Enfermedad":[],"Signo":[],"Síntoma":[],"Glúcido":[],"Lípido":[],"Medicamento":[],"Sigla":[],"Abreviatura":[],"Alias":[],"something":[]} # contain all the terms per category    
all_relations = {"Implicado_en":[],"Activa":[],"Inhibe":[],"Interacciona_con":[],"Alivia":[],"Cura":[],"Previene":[],"Refiere_a":[]} # contain all the relations per category    

brat_files = {} # dict with annotators as keys and their json files with annotations as values
brat_folders = os.listdir("../../Annotations/brat_annotations")


for folder in brat_folders: #obtain the brat files for each annotator
    brat_files[folder.split("_")[1]] = os.listdir("../Annotations/brat_annotations/"+str(folder))

      
for annotator in brat_files: # for each annotator
    
    for brat_file in brat_files[annotator]:
        file = open("../Annotations/brat_annotations/brat_"+ str(annotator)+"/"+str(brat_file),'r', encoding = "utf-8")
        terms_relations = {} 
        for line in file.readlines(): 
            
            annotation = line.split()
            if annotation[0].startswith("T"): # if it that line contains a term
                terms_relations[annotation[0]] = annotation[4] # store the term as value and the category as key
                all_terms[annotation[1]].append(annotation[4])
                
            
            if annotation[0].startswith("R"): # if it is a relation
                sub = annotation[2].split(":")[1] # identify the subject term
                obj = annotation[3].split(":")[1] # identify the object term
                sub_obj = [terms_relations[sub],terms_relations[obj]] # subject term _ object term
                all_relations[annotation[1]].append(sub_obj) # added it to the list of all relations

#Remove duplicated terms:              
for category in all_terms: 
       all_terms[category] = set(all_terms[category])          

# Remove duplicated relations:
all_relations_clean = {"Implicado_en":[],"Activa":[],"Inhibe":[],"Interacciona_con":[],"Alivia":[],"Cura":[],"Previene":[],"Refiere_a":[]} # contain all the terms per category    
for rels in all_relations: 
    for rel in all_relations[rels]:
        
        if rel in all_relations_clean[rels]:
            next
        else:
            all_relations_clean[rels].append(rel)


##### Export numbers:
    
## Calculate total:
 
## A. ENTITIES:    
total_terms = 0
for categ in all_terms:
    n_terms = len(all_terms[categ])
#    print(n_terms)
    total_terms = total_terms + n_terms

## Nº Terms por category:

freq_categ = {}
num_entity_categ = {}
    
for label in all_terms:
 #   print("\n"+str(label))
 #   print(len(label))
    proportion = len(all_terms[label])/total_terms        
    
    freq_categ[label] = str(proportion)
    num_entity_categ[label] = str(len(all_terms[label]))

with open("total_number_entities.txt", "w") as output:
        output.write("\t".join(num_entity_categ.keys()))
        output.write("\n")
        output.write("\t".join(num_entity_categ.values()))
        
with open("frequencies_entities.txt", "w") as output:
        output.write("\t".join(freq_categ.keys()))
        output.write("\n")
        output.write("\t".join(freq_categ.values()))

## B. RELATIONS: 
    
total_rels = 0
for r in all_relations_clean:
    n_rels = len(all_relations_clean[r])
#    print(n_rels)
    total_rels = total_rels + n_rels
        

## Nº rels por category:
freq_rel = {}
num_rel_categ = {}
    
for label_rel in all_relations_clean:
 #   print("\n"+str(label))
 #   print(len(label))
    proportion_rel = len(all_relations_clean[label_rel])/total_rels        
    
    freq_rel[label_rel] = str(proportion_rel)
    num_rel_categ[label_rel] = str(len(all_relations_clean[label_rel]))
    

with open("total_number_relations.txt", "w") as output:
        output.write("\t".join(num_rel_categ.keys()))
        output.write("\n")
        output.write("\t".join(num_rel_categ.values()))
        
with open("frequencies_relations.txt", "w") as output:
        output.write("\t".join(freq_rel.keys()))
        output.write("\n")
        output.write("\t".join(freq_rel.values()))

    
    