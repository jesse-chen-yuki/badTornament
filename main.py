# This is a Python script used to simulate badminton games
# goal is to choose the best team lineup to maximize chance of winning the tournament

from datetime import datetime
import random

DEBUG = 0


class Player:
    def __init__(self, name='who', sex='M', strength=5, team=1):
        self.name = name
        self.sex = sex
        self.strength = strength
        self.team = team

    def display(self):
        print(self.name, self.sex, self.strength, self.team)


class Pair:
    def __init__(self, first=Player(), second=Player()):
        self.first = first
        self.second = second
        if first.sex == 'M' and second.sex == 'M':
            self.pType = 'MD'
        elif first.sex == 'F' and second.sex == 'F':
            self.pType = 'WD'
        else:
            self.pType = 'XD'


class TeamLineup:
    # team will play for 5 rounds round robin
    def __init__(self, teamnum=1, teamagainst=1, pair1=Pair(), pair2=Pair(), sit=Player()):
        self.teamNum = teamnum
        self.teamagainst = teamagainst
        self.pair1 = pair1
        self.pair2 = pair2
        self.sit = sit

    def display(self):
        print('my team, against team ', self.teamNum, self.teamagainst)
        print('pair1 ')
        self.pair1.first.display()
        self.pair1.second.display()
        print('pair2 ')
        self.pair2.first.display()
        self.pair2.second.display()
        print('sitting')
        self.sit.display()


class Team:
    def __init__(self, teamnum=1, playerlist=None, win=0):
        if playerlist is None:
            playerlist = []
        self.teamNum = teamnum
        self.playerList = playerlist
        self.lineUp = self.createlineup()
        self.win = win
        # self.displayTeam()

    def reset_score(self):
        self.win = 0

    def updatescore(self, newwin=0):
        self.win += newwin

    def display(self):
        print('team ', self.teamNum)
        for al in self.lineUp:
            al.display()
        print('wins ', self.win)

    # create 5 lineup for each of the round
    def createlineup(self):

        sitList = [0, 1, 2, 3, 4]
        random.shuffle(sitList)
        # print(sitList)

        lineUpList = []

        teamAgainst = 1
        i = 0
        while teamAgainst <= 6:
            playList = [0, 1, 2, 3, 4]
            if self.teamNum != teamAgainst:
                # set up a lineup
                sitNum = sitList[i]
                sit = self.playerList[sitNum]
                playList.remove(sitList[i])
                pair1List = random.sample(playList, 2)
                playList.remove(pair1List[0])
                playList.remove(pair1List[1])
                pair2List = playList
                pair1 = Pair(self.playerList[pair1List[0]], self.playerList[pair1List[1]])
                pair2 = Pair(self.playerList[pair2List[0]], self.playerList[pair2List[1]])
                lineUp = TeamLineup(self.teamNum, teamAgainst, pair1, pair2, sit)
                lineUpList.append(lineUp)
                i += 1
            teamAgainst += 1
        return lineUpList


# teams with their players
team1List = [
    Player('Drew Nguyen', 'M', 10, 1),
    Player('Hong Jiang', 'M', 8, 1),
    Player('Ling Zhang', 'M', 7, 1),
    Player('Adwin Ko', 'M', 5, 1),
    Player('Ke Lin', 'F', 3, 1)
]

team2List = [
    Player('Bin Liang', 'M', 8, 2),
    Player('Jianguo Jin', 'M', 6, 2),
    Player('Bruce Qian', 'M', 5, 2),
    Player('Liang Zhao', 'M', 6, 2),
    Player('Jocelyn Li', 'F', 3, 2)
]

team3List = [
    Player('Mark Feng', 'M', 8, 3),
    Player('Jackson Dam', 'M', 7, 3),
    Player('William Kwan', 'M', 6, 3),
    Player('Benjamin Di', 'M', 7, 3),
    Player('Paige Cai', 'F', 4, 3)
]

team4List = [
    Player('Richard Foo', 'M', 9, 4),
    Player('Gary Guangwu Liu', 'M', 7, 4),
    Player('Shawn Chen', 'M', 6, 4),
    Player('Grace Hao', 'F', 4, 4),
    Player('Maria Wang', 'F', 4, 4)
]

team5List = [
    Player('Jesse Chen', 'M', 8, 5),
    Player('Kevin Mah', 'M', 7, 5),
    Player('Stephen Hu', 'M', 6, 5),
    Player('Min Li', 'F', 4, 5),
    Player('Rachel Lee', 'F', 4, 5)
]

team6List = [
    Player('Francis Chen', 'M', 10, 6),
    Player('Anton Ko', 'M', 7, 6),
    Player('John Xinghua Liu', 'M', 7, 6),
    Player('Tinnie Le', 'F', 3, 6),
    Player('Yinghua', 'F', 3, 6)
]


def main():
    random.seed(datetime.now())
    i = 1
    team5win = []
    while i < 1000:
        team1 = Team(1, team1List)
        team2 = Team(2, team2List)
        team3 = Team(3, team3List)
        team4 = Team(4, team4List)
        team5 = Team(5, team5List)
        team6 = Team(6, team6List)

        teams = [team1, team2, team3, team4, team5, team6]

        oneWin = tornament(teams)
        team5win.append(oneWin)
        i += 1


def tornament(teams):
    # entire tornament, setup team against team
    # round robin
    # T1 v T2, T1 v T3, T1 v T4  etc
    # record result

    t = [0, 1, 2, 3, 4, 5]
    winCount = [0, 0, 0, 0, 0, 0]

    for i in t:
        if i == 5:
            break
        j = i + 1
        while j <= 5:
            # print("i, j", i, j)
            # match between team i and team j
            # update score

            wins = games(teams[i], teams[j])
            winCount[i] += wins[0]
            winCount[j] += wins[1]
            j += 1
    print(winCount)
    if winCount[4] == max(winCount) and max(winCount) >= 11:
        return teams[4].display()


