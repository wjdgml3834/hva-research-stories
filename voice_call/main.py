import unittest

def start_voice_chat(user_permission):
    if not user_permission:
        return "Starting voice chat."    
    else:
        return "User permission denied. Cannot start voice chat."
        

class TestVoiceChat(unittest.TestCase):

    def test_voice_chat_starts_with_permission(self):
        self.assertEqual(start_voice_chat(True), "Starting voice chat.")

    def test_voice_chat_denied_without_permission(self):
        self.assertEqual(start_voice_chat(False), "User permission denied. Cannot start voice chat.")

def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestVoiceChat('test_voice_chat_starts_with_permission'))
    test_suite.addTest(TestVoiceChat('test_voice_chat_denied_without_permission'))
    runner = unittest.TextTestRunner()
    
    result = runner.run(test_suite)
    if result.wasSuccessful():
        print("🎉Bug is fixed.")
    else:
        print("💀Privacy has been breached.")

if __name__ == '__main__':
    run_tests()
