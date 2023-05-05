import unittest
from interface.adapters.repository import QualityAssuranceRepository


class TestQualityAssurance(unittest.TestCase):

    def setUp(self):
        self.repo = QualityAssuranceRepository()

    def test_add_quality_assurance(self):
        # Test adding a new quality assurance record
        qa_data = {"product_name": "Product A",
                   "pass_fail": "Pass", "defects": "None"}
        result = self.repo.add_inspection(qa_data)
        self.assertTrue(result)
        self.assertEqual(self.repo.count(), 1)

    def test_get_all_quality_assurance(self):
        # Test retrieving all quality assurance records
        self.repo.add_inspection(
            {"product_name": "Product A", "pass_fail": "Pass", "defects": "None"})
        self.repo.add_inspection(
            {"product_name": "Product B", "pass_fail": "Fail", "defects": "Scratches"})
        self.repo.add_inspection(
            {"product_name": "Product C", "pass_fail": "Pass", "defects": "None"})
        records = self.repo.get_inspections()
        self.assertEqual(len(records), 3)

    def test_get_quality_assurance_by_product_name(self):
        # Test retrieving quality assurance records by product name
        self.repo.add_inspection(
            {"product_name": "Product A", "pass_fail": "Pass", "defects": "None"})
        self.repo.add_inspection(
            {"product_name": "Product B", "pass_fail": "Fail", "defects": "Scratches"})
        self.repo.add_inspection(
            {"product_name": "Product C", "pass_fail": "Pass", "defects": "None"})
        records = self.repo.get_inspections_for_product("Product A")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["product_name"], "Product A")
        self.assertEqual(records[0]["pass_fail"], "Pass")
        self.assertEqual(records[0]["defects"], "None")


if __name__ == '__main__':
    unittest.main()
