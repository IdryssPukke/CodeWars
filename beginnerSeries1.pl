paperwork(X,Y,Z) :- 
    ( Y < 0 ->  Z = 0 );
    ( X < 0 ->  Z = 0 );
    Z is Y * X.