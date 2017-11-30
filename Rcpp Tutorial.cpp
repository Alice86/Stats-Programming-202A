/* ~~~~~~~~~~~~~~~~~~
 ~~~~~~~~~~~~~~~~~~~~~
 ~~~ Rcpp tutorial ~~~
 ~~~~~~~~~~~~~~~~~~~~~
 ~~~~~~~~~~~~~~~~~~~~~~ */

#include <Rcpp.h>
using namespace Rcpp;

/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~ Example 1: Simple linear function  ~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

// [[Rcpp::export]]
double linearFunction1(double x){
       
       // Set aside memory for our output y
       double y = 0.0;
       
       // Compute output
       y = x + 3;
       
       // Return output. Note that y is of class "double", and
       // that's why we have "double" in front of our function name
       return y;
       
}

// [[Rcpp::export]]
int linearFunction2(int x){
       
       // Print statement in Rcpp
       Rcout << "x is equal to " << x << std::endl;
       
       // Set aside memory for our output y
       int y = 0;
       
       // Compute output
       y = x + 3;
       
       // Return output. Note that y is of class "int", and
       // that's why we have "int" in front of our function name
       return y;
       
}


/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~ Example 2: Looping in Rcpp  ~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

// [[Rcpp::export]]
int loopExample(int n){
       
       int x = 0;
       
       for(int i = 0; i <= n; i++){
              x = x + i;
       }
       
       return(x);
       
}



/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~ Example 3: Importing R functions into Rcpp  ~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

// [[Rcpp::export]]
double rbetaCPP(Function f, double x1, double x2) {
       
       // Declare our output
       double output = 0.0;
       
       // Create a list to store R function output
       List temporary;
       
       // Call R function and store results into our list
       temporary = f(1, x1, x2);
       
       // Access the 0th element of that list, aka our desired output
       output = as<double>(temporary[0]);
       
       return output;
}


/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~ Example 4: Vectors and matrices  ~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

// [[Rcpp::export]]
NumericVector vectorManipulation1(NumericVector x, NumericVector y){
       
       double sumy = sum(y);
       int lengthx = x.size();
       NumericVector z(lengthx);
       
       // Calculate the sum of the elements of y
       for(int i = 0; i <= lengthx; i++){
              z[i] = (i * x[i]) / sumy;
       }
       
       return z;
       
}


// [[Rcpp::export]]
NumericVector vectorManipulation2(NumericVector x, NumericVector y){
       
       double sumy = sum(y);
       int lengthx = x.size();
       NumericVector z(lengthx);
       
       // Calculate the sum of the elements of y
       for(int i = 0; i <= lengthx; i++){
              x[i] = x[i] - 1;
              z[i] = (i * x[i]) / sumy;
       }
       
       return z;
       
}


// [[Rcpp::export]]
NumericMatrix basicMatrix(int n, int m = 3){
       
       // Matrix of n rows & m columns (filled with zeros)
       NumericMatrix y(n, m);
       
       for(int i = 0; i < y.nrow(); i ++){
              for(int j = 0; j < y.ncol(); j ++){
                     Rcout << "i is " << i << ", and j is " << j << std::endl;
                     y(i, j) = i + j;
              }
       }
       
       return y;
       
}

////////////////////
// Be careful !!! //
////////////////////

// [[Rcpp::export]]
double vectorManipulation3(NumericVector x){
       
       x = 3 * x;
       double z = sum(x);
       
       return z;
       
}


/* ~~~~~~~~~~~~~~~~~~~~~~~~
~~~ Example 5: Void  ~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~ */

// [[Rcpp::export]]
void changeX(NumericVector x){
       x = 2 * x;
}


/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~ Example 6: Output lists  ~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

// [[Rcpp::export]]
List sumDiff(NumericVector x, NumericVector y){
       
       int lengthx = x.size();
       int lengthy = y.size();
       NumericVector z1(lengthx);
       NumericVector z2(lengthx);
       List output;
       
       if(lengthx != lengthy){
              throw std::range_error("Inputs must be of equal length");
       }
       
       z1 = x + y;
       z2 = x - y;
       
       output["Sum"]  = z1;
       output["Diff"] = z2;
       return(output);
       
}
