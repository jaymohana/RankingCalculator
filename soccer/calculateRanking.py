import re
from operator import itemgetter

dict = {}

def scoreCalculator(text):
    for line in text:
        fields = line.split(",")

        team1 = fields[0][0:(re.search("\d", fields[0])).start()].strip()
        team2 = fields[1][0:(re.search("\d", fields[1])).start()].strip()

        dict.setdefault(team1, 0)
        dict.setdefault(team2, 0)

        score1 = int(re.search(r'\d+', fields[0]).group(0))
        score2 = int(re.search(r'\d+', fields[1]).group(0))

        if score1 > score2:
            dict[team1] += 3
        elif (score1 == score2):
            dict[team1] += 1
            dict[team2] += 1
        else:
            dict[team2] += 3

    print("Rankings compiled!")

    # returning here just for the automated test.
    return dict

def compileRanking(outputFormat):
    s = sorted(dict.items(), key=itemgetter(0))
    rankings = sorted(s, key=itemgetter(1), reverse=True)
    createTable(rankings, outputFormat)

def createTable(rankings, outputFormat):
    prevScore = rankings[0][1]
    currentRank = 1
    sameRank = 0
    outputStr = ""

    for scoreItem in rankings:
        team = scoreItem[0]
        points = scoreItem[1]

        if points == prevScore:
            rank = currentRank
            sameRank = sameRank + 1
        elif points < prevScore:
            currentRank = currentRank + sameRank
            rank = currentRank
            prevScore = points
            sameRank = 1

        end = ""
        if points == 1:
            end = "pt"
        else:
            end = "pts"

        output = "%s. %s, %s %s\n" % (rank, team, points, end)
        outputStr = outputStr + output

    if outputFormat == "t" or outputFormat == "T":
        textFile = open("Output table.txt", "w")
        textFile.write(outputStr)
        textFile.close()
    else:
        print("Season Rankings: ")
        print()
        print(outputStr)

    # returning here just for the automated test.
    return outputStr
