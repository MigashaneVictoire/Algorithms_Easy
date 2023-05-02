from solution import tournamentWinner
import unittest

class testSolution(unittest.TestCase):
    def test_case_1(self):
        competitions = [
            ["HTML", "C#"],
            ["C#", "Python"],
            ["Python", "HTML"]
            ]
        results = [0, 0, 1]

        expected = "Python"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        competitions = [
            ["HTML", "Java"],
            ["Java", "Python"],
            ["Python", "HTML"]
            ]
        results = [0, 1, 1]

        expected = "Java"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(expected, actual)

    def test_case_3(self):
        competitions = [
            ["HTML", "Java"],
        ["Java", "Python"],
        ["Python", "HTML"],
        ["C#", "Python"],
        ["Java", "C#"],
        ["C#", "HTML"]
        ]
        results = [0, 1, 1, 1, 0, 1]

        expected = "C#"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(expected, actual)

    def test_case_4(self):
        competitions = [
            ["HTML", "Java"],
            ["Java", "Python"],
            ["Python", "HTML"],
            ["C#", "Python"],
            ["Java", "C#"],
            ["C#", "HTML"],
            ["SQL", "C#"],
            ["HTML", "SQL"],
            ["SQL", "Python"],
            ["SQL", "Java"]
            ]
        results = [0, 1, 1, 1, 0, 1, 0, 1, 1, 0]

        expected = "C#"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(expected, actual)

    def test_case_5(self):
        competitions = [
            ["Bulls", "Eagles"]
            ]
        results = [1]

        expected = "Bulls"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(expected, actual)

    def test_case_6(self):
        competitions = [
            ["Bulls", "Eagles"],
            ["Bulls", "Bears"],
            ["Bears", "Eagles"]
            ]
        results = [0, 0, 0]

        expected = "Eagles"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(expected, actual)

    def test_case_7(self):
        competitions = [
            ["Bulls", "Eagles"],
            ["Bulls", "Bears"],
            ["Bulls", "Monkeys"],
            ["Eagles", "Bears"],
            ["Eagles", "Monkeys"],
            ["Bears", "Monkeys"]
            ]
        results = [1, 1, 1, 1, 1, 1]

        expected = "Bulls"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(expected, actual)

    def test_case_8(self):
        competitions = [
            ["AlgoMasters", "FrontPage Freebirds"],
            ["Runtime Terror", "Static Startup"],
            ["WeC#", "Hypertext Assassins"],
            ["AlgoMasters", "WeC#"],
            ["Static Startup", "Hypertext Assassins"],
            ["Runtime Terror", "FrontPage Freebirds"],
            ["AlgoMasters", "Runtime Terror"],
            ["Hypertext Assassins", "FrontPage Freebirds"],
            ["Static Startup", "WeC#"],
            ["AlgoMasters", "Static Startup"],
            ["FrontPage Freebirds", "WeC#"],
            ["Hypertext Assassins", "Runtime Terror"],
            ["AlgoMasters", "Hypertext Assassins"],
            ["WeC#", "Runtime Terror"],
            ["FrontPage Freebirds", "Static Startup"]
            ]
        results = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]

        expected = "AlgoMasters"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(expected, actual)

    def test_case_9(self):
        competitions = [
            ["HTML", "Java"],
            ["Java", "Python"],
            ["Python", "HTML"],
            ["C#", "Python"],
            ["Java", "C#"],
            ["C#", "HTML"],
            ["SQL", "C#"],
            ["HTML", "SQL"],
            ["SQL", "Python"],
            ["SQL", "Java"]
            ]
        results = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1]

        expected = "SQL"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(expected, actual)

    def test_case_10(self):
        competitions = [
            ["A", "B"]
            ]
        results = [0, 0, 1]

        expected = "B"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()