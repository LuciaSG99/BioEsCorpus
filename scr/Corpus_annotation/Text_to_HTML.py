# -*- coding: utf-8 -*-
"""

@author: Lucía Sánchez González

This script allows to insert the clinical reports (.txt files) inside the TextAE editor and obtained it in a HTML file

"""
# Import the libraries:
import os
from string import Template



tool		= open("template.html", "r",encoding='utf-8') # Import the HTML template of TextAE 
template 	= Template(tool.read())
path_bioannotations	= "./docker/Html-files/annotations/"  
path_files = "../../Files_SPACCC" # path to the clinical reports
folder_texts = os.listdir("../../Files_SPACCC") # list with the the clinical reports 


for report in folder_texts: # for each report
    
    
    file = open(os.path.join(path_files,report),'r+',encoding="utf-8") # open the file
    lines = file.readlines() # list with the lines of the report
    new_report = "" 
    
    for line in lines: # for each line
        if line == "\n": # if the line is a empty line, skip it
            next
        else:
            new_report += line.replace("\"","\'") # remove rare symbols 
    
    report_name = report.replace(".txt","") # store the report name in a variable
    report_final = new_report.replace("\n"," ") # Remove the \n from the reports, if not the text is not showed in the html
    report_final = report_final + " ID Texto: " + str(report) # Add the name of the report inside the text in order to identify them afterwards
    
    d = {'content': report_final} # create a dictionary with the content that will be embedded in the HTML file    
    result = template.substitute(content = d['content'], encoding='utf-8') # insert the content
    filename = str(report_name)+".html" 
    output 	= open(os.path.join(path_bioannotations, filename), "w", encoding= 'utf-8') # create the HTML file
    output.write(result)
    output.close()
    print(filename, "created successfully!")

   
 


     

