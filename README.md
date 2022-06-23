# BioEsCorpus

This repository contains the scripts, tools and data generated from the process of annotate 18 Spanish clinical reports from the Spanish Clinical Case Corpus (SPACCC) (https://doi.org/10.5281/zenodo.2560316) with biomedical entities and semantic relations.
It also contains the scripts use to perfom a systematic review of biomedical annotated corpus in English and Spanish.

Three annotators had to identify the following eleven types of entities: Gen, Proteína, Glúcido, Lípido, Enfermedad, Síntoma, Signo, Medicamento, Alias, Abreviatura and Sigla. 
And the next eight semantic relations: "Implicado en", "Activa", "Inhibe", "Interacciona con",  "Previene", "Alivia", "Cura" and "Refiere a".
The annotations were done employing TextAE annotation tool (https://textae.pubannotation.org) embedded in HTML files containing the text of the clinical reports. 
Finally there were identified 324 entities from ten of the groups of entities, and 170 relations from five of the eight types. 

Content:

- Annotations: It contains 2 folders:

1) JSON: Three folders, one per annotator. They contain the JSON files output of TextAE
2) brat_annotations: Three folders, one for each annotator. They contain the eighteen annotations made by the annotator in brat format.

- Files_sample: It contais the 18 original clinical reports (.txt) from SPACCC.

- TextAE: It contains the 18 HTML files of TextAE containing the text from the clinical reports already uploaded. The folder lib contains all the libraries neccesary to allow TextAE to work. 

- Annotation_guideline_Tool_Usage_Guide.pdf: PDF file which contains firstable a guide with indications in how to annotate using TextAE, and secondly the annotation guideline provided to the annotators with the indications in how to procee with the annotations. 

- scr: It contains two folders:
1) Corpus_annotation: folder with the scripts used to annotated the corpus. Language programming: Python. 
2) Systematic_Review: folder with the scripts used to performed the Inclusion-Exclusion filtering step in the Systematic Review. Language programming: R.

These resources are freely distributed under a Creative Commons Attribution 4.0 International License.
