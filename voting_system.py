import csv
from collections import defaultdict

"""
Voting system and management classes.

This module contains the `Candidate` and `VoteManager` classes which handle
the voting logic, including managing candidates, votes, and voting records.
"""

class Candidate:
    def __init__(self, name: str):
        self._name = name
        self._votes = 0

    def add_vote(self):
        self._votes += 1

    @property
    def name(self) -> str:
        return self._name

    @property
    def votes(self) -> int:
        return self._votes

class VoteManager:
    def __init__(self):
        self._candidates = {'John': Candidate('John'), 'Jane': Candidate('Jane')}
        self._voted_identifiers = set()
        self._voting_record = defaultdict(list)

    def validate_identifier(self, identifier: str) -> bool:
        return identifier.isdigit() and len(identifier) == 8

    def vote(self, candidate_name: str, voter_id: str) -> bool:
        if not self.validate_identifier(voter_id):
            raise ValueError("Identifier must be an 8-digit number.")
        if voter_id in self._voted_identifiers:
            return False
        candidate = self._candidates.get(candidate_name)
        if candidate:
            candidate.add_vote()
            self._voted_identifiers.add(voter_id)
            self._voting_record[voter_id].append(candidate_name)
            return True
        return False

    def get_candidate_names(self) -> list:
        """Returns a list of all candidate names."""
        return [candidate.name for candidate in self._candidates.values()]

    def save_voting_record_to_csv(self):
        with open('voting_record.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Voter ID', 'Voted For'])
            for voter_id, candidates in self._voting_record.items():
                for candidate in candidates:
                    writer.writerow([voter_id, candidate])

    def get_results(self):
        return {candidate.name: candidate.votes for candidate in self._candidates.values()}
