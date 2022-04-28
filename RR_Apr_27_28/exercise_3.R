data <- state.name
col1 <- c()
col2 <- c()
path = './test.csv'

for (state in data) {
  col1 <- c(col1,toupper(state))
  col2 <- c(col2,tolower(state))
}
data.csv <- data.frame( col1,col2)



write.csv(data.csv, path, row.names=FALSE)
