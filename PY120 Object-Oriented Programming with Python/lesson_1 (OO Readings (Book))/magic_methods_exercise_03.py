class Candidate:

    def __init__(self, name):
        self._name = name
        self._votes = 0

    def __iadd__(self, vote):
        if not isinstance(vote, int):
            return NotImplemented

        self._votes += vote
        return self

class Election:

    def __init__(self, candidates):
        self.candidates = candidates

    def results(self):
        max_votes = 0
        winner = None
        vote_count = 0

        for candidate in candidates:
            vote_count += candidate._votes 
            if candidate._votes > max_votes:
                winner = candidate._name
                max_votes = candidate._votes

        for candidate in candidates:
            print(f'{candidate._name}: {candidate._votes} votes')

        percent = 100 * (max_votes / vote_count)
        print()    
        print(f'{winner} won: {percent}% of votes')
        
mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()