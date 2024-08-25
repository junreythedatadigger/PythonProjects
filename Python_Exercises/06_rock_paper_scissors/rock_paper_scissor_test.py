import unittest
from rock_paper_scissor import RockPaperScissorGame


class TestRockPaperScissor(unittest.TestCase):
    def test_case_01(self):
        self.rpsgame = RockPaperScissorGame('r', 'r')
        self.assertEqual(self.rpsgame.declare_winner(), "You both selected rock!")

    def test_case_02(self):
        self.rpsgame = RockPaperScissorGame('r', 't')
        self.assertEqual(self.rpsgame.declare_winner(), "You entered an invalid choice!")

    def test_case_03(self):
        self.rpsgame = RockPaperScissorGame('r', 's')
        self.assertEqual(self.rpsgame.declare_winner(), "Computer wins!")

    def test_case_04(self):
        self.rpsgame = RockPaperScissorGame('r', 'p')
        self.assertEqual(self.rpsgame.declare_winner(), "You win!")

    def test_case_05(self):
        self.rpsgame = RockPaperScissorGame('p', 'p')
        self.assertEqual(self.rpsgame.declare_winner(), "You both selected paper!")

    def test_case_06(self):
        self.rpsgame = RockPaperScissorGame('p', 'r')
        self.assertEqual(self.rpsgame.declare_winner(), "Computer wins!")

    def test_case_07(self):
        self.rpsgame = RockPaperScissorGame('p', 's')
        self.assertEqual(self.rpsgame.declare_winner(), "You win!")

    def test_case_08(self):
        self.rpsgame = RockPaperScissorGame('p', 'u')
        self.assertEqual(self.rpsgame.declare_winner(), "You entered an invalid choice!")

    def test_case_09(self):
        self.rpsgame = RockPaperScissorGame('s', 'r')
        self.assertEqual(self.rpsgame.declare_winner(), "You win!")

    def test_case_10(self):
        self.rpsgame = RockPaperScissorGame('s', 'p')
        self.assertEqual(self.rpsgame.declare_winner(), "Computer wins!")

    def test_case_11(self):
        self.rpsgame = RockPaperScissorGame('s', 's')
        self.assertEqual(self.rpsgame.declare_winner(), "You both selected scissors!")

    def test_case_12(self):
        self.rpsgame = RockPaperScissorGame('s', 'a')
        self.assertEqual(self.rpsgame.declare_winner(), "You entered an invalid choice!")


if __name__ == "__main__":
    unittest.main()
