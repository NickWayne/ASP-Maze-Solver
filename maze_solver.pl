node(X, Y) :- board(X, Y, 0).
node(X, Y) :- start(X, Y, 0).
root(X, Y) :- start(X, Y, 0).

%%%%%%%%%%%%%%%%%% Edge detection %%%%%%%%%%%%%%%%%%
edge(X1, Y, X2, Y) :- node(X1, Y), node(X2, Y), X1 != X2,
                      #absdiff(X1, X2, 1).

edge(X, Y1, X, Y2) :- node(X, Y1), node(X, Y2), Y1 != Y2,
                      #absdiff(Y1, Y2, 1).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%% Disjunction %%%%%%%%%%%%%%%%%%
inpath(X1, Y1, X2, Y2) | notpath(X1, Y1, X2, Y2) :- edge(X1, Y1, X2, Y2).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%% Ineficient %%%%%%%%%%%%%%%%%%
% reachable(X1, Y1, X2, Y2) :- inpath(X1, Y1, X2, Y2).
% reachable(X1, Y1, X2, Y2) :- reachable(X1, Y1, X, Y), inpath(X, Y, X2, Y2).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%% Including root %%%%%%%%%%%%%%%%%%
reachable(X1, Y1, X2, Y2) :- root(X1, Y1), inpath(X1, Y1, X2, Y2).
reachable(X1, Y1, X2, Y2) :- reachable(X1, Y1, X, Y), inpath(X, Y, X2, Y2).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%% Solving / minimizing %%%%%%%%%%%%%%%%%%
:- not reachable(1,0,18,19). %change to start and end, X, Y pairs
:~ inpath(X1, Y1, X2, Y2).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
