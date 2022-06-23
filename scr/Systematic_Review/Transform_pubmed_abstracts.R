rm(list = ls())

##### PROCESSING PUBMED PAPERS ABOUT SPANISH CORPUS ##########################

# Open the pubmed file with the metadata:
data_es = scan("pubmed_es.txt", what = character(), sep = "\n",encoding = "UTF-8")

articles_es = data.frame() #data frame that will contain the abstracts

switch_line = FALSE

for (line in data_es){
  
  if (startsWith(line, prefix = "AB  -")) {
    
    switch_line = TRUE
    abstract = character()
    abstracts = c(abstract,gsub(x = line,pattern = "AB  - ", replacement = ""))
    
  }
  
  if (startsWith(line, prefix = "  ") & switch_line){
    
    abstracts = c(abstracts,gsub(x = line,pattern = "^ +", replacement = " "))
    
  }
  
  if (!startsWith(line, prefix = "  ") & !startsWith(line, prefix = "AB  -")){
    
    if (switch_line){
      abstracts = paste(abstracts,collapse = " ")
      abstracts = gsub(abstracts,pattern = " +", replacement = " ")
      articles_es = rbind(articles_es,abstracts)
    }
    switch_line = FALSE 
  }
}

colnames(articles_es) = "Abstract" 

### Combine them with the rest of information:
data_rest_es <- read.csv("pubmed_es_info.csv", sep = ";")

#Staying only with the columns we are interested in:
data_rest_es <- data_rest_es[,c(2,3,6,7,8)] #Title, Authors, Journal or Book, Year of publication and DOI

pub_es_combined <- cbind(data_rest_es,articles_es) # combine the dataframes

write.csv(pub_es_combined, file = "pubmed_es.csv",row.names = FALSE) # save the metadata

##### PROCESSING PUBMED PAPERS ABOUT ENGLISH CORPUS ####
rm(list = ls())

data_en = scan("pubmed_en.txt", what = character(), sep = "\n")

articles_en = data.frame() #data frame that will contain the abstracts

switch_line = FALSE

for (line in data_en){
  if (startsWith(line, prefix = "AB  -")) {
    
    switch_line = TRUE
    abstract = character()
    abstracts = c(abstract,gsub(x = line,pattern = "AB  - ", replacement = ""))
    
  }
  
  if (startsWith(line, prefix = "  ") & switch_line){
    
    abstracts = c(abstracts,gsub(x = line,pattern = "^ +", replacement = " "))
    
  }
  
  if (!startsWith(line, prefix = "  ") & !startsWith(line, prefix = "AB  -")){
    
    if (switch_line){
      abstracts = paste(abstracts,collapse = " ")
      abstracts = gsub(abstracts,pattern = " +", replacement = " ")
      articles_en = rbind(articles_en,abstracts)
    }
    switch_line = FALSE 
  }
}

colnames(articles_en) = "Abstract"

### Combine them with the rest of information:
data_rest_en <- read.csv("pubmed_info_en.csv", sep = ",", encoding = "UTF-8")

#Staying only with the columns we are interested in:
data_rest_en <- data_rest_en[,c(2,3,6,7,11)] #Title, Authors, Journal or Book, Year of publication and DOI

pub_en_combined <- cbind(data_rest_en,articles_en)

write.csv(pub_en_combined, file = "pubmed_en.csv",row.names = FALSE)
