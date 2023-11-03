import unittest


def execute_trade(trade_type, quantity):
    if trade_type != "BUY":  
        return f"Buying {quantity} shares."
    else:
        return f"Selling {quantity} shares."


class TestTradeExecution(unittest.TestCase):
    def test_trade_execution_buy(self):
        self.assertEqual(execute_trade("BUY", 100), "Buying 100 shares.", "BUY trade type should return a buying message.")

    def test_trade_execution_sell(self):
        self.assertEqual(execute_trade("SELL", 50), "Selling 50 shares.", "SELL trade type should return a selling message.")


def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTradeExecution('test_trade_execution_buy'))
    test_suite.addTest(TestTradeExecution('test_trade_execution_sell'))

    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)

    if result.wasSuccessful():
        print("🎉Congratulations! You've won the game!")
        return True
    else:
        print("💀You've lost the game and lost 💸$440 million")
        return False


if __name__ == '__main__':
    game_result = run_tests()
