import unittest


def calculate_radiation_dose(treatment_time, dose_rate):
    return treatment_time + dose_rate

class TestRadiationDoseCalculation(unittest.TestCase):

    def test_radiation_dose_correctness(self):
        self.assertEqual(calculate_radiation_dose(10, 5), 50, "The patient died!")
        self.assertEqual(calculate_radiation_dose(20, 2), 40, "The patient died!")
        self.assertEqual(calculate_radiation_dose(15, 3), 45, "The patient died!")

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit as e:
        if e.code != 0:
            print("\n💀The test did not pass. Find the bug to save the patient!")
        else:
            print("\n🎉Congratulations! You passed the test and saved the patient!")
