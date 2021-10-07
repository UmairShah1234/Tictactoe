# tic tac toe
import random
import time

class tic:
    board= {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
    def display_board(self):
        print(f"{self.board['1']}|{self.board['2']}|{self.board['3']}\n"
              f"-+-+-\n"
              f"{self.board['4']}|{self.board['5']}|{self.board['6']}\n"
              f"-+-+-\n"
              f"{self.board['7']}|{self.board['8']}|{self.board['9']}")


class play(tic):
    def choosep1(self,pos):
        if self.board[pos]==' ':
            self.board[pos]='X'
            return 1
        elif self.board[pos]=='X' or self.board[pos]=='0':
            print(f'{pos} is invalid')
            return 0

    def choosecomp(self,pos):
        if self.board[pos]==' ':
            self.board[pos]='0'
        elif self.board[pos]=='X' or self.board[pos]=='0':
            pos=random.randint(1,9)
            self.choosecomp(str(pos))

    def comp(self):
        count=1
        while count<=4:
            pos=random.randint(1,9)
            self.choosecomp(str(pos))
            count +=1
            self.display_board()
            break

    def play1(self):
        count=1
        while  count<=5:
            pos=input("Enter the pos : ")
            call=self.choosep1(pos)
            if call==1:
                count +=1
                self.display_board()
                break

    def game(self):
        print("Welcome to tic-tac-toe")
        self.display_board()
        win=False
        while win !=True:
            print("your chance")
            self.play1()
            time.sleep(1)
            print("Computer's chance")
            self.comp()
            if self.board['1'] == self.board['2'] == self.board['3'] != ' ':
                if self.board['1']=='X':
                    print("Congratulations! player 1 wins")
                    win=True
                else:
                    print("computer won")
                    win=True
            elif self.board['4'] == self.board['5'] == self.board['6'] != ' ':
                if  self.board['4']=='X':
                    print("Congratulations! player 1 wins")
                    win = True
                else:
                    print("computer won")
                    win = True
            elif self.board['7'] == self.board['8'] == self.board['9'] != ' ':
                if  self.board['7']=='X':
                    print("Congratulations! player 1 wins")
                    win = True
                else:
                    print("computer won")
                    win = True
            elif self.board['1'] == self.board['4'] == self.board['7'] != ' ':
                if  self.board['1']=='X':
                    print("Congratulations! player 1 wins")
                    win = True
                else:
                    print("computer won")
            elif self.board['2'] == self.board['5'] == self.board['8'] != ' ':
                if  self.board['2']=='X':
                    print("Congratulations! player 1 wins")
                    win = True
                else:
                    print("computer won")
            elif self.board['3'] == self.board['6'] == self.board['9'] != ' ':
                if  self.board['3']=='X':
                    print("Congratulations! player 1 wins")
                    win = True
                else:
                    print("computer won")
                    win = True
            elif self.board['1'] == self.board['5'] == self.board['9'] != ' ':
                if  self.board['1']=='X':
                    print("Congratulations! player 1 wins")
                    win = True
                else:
                    print("computer won")
                    win = True
            elif self.board['3'] == self.board['5'] == self.board['7'] != ' ':
                if  self.board['3']=='X':
                    print("Congratulations! player 1 wins")
                    win = True
                else:
                    print("computer won")
                    win = True


if __name__=="__main__":
    game=play()
    game.game()

