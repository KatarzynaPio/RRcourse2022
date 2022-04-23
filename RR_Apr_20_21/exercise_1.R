x <- 1:100
y <- 1:100
for (i in 3*x) {
  y[i] = 'Fizz'
}
for (i in 5*x) {
  y[i] = 'Buzz'
}
for (i in 15*x) {
  y[i] = 'FizzBuzz'
}
write(y[x],1)
