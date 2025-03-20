import random as r


list=["Rock","Paper","Scissor"]

comp_ch=r.choice(list)

player_ch=str(input("Enter ur choice (Rock,Paper,Scissor) :"))

if (player_ch==comp_ch) :
    print("Tie!")
elif (player_ch=="Paper") and (comp_ch=="Scissor"):
    print("You win!",comp_ch)
elif (player_ch=="Scissor") and (comp_ch=="Rock"):
    print("You win!",comp_ch)
elif (player_ch=="Rock") and (comp_ch=="paper"):
    print("You win!",comp_ch)
else :
    print("You lost",comp_ch)