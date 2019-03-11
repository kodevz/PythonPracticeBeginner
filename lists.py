
string = "BANANA"
string = string.upper()
vowels = 'AEIOU'
consonant = 'BCDFGHJKLMNPQRSTVWXYZ'
lString = [ string[i:j] for i in range(len(string) + 1) for j in range(i + 1, len(string) + 1) ]
prob = len(lString)
p1 = []
p2 = []
cprop = sum([1 for word in lString if word[0] in consonant])
vprop = sum([1 for word in lString if word[0] in vowels])

whoisplay = 'p1'
playing = True
p1score = 0
p2score = 0

while playing:
    
    if whoisplay == 'p1':
        s = input("Stuart Enter Your words start With Consonant :")
        if s[0] in consonant and s not in p1:
            p1score += lString.count(s)
            print("Stuart {}".format(p1score))
            whoisplay = 'p2'
            p1.append(s.upper())
    
    if whoisplay == 'p2':
        s = input("Kevin Enter Your words start With Vowels :") 
        if s[0] in vowels and s not in p2:
            p2score += lString.count(s)
            print("Kevin {}".format(p2score))
            whoisplay = 'p1'
            p2.append(s.upper())
     
    if p1score == cprop:
        whoisplay = 'p2'
    if p2score == vprop:
        whoisplay = 'p1'
        
    if p1score + p2score == prob:     
        if p1score > p2score:
            print('Stuart {}'. format(p1score))
        else:
            print('Kevin {}'. format(p2score))
        
        break
     
        


       
        
    


