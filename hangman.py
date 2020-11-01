import random as rd
from words import word_list
def get_random_word():
    random_word=rd.choice(word_list)
    return random_word
def hangman():
    word=str(get_random_word())
    word_as_list=list(word)
    print("     WELCOME TO HANGMAN!!!     ")
    user_name=input("What's your name: ")
    print("Hello",user_name+". Let's begin!!!")
    print("""
    RULES:
    Guess the word by entering 1 character at a time 
    or the whole word itself. The length of the word   
    will be given. If you are able to guess in 6 turns,  
    then you will be declared as winner.
          """)
    turns=6
    check=0
    print("This time length of word is",len(word))
    already_guessed_wrong=[]
    while(turns!=0):
        guessed_word=input("Guess the word: ")
        if(len(guessed_word)==1 and guessed_word.isalpha()):
            if(guessed_word in word_as_list):
                word_as_list.remove(guessed_word)
                if(len(word_as_list)==0):
                    check=1
                    break
            else:
               if(guessed_word in already_guessed_wrong):
                   print("You have already guessed this word.")
               else:
                    turns=turns-1
                    already_guessed_wrong.append(guessed_word)
                    print("Your guess was wrong. You have",turns,"turns left.")
                    display_hangman(turns)
           
        elif(len(guessed_word)==len(word) and guessed_word.isalpha()):
            if(guessed_word==word):
                check=1
                break
            elif(guessed_word in already_guessed_wrong):
                print("You have already guessed this word.")
            else:
                turns=turns-1
                already_guessed_wrong.append(guessed_word)
                print("Your guess was wrong. You have",turns,"turns left.")
                display_hangman(turns)
        else:
             print("""
            ERROR: Wrong Input.
            Please try again.
                  """)
    if(check==1):
        print("You Won!!")
        display_hangman(turns)
    else:
        print("You Lost!!")
        print("The answer is",word)
        display_hangman(turns)
        
def display_hangman(turn):
    hangmans=[
        """
        ___________    
       |           |
       |           |
       |           |
       |           0
       |          \\|/
       |           |
       |          / \\
       |
       |
       |

       """,
       """
        ___________    
       |           |
       |           |
       |           |
       |           0
       |          \\|/
       |           |
       |          / 
       |
       |
       |

       """,
       """
        ___________    
       |           |
       |           |
       |           |
       |           0
       |          \\|/
       |           |
       |           
       |
       |
       |
       
       """,
       """
        ___________    
       |           |
       |           |
       |           |
       |           0
       |          \\|
       |           |
       |           
       |
       |
       |

       """,
       """
        ___________    
       |           |
       |           |
       |           |
       |           0
       |           |
       |           |
       |          
       |
       |
       |

       """,
       """
        ___________    
       |           |
       |           |
       |           |
       |           0
       |          
       |           
       |          
       |
       |
       |

       """,
       """
        ___________    
       |           |
       |           |
       |           |
       |           
       |          
       |           
       |           
       |
       |
       |

       """]

    print(hangmans[turn])
if __name__=="__main__":
    times=1
    while(times):
        hangman()
        print("Do you want to play again? Yes or No")
        play_again=input()
        if(play_again=="Yes"):
            times=1
        else:
            times=0
        
  



      


























        
            
    
