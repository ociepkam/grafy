if (!require('dplyr')) install.packages('dplyr')
library(dplyr)

files = list.files(pattern=".csv") 

all_files = data.frame()
for (file in files) {
  dat = read.table(file, header=TRUE, sep=";")
  all_files = bind_rows(all_files, dat) 
}

write.csv2(all_files, "MERGED_RESULTS.csv") # name of the file