def games(team1, team2):
    t1win = 0
    t2win = 0
    # lineups

    l1 = [2, 3, 4, 5, 6]
    l2 = [1, 3, 4, 5, 6]
    l3 = [1, 2, 4, 5, 6]
    l4 = [1, 2, 3, 5, 6]
    l5 = [1, 2, 3, 4, 6]
    l6 = [1, 2, 3, 4, 5]

    lineList = [l1, l2, l3, l4, l5, l6]

    # for scoring specific game between two teams
    t1 = team1.teamNum
    t2 = team2.teamNum

    t1ln = lineList[t1 - 1].index(t2)
    t2ln = lineList[t2 - 1].index(t1)
    # setup pair1 v pair1 for twice

    # score array of score of two teams
    score1 = match(team1.lineUp[t1ln].pair1, team2.lineUp[t2ln].pair1)
    score2 = match(team1.lineUp[t1ln].pair1, team2.lineUp[t2ln].pair1)
    if score1[0] > score1[1] and score2[0] > score2[1]:
        team1.win += 1
        t1win += 1
    if score1[0] < score1[1] and score2[0] < score2[1]:
        team2.win += 1
        t2win += 1
    if (score1[0] > score1[1] and score2[0] < score2[1]) or (score1[0] < score1[1] and score2[0] > score2[1]):
        t1Tot = score1[0] + score2[0]
        t2Tot = score1[1] + score2[1]
        if t1Tot > t2Tot:
            team1.win += 1
            t1win += 1
        else:
            team2.win += 1
            t2win += 1
        if t1Tot == t2Tot:
            [s1, s2] = matchEx(team1.lineUp[t1ln].pair1, team2.lineUp[t2ln].pair1)
            if s1 > s2:
                team1.win += 1
                t1win += 1
            else:
                team2.win += 1
                t2win += 1

    if DEBUG:
        print('team1')
        team1.lineUp[t1ln].pair1.first.display()
        team1.lineUp[t1ln].pair1.second.display()
        print('team2')
        team2.lineUp[t2ln].pair1.first.display()
        team2.lineUp[t2ln].pair1.second.display()
        print("pair1 ", score1, score2)

    # pair2 v pair2 for twice
    score1 = match(team1.lineUp[t1ln].pair2, team2.lineUp[t2ln].pair2)
    score2 = match(team1.lineUp[t1ln].pair2, team2.lineUp[t2ln].pair2)

    if score1[0] > score1[1] and score2[0] > score2[1]:
        team1.win += 1
        t1win += 1
    if score1[0] < score1[1] and score2[0] < score2[1]:
        team2.win += 1
        t2win += 1
    if (score1[0] > score1[1] and score2[0] < score2[1]) or (score1[0] < score1[1] and score2[0] > score2[1]):
        t1Tot = score1[0] + score2[0]
        t2Tot = score1[1] + score2[1]
        if t1Tot > t2Tot:
            team1.win += 1
            t1win += 1
        else:
            team2.win += 1
            t2win += 1
        if t1Tot == t2Tot:
            [s1, s2] = matchEx(team1.lineUp[t1ln].pair2, team2.lineUp[t2ln].pair2)
            if s1 > s2:
                team1.win += 1
                t1win += 1
            else:
                team2.win += 1
                t2win += 1

    if DEBUG:
        print('team1')
        team1.lineUp[t1ln].pair2.first.display()
        team1.lineUp[t1ln].pair2.second.display()
        print('team2')
        team2.lineUp[t2ln].pair2.first.display()
        team2.lineUp[t2ln].pair2.second.display()
        print("pair2 ", score1, score2)
    # updateWinnerScore
    return [t1win, t2win]


def match(pair1, pair2):
    s1 = 0
    s2 = 0

    if pair1.pType == 'MD' and pair2.pType == 'XD':
        s2 = 7
    if pair1.pType == 'XD' and pair2.pType == 'WD':
        s2 = 7
    if pair1.pType == 'MD' and pair2.pType == 'WD':
        s2 = 10
    if pair2.pType == 'MD' and pair1.pType == 'XD':
        s1 = 7
    if pair2.pType == 'XD' and pair1.pType == 'WD':
        s1 = 7
    if pair2.pType == 'MD' and pair1.pType == 'WD':
        s1 = 10

    p1Str = pair1.first.strength + pair1.second.strength
    p2Str = pair2.first.strength + pair2.second.strength
    tStr = p1Str + p2Str
    p1winChance = p1Str / tStr

    while s1 < 21 and s2 < 21:
        pt = playPoint()
        if pt < p1winChance:
            s1 += 1
        else:
            s2 += 1

        if s1 >= 21 or s2 >= 21:
            if abs(s1 - s2) >= 2:
                break
            else:
                while abs(s1 - s2) < 2:
                    if playPoint() < p1winChance:
                        s1 += 1
                    else:
                        s2 += 1
                    if s1 == 30 or s2 == 30:
                        break
                break

    return [s1, s2]


def matchEx(pair1, pair2):
    s1 = 0
    s2 = 0

    p1Str = pair1.first.strength + pair1.second.strength
    p2Str = pair2.first.strength + pair2.second.strength
    tStr = p1Str + p2Str
    p1winChance = p1Str / tStr

    while s1 < 5 and s2 < 5:
        pt = playPoint()
        if pt < p1winChance:
            s1 += 1
        else:
            s2 += 1

    return [s1, s2]


def playPoint():
    random.seed()
    return random.random()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
