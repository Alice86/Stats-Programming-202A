library(Rcpp)

extern "C" SEXP fibWrapper(SEXPxs){ 
       int x = Rcpp::as<int>(xs);
       int fib = fibonacci(x);
       return (Rcpp::wrap(fib));
}


library(inline)
incltxt <- '
int fibonacci(const int x){ 
       if (x == 0) return(0);
       if (x == 1) return(1);
       return fibonacci(x - 1) + fibonacci(x - 2);
       }'

fibRcpp<-cxxfunction(signature(xs="int"),
                     plugin="Rcpp", 
                     incl=incltxt, body='
                     int x = Rcpp::as<int>(xs);
                     return Rcpp::wrap( fibonacci(x) );
')

#include <Rcpp.h> 
using namespace Rcpp:
// [[Rcpp::export]]
double linearFunction1(double x) {}


#include <Rcpp.h> 
using namespace Rcpp:
       
// [[Rcpp::export]]
int fibonacci(const int x) {
       if (x < 2)
              return x;
       else
              return (fibonacci(x - 1)) + fibonacci(x - 2);
}

##memoization solution courtesy of PatBurns 
mfibR <- local({
       memo <- c(1, 1, rep(NA, 1000)) 
       f <- function(x) {
              if (x == 0) return(0) 
              if (x < 0) return(NA) 
              if (x > length(memo))
                     stop("x too big for implementation") 
              if (!is.na(memo[x])) 
                     return(memo[x])
              ans <- f(x-2) + f(x-1) 
              memo[x] <<- ans
              ans
       } 
})

## memoization using C++ 2 
mincltxt<-’
#include <algorithm>
#include<vector> 
#include <stdexcept> 
#include<cmath> 
#include <iostream>
class Fib {
       public:
              Fib(unsigned int n = 1000) {
                     memo.resize(n); // reserve n elements
                     std::fill( memo.begin(), memo.end(), NAN ); // set to NaN
                     memo[0] = 0.0; // initialize for 
                     memo[1] = 1.0; // n=0 and n=1
              }
       double fibonacci(int x) {
              if (x < 0)
                     return( (double) NAN );  // guard against bad input
              if (x >= (int) memo.size())
                     throw std::range_error(\"x too large for implementation\");
                                             if (! ::isnan(memo[x]))
                                                 return(memo[x]);  // if exist, reuse values
                                             // build precomputed value via recursion 
                                             memo[x] = fibonacci(x-2) + fibonacci(x-1);
                                             return( memo[x] );
       } private:
                                             std::vector< double > memo;  // internal memory for precomp.
       };
’
                                             
