library(ggplot2)
table(diamonds$cut)
diamonds$cut=factor(diamonds$cut, levels=c("Fair","Good","Very Good","Premium","Ideal"))
round(prop.table(table(diamonds$cut))*100, digits=1)
summary(diamonds[c("x","y","z")])
normalize<-function(x){
  return ((x-min(x))/(max(x)-min(x)))
}
normalize(c(1,2,3,4,5))
normalize(c(10,20,30,40,50))
diamonds_n <- as.data.frame(lapply(diamonds[c(1,5,6,7,8,9,10)],normalize))
head(diamonds)
summary(diamonds)
diamonds_train = diamonds_z[1:26970, ]
diamonds_test = diamonds_z[26970:53940,]
diamonds_train_labels = diamonds[1:26970,2]
diamonds_test_labels = diamonds[26970:53940,2]
#install.packages("class")
library(class)
diamonds_test_pred <- knn(train=diamonds_train, test=diamonds_test, cl=diamonds_train_labels,
                          k=3)
#install.packages("gmodels")
#library(gmodels)
CrossTable(x =diamonds_test_labels,y=diamonds_test_pred,prop.chisq=FALSE)
diamonds_z = as.data.frame(scale(diamonds[c(1,5,6,7,8,9,10)]))
summary(diamonds_z$price)