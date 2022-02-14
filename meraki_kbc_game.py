question_list=[
"how many continents are there?",
"what is the capital of india?",
"NG mei kaunsa course hota hai?"
]
options_list=[
    ["four","nine","seven","eight"],
    ["chandigarh","bhopal","chennai","delhi"],
    ["software engineering","counselling","tourism","agriculture"]
]

solution_list = [3, 4, 1]
life_line = [[1,3],[2,4],[1,2]]
money = [1000 , 5000 , 10000]
i=0
sum = 0 
count = 0
while i<len(question_list):
    print(i+1,question_list[i])   
    j=0
    while j<=len(options_list):
        print(j+1,options_list[i][j])
        j+=1
    if count<1:
        print("do you want to use life line :")
        s = (input("enter yes or no:"))
        if s == "yes":
            count+=1
            print(life_line[i])
    else:
        print("you have already used life_line")                                                                                                                                                                                                                                          
    n=int(input("Enter the number:"))
    if n==solution_list[i]:
        sum = sum + money[i]
        print("ur ans is correct , you have won rupees" , sum,"only/-")
    else:
        print("ur ans is wrong game is over,you're total sum of money is rupees " , sum,"only/-")
        break
    i+=1