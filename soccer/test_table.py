import unittest
from soccer import calculateRanking

class testing(unittest.TestCase):
    def testLeague(self):
        expected = {'Liverpool': 12, 'Norwich': 3, 'West Ham': 7, 'Man City': 10, 'Crystal Palace': 7, 'Everton': 4,
                    'Burnley FC': 4, 'Southampton': 4, 'Watford': 1, 'Brighton': 4, 'Bournemouth': 4, 'Sheff Utd': 5,
                    'Tottenham': 4, 'Aston Villa': 3, 'Leicester City': 8, 'Wolves': 3, 'Newcastle': 4, 'Arsenal': 6,
                    'Man United': 5, 'Chelsea': 5}
        scores = [
            'Liverpool 4,Norwich 1\n',
            'West Ham 0,Man City 5\n',
            'Crystal Palace 0,Everton 0\n',
            'Burnley FC 3,Southampton 0\n',
            'Watford 0,Brighton 3\n',
            'Bournemouth 1,Sheff Utd 1\n',
            'Tottenham 3,Aston Villa 1\n',
            'Leicester City 0,Wolves 0\n',
            'Newcastle 0,Arsenal 1\n',
            'Man United 4,Chelsea 0\n',
            'Arsenal 2,Burnley FC 1\n',
            'Southampton 1,Liverpool 2\n',
            'Brighton 1,West Ham 1\n',
            'Everton 1,Watford 0\n',
            'Norwich 3,Newcastle 1\n',
            'Aston Villa 1,Bournemouth 2\n',
            'Man City 2,Tottenham 2\n',
            'Sheff Utd 1,Crystal Palace 0\n',
            'Chelsea 1,Leicester City 1\n',
            'Wolves 1,Man United 1\n',
            'Aston Villa 2,Everton 0\n',
            'Norwich 2,Chelsea 3\n',
            'Brighton 0,Southampton 2\n',
            'Man United 1,Crystal Palace 2\n',
            'Watford 1,West Ham 3\n',
            'Sheff Utd 1,Leicester City 2\n',
            'Liverpool 3,Arsenal 1\n',
            'Bournemouth 1,Man City 3\n',
            'Tottenham 0,Newcastle 1\n',
            'Wolves 1,Burnley FC 1\n',
            'Southampton 1,Man United 1\n',
            'Crystal Palace 1,Aston Villa 0\n',
            'Chelsea 2,Sheff Utd 2\n',
            'Newcastle 1,Watford 1\n',
            'Man City 4,Brighton 0\n',
            'West Ham 2,Norwich 0\n',
            'Leicester City 3,Bournemouth 1\n',
            'Burnley FC 0,Liverpool 3\n'
        ]
        result = calculateRanking.scoreCalculator(scores)
        self.assertEqual(result, expected)

    def testRanking(self):
        expected = "1. Liverpool, 12 pts\n2. Man City, 10 pts\n3. Leicester City, 8 pts\n4. Crystal Palace, 7 pts\n4. West Ham, 7 pts\n6. Arsenal, 6 pts\n7. Chelsea, 5 pts\n7. Man United, 5 pts\n7. Sheff Utd, 5 pts\n10. Bournemouth, 4 pts\n10. Brighton, 4 pts\n10. Burnley FC, 4 pts\n10. Everton, 4 pts\n10. Newcastle, 4 pts\n10. Southampton, 4 pts\n10. Tottenham, 4 pts\n17. Aston Villa, 3 pts\n17. Norwich, 3 pts\n17. Wolves, 3 pts\n20. Watford, 1 pt\n"
        input = [['Liverpool', 12], ['Man City', 10], ['Leicester City', 8], ['Crystal Palace', 7],
                 ['West Ham', 7], ['Arsenal', 6], ['Chelsea', 5], ['Man United', 5], ['Sheff Utd', 5],
                 ['Bournemouth', 4],['Brighton', 4], ['Burnley FC', 4], ['Everton', 4], ['Newcastle', 4],
                 ['Southampton', 4],['Tottenham', 4], ['Aston Villa', 3], ['Norwich', 3], ['Wolves', 3], ['Watford', 1]]
        result = calculateRanking.createTable(input, "c")
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
