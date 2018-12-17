# -*- coding: utf-8 -*-
print("Hongyuan Li");
print("\n")
print("Exercise 1");
print("\n")
print("(a)",(5/3));
print("This method prints 1.6666666666666667, which is 5/3 rounded up.");

print("(b)", (5%3));
print("Prints out 5 mod 3, output is 2.");

print("(c)", (5.0/3));
print("Though being diffrent types, this still prints out the same output as (a).");

print("(d)", (5/3.0));
print("Though being diffrent types, this still prints out the same output as (a).");

print("(e)", (5.2%3));
print("This prints out 5.2 mod 3.");

print("\n")
print("EXERCISE 2");
print("\n")

print("(a) The result shows -- OverflowError: (34, 'Numerical result out of range') ");
print("I guess this is too big to compute.....");

print("(b)", (1.0 + 1.0 - 1.0) );
print("double 1.0 + 1.0 then - 1.0 so it returns 1.0.");

print("(c)", (1.0 + 1.0e20 - 1.0e20) );
print("This prints 0, im guessing the 1.0 is too small so its ignored?");

print("\n")
print("EXERCISE 3");
print("\n")

print("(a)", float(123) );
print("Turns 123 into a float.");

print("(b)", float('123') );
print("Turns '123' (which is a string?) into a float.");

print("(c)", float('123.23'));
print("Turns '123.23' into a float.");

print("(d)", float(123.23));
print("Turns 123.23 into a float.");

print("(e) int(123.23) actually creates a ValueError: invalid literal for int() with base 10: '123.23'");
print("Value Error");

print("(f)", int(float('123.23')));
print("Turns the input '123.23' into a float then to an int I belive, the output should be int.");

print("(g)", str(12));
print("Turns the input 12 into a string.");

print("(h)", str(12.2));
print("Tunrs the input 12.2 into a string.");

print("(i)", bool('a'));
print("a is a value so it returns true.");

print("(j)", bool(0));
print("0 or empty returns false in Python.");

print("(k)", bool(0.1));
print("Its not empty so returns true.");

print("\n")
print("EXERCISE 4");
print("\n")

print(range(5));
print("returns range(0, 5) which I belive is used for index, and (0,5) would generate 0 to 4.");
print(type(range(5)));
print("The output shows that the class of range() is 'range' ");

print("\n")
print("EXERCISE 5");
print("\n")

def excercise5divisible():

     number_found = 0;
     x = 11;

     while number_found < 20:
        a = (x % 5 == 0);
        b = (x % 7 == 0);
        c = (x % 11 == 0);

        if a == True and b and c:
           print(x);
           number_found += 1;
     
        x += 1; 


print("The frist 20 numbers that are divisible by 5, 7 and 11");
excercise5divisible();

print("\n")
print("EXERCISE 6");
print("\n")

print("(a)");
def is_prime(n):
  if n < 2:
    return False;
  for x in range(2,n-1):   
        if (n % x) == 0:     
            return False
        else:                   
            return True
print("\n")
print("(b)");
print("\n")
print("I didnt understand the question.")

print("\n")
print("(c)");
print("\n")

def primes_up_to(n):
        x = 0;
        while x <= n:
                if is_prime(x):
                        print(x);
                x += 1;
                

print("test")
print(primes_up_to(10));

print("\n")
print("(d)");
print("\n")

def first_n_primes(n):
    x=0;

print("\n")
print("EXERCISE 7");
print("\n")
print("(a)");
print("\n")
listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 

def printlist(list):
  for x in range(len(list)): 
    print (list[x]);
    
printlist(listA);

print("\n")
print("(b)");
print("\n")
#i know this reverse the list
def reverseprint(list):
    list.reverse();
    print(list);
      
reverseprint(listA);

print("\n")
print("(c)");
print("\n")

def LenFunc(list):

	counter = 0; 
	for x in list:
		counter += 1;
	return(counter);

print(LenFunc(listA));

print("\n")
print("EXERCISE 8");
print("\n")
print("(a)");
print("\n")

a = [1, 3, 5, 7, 9, 11, 13, 15, 17];
print("a=", a);

print("(b)");

b = a;
print("b= ", b);
print("b is the same");
print("(c)");
b[1] = 25;
print("(d)");
print("a=", a);
print("a changed too.");
print("(e)");
c = a[:]
print("(f)");
c[2] = 0;
print("(g)");
print("a=", a);
print("c=", c);
print("c changed but a is unchanged")
print("\n")
print("EXERCISE 9");
print("\n")
def merglists(list):

	joined = [];
	for i in list:
		joined += i

	return (joined);

lista = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]];


print( merglists(lista));

print("\n")
print("EXERCISE 10");
print("I dont know")
print("\n")
print("\n")
print("EXERCISE 11");
print("\n")
testlist = [2,4,6,8]
print("recursion")
def recursion(list):
    product = 1;

    if len(list) == 0:
         return product;
    else:
                product = list[0];
                del list[0];
                return product * recursion(list);

print( recursion(testlist));
print("iteration")
def iteration(list):

        i = 1;
        p = list[0]; #product using p just to make it diffrect from above

        if len(list) == 0:
                return 0;

        while i < len(list):
                p = p * list[i];
                i += 1;
                
        return p;

print(iteration(testlist));
print("\n")
print("EXERCISE 12");
print("\n")
print("??? that is not a question but okay.")
