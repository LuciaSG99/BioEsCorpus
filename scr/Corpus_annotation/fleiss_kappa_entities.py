# -*- coding: utf-8 -*-
"""

@author: Lucía Sánchez González

This scripts allows to measure the Fleiss' Kappa of the entities annotated by the annotators for each file

"""

# Import the libraries:
import numpy 
import os
from statsmodels.stats.inter_rater import fleiss_kappa
from functions_corpus import list_term_label
import pandas as pd
import numpy as np



Annotator_files = {} 
folders = os.listdir("../../Annotations/JSON") ## list with the annotations in the JSON files
names_files = os.listdir("../../Files_sample") ## list with the clinical reports
name_files_clean = [] # variable storing the names of the reports

for name in names_files:
    name = name.replace(".txt","")
    name_files_clean.append(name) # remove the sufix ".txt" from the name's file

for annotator in folders:
        Annotator_files[annotator] = os.listdir("../../Annotations/JSON/"+str(annotator)) 
             
annotators_names = Annotator_files.keys()

# Panda dataframe that will contain the Fleiss' Kappa value for each report
fleiss_kappa_per_file = pd.DataFrame(columns=["Fleiss' kappa"], index = name_files_clean)

# Calculate the number of annotators that annotate each term as a category:
for file in name_files_clean:
    with open("../all_terms_per_file/"+str(file)+".tsv") as f: # open the file with all the entities from that clinical report
        line = f.readline()
        all_terms = line.split("\t") 
        
        all_entities = []
        for term_label in all_terms:
            all_entities.append(term_label.split("_")[0])
        all_entities = set(all_entities) # list of all the terms annotated in that file without duplicates
            
        initial_anno = np.zeros(len(all_terms))
        labels = ["Proteína","Enfermedad","Signo","Síntoma","Glúcido","Lípido","Medicamento","Sigla","Abreviatura","Alias","something","NULL"]
        
        # Create the contigency table of the entities:
        df_categ = pd.DataFrame(np.zeros((len(all_entities),len(labels))),index=all_entities, columns = labels)
        
        terms_dict_annotator = {}
        
        for ent in all_entities:
                                   
            for annotator_name in annotators_names: # for each annotator:
                terms_dict_annotator[annotator_name] = [] # first create a empty list that will contain their annotated terms   
            
                # Apply a function that allows to obtain the list of terms that annotator has annotated by the json file:
                terms_dict_annotator[annotator_name] = set(list_term_label("../../Annotations/JSON/"+str(annotator_name)+"/"+str(file)+".json",terms_dict_annotator[annotator_name]))
                temp_entitie_list = {}
                for ter_lab in terms_dict_annotator[annotator_name]:
                    temp_entitie_list[ter_lab.split("_")[0]] = ter_lab.split("_")[1].rstrip()
                
                if ent in temp_entitie_list.keys(): # if the annotator has annotate that term:
                    
                    df_categ.loc[[ent],[temp_entitie_list[ent]]] += 1 # add 1 to their category 
                
                else:   # if the annotator has not annotate that term:
                    df_categ.loc[[ent],["NULL"]] += 1 # add one to the category NULL

            
        df_categ.to_csv(str(file)+"ann_term.tsv", sep = "\t")
        df_categ = df_categ.astype(int)
        
        
        ## Calculate Fleiss' Kappa:
        matrix_terms = df_categ.values           

        fleiss_statsmodels = fleiss_kappa(matrix_terms) # apply the Fleiss' Kappa equation
        print("Fleiss Kappa score for "+str(file)+": {0}".format(fleiss_statsmodels))
        
        fleiss_kappa_per_file.loc[[file],["Fleiss' kappa"]] = fleiss_statsmodels
        
# Save the results:
fleiss_kappa_per_file.to_csv('fleiss_kappa_entities.tsv', sep = "\t")


