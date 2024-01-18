whats_between(A, B, [A]) :- 
    A >= B.

whats_between(A, B, [A|R]) :-
    A < B,
    AA is A + 1,
    whats_between(AA, B, R).


# whats_between(A, B, R) :- numlist(A, B, R).
