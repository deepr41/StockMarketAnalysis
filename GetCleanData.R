
#initiate the library to getData
library(quantmod)

findDetails<- function(companyname){

  getSymbols(companyname,src = 'yahoo')
  if(substr(companyname,start = 1,stop = 1)=="^"){
    companyname=substr(companyname,start = 2,stop = nchar(companyname))
  }
  
  #Get the data as a dataframe and and a Date column to it
  
  df<-as.data.frame(coredata(get(companyname)))
  Date<-index(get(companyname))
  df<-cbind(Date,df)
  
  
  #find indexes of NA data
  myList = c()
  for(i in 1:nrow(df)){
    if(is.na(df[i,2])){
      myList<-c(myList,i)
    }
  }
  
  #delete NA rows
  if(!is.null(myList)){
    df<-df[-myList,]
  } 
  companyname<-gsub('.','_',x = companyname,fixed = TRUE)
   #output the proper csv file
   #the file is written to "./Data/Raw"
  write.csv(paste("./Data/Raw/",paste(companyname,"Raw.csv",sep = ""),sep = ""),x=df,row.names = F,eol = "\n")
  
  print("Details Written")
  #print(length(myList))

}
#retrieve arguments from command line


args<-as.vector(read.csv("Companies.txt")[,1])

for(i in args){
  findDetails(i)
  # Sys.sleep(1)
  # print(i)
}

