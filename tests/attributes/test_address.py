import unittest

from bin.attributes.Address import Address  # Make sure to import your Address class properly


class TestAddress(unittest.TestCase):
    def setUp(self):
        self.proof = 'ID Card'  # Example proof
        self.address = Address('123 Main St', 'Springfield', 'IL', 'USA', 62701, self.proof)

    def test_initialization(self):
        self.assertEqual(self.address.street, '123 Main St')
        self.assertEqual(self.address.city, 'Springfield')
        self.assertEqual(self.address.state, 'IL')
        self.assertEqual(self.address.country, 'US')
        self.assertEqual(self.address.postal_code, 62701)

    def test_street_property(self):
        new_street = '456 Elm St'
        self.address.street = new_street
        self.assertEqual(self.address.street, new_street)

    def test_city_property(self):
        new_city = 'Chicago'
        self.address.city = new_city
        self.assertEqual(self.address.city, new_city)

    def test_state_property(self):
        new_state = 'NY'
        self.address.state = new_state
        self.assertEqual(self.address.state, new_state)

    def test_country_property(self):
        new_country = 'Canada'
        self.address.country = new_country
        self.assertEqual(self.address.country, new_country)

    def test_postal_code_property(self):
        new_postal_code = 'H0H 0H0'
        self.address.postal_code = new_postal_code
        self.assertEqual(self.address.postal_code, new_postal_code)

    def test_str_representation(self):
        expected_str = '123 Main St, Springfield, IL, US - 62701'
        self.assertEqual(str(self.address), expected_str)


if __name__ == '__main__':
    unittest.main()
