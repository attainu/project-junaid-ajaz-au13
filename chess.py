import itertools
import copy
import inspect
WHITE = "white"
BLACK = "black"
gameboard = None

def canSeeKing(kingpos,piecelist, overridegameboard = None):
global gameboard
overridegameboard = overridegameboard or gameboard
for piece,position in piecelist:
if piece.isValid(position,kingpos,piece.Color,overridegameboard):
return True

def isCheck(overridegameboard = None):
global gameboard
#ascertain where the kings are, check all pieces of opposing color against those kings,
# then if either get hit, check if its checkmate
overridegameboard = overridegameboard or gameboard
king = King
kingDict = {}
pieceDict = {BLACK : [], WHITE : []}
for position,piece in overridegameboard.items():
if type(piece) == king:
kingDict[piece.Color] = position
print(piece)
pieceDict[piece.Color].append((piece,position))
#white
if canSeeKing(kingDict[WHITE],pieceDict[BLACK], overridegameboard):
return WHITE
if canSeeKing(kingDict[BLACK],pieceDict[WHITE], overridegameboard):
return BLACK
return False

class Game:
def init(self):
global gameboard
self.playersturn = WHITE
self.message = "Input Your Move"
gameboard = self.gameboard = {}
self.placePieces()
print("Chess program. Enter moves in algebraic notation separated by space. Example: a2-a4")
self.main()

def placePieces(self):

    for i in range(0,8):
        self.gameboard[(i,1)] = Pawn(WHITE,uniDict[WHITE][Pawn],1)
        self.gameboard[(i,6)] = Pawn(BLACK,uniDict[BLACK][Pawn],-1)
        
    placers = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
    
    for i in range(0,8):
        self.gameboard[(i,0)] = placers[i](WHITE,uniDict[WHITE][placers[i]])
        self.gameboard[((7-i),7)] = placers[i](BLACK,uniDict[BLACK][placers[i]])
    placers.reverse()

    
def main(self):
    
    while True:
        self.printBoard()
        print(self.message)
        self.message = ""
        startpos,endpos = self.parseInput()
        try:
            target = self.gameboard[startpos]
        except:
            self.message = "could not find piece; index probably out of range"
            target = None
            
        if target:
            print("found "+str(target))
            if target.Color != self.playersturn:
                self.message = "This is Not Your Turn"
                continue
            if target.isValid(startpos,endpos,target.Color,self.gameboard):
                hasLegalMoves = False
                for position in self.gameboard:
                    piece = self.gameboard[position]
                    if (piece.Color == self.playersturn):
                        for move in piece.availableMoves(position[0], position[1], self.gameboard):
                            overridegameboard = copy.deepcopy(self.gameboard)
                            overridegameboard[move] = self.gameboard[position]
                            del overridegameboard[position]
                            if (isCheck(overridegameboard) != self.playersturn):
                                hasLegalMoves = True
                                break
                if (not hasLegalMoves):
                    if (isCheck() == self.playersturn) : print("You are in checkmate. " + ({WHITE: BLACK, BLACK: WHITE})[self.playersturn] + " wins!")
                    else : print("Stalemate. Nobody wins!")
                    return
                overridegameboard = copy.deepcopy(self.gameboard)
                overridegameboard[endpos] = self.gameboard[startpos]
                del overridegameboard[startpos]
                if (isCheck(overridegameboard) == self.playersturn) : self.message = "You are not allowed to put yourself in check!"
                else:
                    self.message = "That Move is Allowed"
                    self.gameboard[endpos] = self.gameboard[startpos]
                    del self.gameboard[startpos]
                    Check = isCheck()
                    if (Check):
                        self.message = "Player is in check"
                    if self.playersturn == BLACK:
                        self.playersturn = WHITE
                    else : self.playersturn = BLACK
            else : 
                self.message = "invalid move" + str(target.availableMoves(startpos[0],startpos[1],self.gameboard))
                print(target.availableMoves(startpos[0],startpos[1],self.gameboard))
        else : self.message = "There is no Piece in That Space"
            
def parseInput(self):
    try:
        a,b = input().split('-')
        a = ((ord(a[0])-97), int(a[1])-1)
        b = (ord(b[0])-97, int(b[1])-1)
        print(a,b)
        return (a,b)
    except:
        print("error decoding input. please try again")
        return((-1,-1),(-1,-1))

"""def validateInput(self, *kargs):
    for arg in kargs:
        if type(arg[0]) is not type(1) or type(arg[1]) is not type(1):
            return False
    return True"""
    
def printBoard(self):
    print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
    for i in range(0,8):
        print("-"*32)
        print(chr(i+97),end="|")
        for j in range(0,8):
            item = self.gameboard.get((i,j)," ")
            print(str(item)+' |', end = " ")
        print()
    print("-"*32)