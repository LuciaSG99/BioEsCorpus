# -*- coding: utf-8 -*-
"""
@author: Lucía Sánchez González

"""
# Import the libraries:
import numpy 
import os
from statsmodels.stats.inter_rater import fleiss_kappa
from functions_corpus import create_list_relations
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
        Annotator_files[annotator] = os.listdir("../Annotations/JSON/"+str(annotator)) 
             
annotators_names = Annotator_files.keys()

# Panda dataframe that will contain the Fleiss' Kappa value for each report
fleiss_kappa_per_file_rel = pd.DataFrame(columns=["Fleiss' kappa"], index = name_files_clean)


# Calculate the number of annotators that annotate each relation:
for file in name_files_clean:
    with open("../../all_rels_per_file/"+str(file)+"_rels.tsv") as f: # open the file with all the relations from that clinical report
        line = f.readline()
        all_rels = line.split("\t")
        
        all_relations = [] # list of all the relations annotated in that file without duplicates
        for term_term_label in all_rels:
            all_relations.append("_".join([term_term_label.split("_")[0],term_term_label.split("_")[1]]))
        all_relations = set(all_relations)
            
        initial_anno = np.zeros(len(all_rels))
        labels_rels = ["Implicado en","Activa","Inhibe","Interacciona con","Alivia","Cura","Previene","Refiere a","NULL"]
        
        # Create the contigency table of the relations:
        df_categ_rel = pd.DataFrame(np.zeros((len(all_relations),len(labels_rels))),index=all_relations, columns = labels_rels)
        
        rels_dict_annotator = {}
        
        for rel in all_relations:
                                   
            for annotator_name in annotators_names: # for each annotator:
                rels_dict_annotator[annotator_name] = [] # first create a empty list that will contain their annotated relations   
            
                # Apply a function that allows to obtain the list of relations that annotator has annotated by the json file:
                rels_dict_annotator[annotator_name] = set(create_list_relations("../../Annotations/JSON/"+str(annotator_name)+"/"+str(file)+".json",rels_dict_annotator[annotator_name]))
                temp_rels_list = {}
                for ter_ter_lab in rels_dict_annotator[annotator_name]:
                    temp_rels_list["_".join([ter_ter_lab.split("_")[0],ter_ter_lab.split("_")[1]])] = ter_ter_lab.split("_")[2].rstrip()
                
                if rel in temp_rels_list.keys():
                    
                    df_categ_rel.loc[[rel],[temp_rels_list[rel]]] += 1
                
                else:
                    df_categ_rel.loc[[rel],["NULL"]] += 1

            
        df_categ_rel.to_csv(str(file)+"ann_rels.tsv", sep = "\t")
        df_categ_rel = df_categ_rel.astype(int)
        
        ## Calculate Fleiss' Kappa:
        matrix_rels = df_categ_rel.values        
       
        fleiss_statsmodels_rels = fleiss_kappa(matrix_rels)  # apply the Fleiss' Kappa equation
        print("Fleiss Kappa score for "+str(file)+": {0}".format(fleiss_statsmodels_rels))
        
        fleiss_kappa_per_file_rel.loc[[file],["Fleiss' kappa"]] = fleiss_statsmodels_rels

# Save the results:      
fleiss_kappa_per_file_rel.to_csv('fleiss_kappa_relations.tsv', sep = "\t")
