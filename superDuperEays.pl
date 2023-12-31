problem(X, Result) :-
  ( number(X) ->  Result is  X * 50 + 6;  Result = "Error").