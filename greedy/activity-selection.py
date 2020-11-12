import string
alphabet = list(string.ascii_uppercase)

class Activity:
    def __init__(self,i, s, f):
        self.index = i
        self.start = s
        self.end = f
      
    def __lt__(self, other): 
        return self.end < other.end

    def print(self):
        print(f'{self.index}[{self.start},{self.end}]', end=' ')
        
def max_activities(s , f ):
    n = len(f) 
    activities = [Activity(alphabet[i],s[i],f[i]) for i in range(0,n)]
    activities.sort(reverse=False)
    solution = []
    print('Atividades disponíveis:')
    for a in activities:
        a.print()
    print('')
    i = 0
    solution.append(activities[i])    
    for j in range(n):
        if activities[j].start >= activities[i].end:
            # activities[j].print()
            solution.append(activities[j]) 
            i = j
    return solution
  
if __name__ == "__main__":
    s = [4,6,13,4,2,6,7 ,9 ,1 ,3 ,9] 
    f = [8,7,14,5,4,9,10,11,6,13,12]
    n = len(f)
    solution = max_activities(s, f)
    print('Atividades selecionadas:')
    for activity in solution:
        activity.print()