#############################################
## Description: Linear regression in R 
## Author: Levon Demirdjian
## Email: levondem@gmail.com
## Last updated: 10/02/2017
#############################################

#############################
## Example 1: 'trees' data ##
#############################

## First, load data. In this case, we will be 
## using the 'trees' data that comes with R
data(trees)

## Look at data
head(trees)

## Plot data
plot(trees$Girth, trees$Volume, xlab = "Girth", ylab = "Volume", 
     main = "Tree girth vs volume")

## Use R's 'lm' functional to create a linear 
## model.
log_trees <- log(trees)
my_model  <- lm(Volume ~ Girth, data = trees)

## Look at summary of results
summary(my_model)

## Look at all properties of my_model
names(my_model)

## Make some graphics 
par(mfrow=c(1,2))

## Residual plot
plot(my_model, which = 1)

## QQ Plot
plot(my_model, which = 2)

## Fit looks questionable... try taking the log of the variables
my_model_log  <- lm(Volume ~ Girth, data = log_trees)

## Look at summary of results
summary(my_model_log)

## Look at all properties of my_model_log
names(my_model_log)

## Residual plot
plot(my_model_log, which = 1)

## QQ Plot
plot(my_model_log, which = 2)

## Plot data
par(mfrow=c(1,1))
plot(log_trees$Girth, log_trees$Volume, 
     xlab = "log Girth", ylab = "log Volume", 
     main = "Tree girth vs volume (in log scale)")
abline(my_model_log, col = 'blue', lty = 2)

##############################################
## Example 2: Reading data from a .txt file ##
##############################################

## Read in data using read.table
my_data <- read.table('mystery_data.txt', header = T)

## Look at data
par(mfrow=c(2,2))
hist(my_data$x, xlab = 'x', main = "Histogram of x")
hist(my_data$u, xlab = 'u', main = "Histogram of u")
hist(my_data$z, xlab = 'z', main = "Histogram of z")
hist(my_data$y, xlab = 'y', main = "Histogram of y")

## Try several linear models
model1 <- lm(y ~ x + u + z, data = my_data)
summary(model1)

model2 <- lm(y ~ x + u + z + x * u, data = my_data)
summary(model2)

model3 <- lm(y ~ x + u + z + x * u + 0, data = my_data)
summary(model3)
