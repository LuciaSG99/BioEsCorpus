########### FILTER BY TITLE MENTIONING #####
## 09/02/22 ##
# Author: Lucía Sánchez González

rm(list = ls())

library(dplyr)

################################################ ENGLISH CORPORA #########################################################

######### ENGLISH CORPORA FOUND IN SCOPUS:
# Open the file containing the metadata for each paper:
articles_sco_en <- read.csv("scopus_en.csv", sep = ";")


## Identify those articles which mentions the following expressions in their titles:
articles_sco_en_filtered <- filter(articles_sco_en, grepl("biomedical|clinical|medical|bio|biomedicine",Title, ignore.case = TRUE))
articles_sco_en_filtered <-filter(articles_sco_en_filtered, grepl("corpus",Title, ignore.case = TRUE))

## Filtering by removing those papers that do not have DOI:
articles_sco_en_filtered_V2 <- articles_sco_en_filtered[which(!articles_sco_en_filtered$DOI == ""),]

# Save the metadata of the articles in CSV:
write.csv(articles_sco_en_filtered_V2,"scopus_en_filtered.csv")


##### ENGLISH CORPORA FOUND IN WEB OF SCIENCE:
articles_wos_en <- read.csv("wos_en.csv", sep = ";", encoding = "UTF-8")

## Identify those articles which mentions the following expressions in their titles:
articles_wos_en_filtered <- filter(articles_wos_en, grepl("biomedical|clinical|medical|bio|biomedicine",Article.Title, ignore.case = TRUE))
articles_wos_en_filtered <-filter(articles_wos_en_filtered, grepl("corpus",Article.Title, ignore.case = TRUE))


## Filtering by removing those papers that do not have DOI:
articles_wos_en_filtered_V2 <- articles_wos_en_filtered[which(!articles_wos_en_filtered$DOI == ""),]

# Save the metadata of the articles in CSV:
write.csv(articles_wos_en_filtered_V2,"wos_en_filtered.csv")


##### ENGLISH CORPORA FOUND IN PUBMED:

articles_pub_en <- read.csv("pubmed_en.csv", sep = ",")

## Identify those articles which mentions the following expressions in their titles:
articles_pub_en_filtered <- filter(articles_pub_en, grepl("biomedical|clinical|medical|bio|biomedicine",Title, ignore.case = TRUE))
articles_pub_en_filtered <- filter(articles_pub_en_filtered, grepl("corpus",Title, ignore.case = TRUE))

## Filtering by removing those papers that do not have DOI:
articles_pub_en_filtered_V2 <- articles_pub_en_filtered[which(!articles_pub_en_filtered$DOI == ""),]

# Save the metadata of the articles in CSV:
write.csv(articles_pub_en_filtered_V2,"pub_en_filtered.csv") #save the results in a csv


########################## FILTERING BY DUPLICATES ############################################################# 

#remove duplicates:
duplicates_sco_pub <- intersect(articles_sco_en_filtered_V2$DOI,articles_pub_en_filtered_V2$DOI) 


duplicates_sco_wos <- intersect(articles_sco_en_filtered_V2$DOI,articles_wos_en_filtered_V2$DOI) 


articles_wos_en_final <- articles_wos_en_filtered_V2[!articles_wos_en_filtered_V2$DOI %in% duplicates_sco_wos,]
articles_pub_en_final <-  articles_pub_en_filtered_V2[!articles_pub_en_filtered_V2$DOI %in% duplicates_sco_pub,]

duplicates_wos_pub <- intersect(articles_pub_en_final$DOI,articles_wos_en_final$DOI)
articles_wos_en_final_V2 <- articles_wos_en_final[!articles_wos_en_final$DOI %in% duplicates_wos_pub,]

# Save the metadata of the final datasets with duplicates:
write.csv(articles_wos_en_final_V2,"wos_english_nodupl_filtered.csv")
write.csv(articles_pub_en_final,"pub_english_nodupl_filtered.csv")


################################################ SPANISH CORPORA #########################################################

######### SPANISH CORPORA FOUND IN SCOPUS:

articles_sco_es <- read.csv("scopus_es.csv", sep = ",", encoding = "UTF-8")

## Identify those articles which mentions the following expressions in their titles:
articles_sco_es_filtered <- filter(articles_sco_es, grepl("biomedical|clinical|medical|bio|biomedicine",Title, ignore.case = TRUE))
articles_sco_es_filtered <-filter(articles_sco_es_filtered, grepl("corpus",Title, ignore.case = TRUE))

## Filtering by removing those papers that do not have DOI:
articles_sco_es_filtered_V2 <- articles_sco_es_filtered[which(!articles_sco_es_filtered$DOI == ""),]

# Save the metadata of the articles in CSV:
write.csv(articles_sco_es_filtered_V2,"scopus_es_filtered.csv")

##### SPANISH CORPORA FOUND IN WEB OF SCIENCE:

articles_wos_es <- read.csv("wos_es.csv", sep = ";", encoding = "UTF-8")

## Identify those articles which mentions the following expressions in their titles:
articles_wos_es_filtered <- filter(articles_wos_es, grepl("biomedical|clinical|medical|bio|biomedicine",Article.Title, ignore.case = TRUE))
articles_wos_es_filtered <-filter(articles_wos_es_filtered, grepl("corpus",Article.Title, ignore.case = TRUE))

## Filtering by removing those papers that do not have DOI:
articles_wos_es_filtered_V2 <- articles_wos_es_filtered[which(!articles_wos_es_filtered$DOI == ""),]

# Save the metadata of the articles in CSV:
write.csv(articles_wos_es_filtered_V2,"wos_es_filtered.csv")


######### SPANISH CORPORA FOUND IN PUBMED:

articles_pub_es <- read.csv("pubmed_es.csv", sep = ",")

## Identify those articles which mentions the following expressions in their titles:
articles_pub_es_filtered <- filter(articles_pub_es, grepl("biomedical|clinical|medical|bio|biomedicine",Title, ignore.case = TRUE))
articles_pub_es_filtered <- filter(articles_pub_es_filtered, grepl("corpus",Title, ignore.case = TRUE))

## Filtering by removing those papers that do not have DOI:
articles_pub_es_filtered_V2 <- articles_pub_es_filtered[which(!articles_pub_es_filtered$DOI == ""),]

# Save the metadata of the articles in CSV:
write.csv(articles_pub_es_filtered_V2,"pub_es_filtered.csv") #save the results in a csv


########################## FILTER BY DUPLICATES ##### 

#remove duplicates:
duplicates_sco_pub_es <- intersect(articles_sco_es_filtered_V2$DOI,articles_pub_es_filtered_V2$DOI)
#Again the 2 articles from pubmed are in scopus, so this variable disappears. 

duplicates_sco_wos_es <- intersect(articles_sco_es_filtered_V2$DOI,articles_wos_es_filtered_V2$DOI)
#There are 2 articles from web of science that are in scopus. 

# Save without duplicates:
articles_wos_es_final <- articles_wos_es_filtered_V2[!articles_wos_es_filtered_V2$DOI %in% duplicates_sco_wos_es,]

write.csv(articles_wos_es_final,"wos_es_nodupl_filtered.csv")




