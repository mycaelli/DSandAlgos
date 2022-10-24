'''
input: 2 arrays, competitions and results
      competitions has the form [homeTeam, awayTeam], each team is a String 
      results has information about the winner of each competition, 
        results[i] denotes the winner of competitions[i]. 
        In results array, 1 means the homeTeam won and 0 means the awayTeam won.

output: The winner of the tournament

There will always be one tournament winner and there will neve be any ties.


Example
competitions [['HTML', 'C#'], ['C#', 'Python'], ['Python', 'HTML']]
results [0, 0, 1]
winner Python
'''
def tournamentWinner(competitions, results):
    winner = {}

    for idx, i in enumerate(results):
      if i == 0:
        try:
          winner[competitions[idx][1]] += 1
        except:
          winner[competitions[idx][1]] = 1
      else:
        try:
          winner[competitions[idx][0]] += 1
        except:
          winner[competitions[idx][0]] = 1
        
    return max(winner, key=winner.get)
