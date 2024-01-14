square_sum([],0).
square_sum([X|T], Result) :-
  square_sum(T, NewResult),
  Result is NewResult + X * X.