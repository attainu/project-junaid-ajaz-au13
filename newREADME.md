# project-junaid-ajaz-au13
AttainU project Repositor
two arrays of pieces for each player
8x8 piece array with references to these pieces
a parse function, which turns the input from the user into a list of two tuples denoting start and end points
a checkmateExists function which checks if either players are in checkmate
a checkExists function which checks if either players are in check
a main loop, which takes input, runs it through the parser, asks the piece if the move is valid, 
and moves the piece if it is.
If the move conflicts with another piece, that piece is removed. is check(mate) is run,
and if there is a checkmate, the game prints a message as to who wins.
