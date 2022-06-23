# BioEsCorpus

This repository contains the scripts, tools and data generated from the process of annotate 18 Spanish clinical reports from the Spanish Clinical Case Corpus (SPACCC) (https://doi.org/10.5281/zenodo.2560316) with biomedical entities and semantic relations.

Three annotators had to identify the following eleven types of entities: Gen, Proteína, Glúcido, Lípido, Enfermedad, Síntoma, Signo, Medicamento, Alias, Abreviatura and Sigla. 
And the next eight semantic relations: "Implicado en", "Activa", "Inhibe", "Interacciona con",  "Previene", "Alivia", "Cura" and "Refiere a".
The annotations were done employing TextAE annotation tool (https://textae.pubannotation.org) embedded in HTML files containing the text of the clinical reports. 
Finally there were identified 324 entities from ten of the groups of entities, and 170 relations from five of the eight types. 

Content:

- brat_annotations: It contains 3 folder, one for each annotator. They contain the eighteen annotations made by the annotator in brat format.

- Clinical_Reports_SPACCC: It contais the 18 original clinical reports (.txt) from SPACCC.

- Pub_Annotations: It contains 3 folder, one for each annotator. They contain eighteen JSON files with the annotations in PubAnnotation format, which is the original output from TextAE.

- TextAE: It contains the 18 HTML files of TextAE containing the text from the clinical reports already uploaded. The folder lib contains all the libraries neccesary to allow TextAE to work. 

- Annotation_guideline_Tool_Usage_Guide.pdf: PDF file which contains firstable a guide with indications in how to annotate using TextAE, and secondly the annotation guideline provided to the annotators with the indications in how to procee with the annotations. 

- scr: contains all the scripts employed for the whole process. The programming language employed was Python. 

These resources are freely distributed under a Creative Commons Attribution 4.0 International License.
