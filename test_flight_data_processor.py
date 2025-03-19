import unittest
from typing import List, Dict
from flight_data_processor import FlightDataProcessor

class TestFlightDataProcessor(unittest.TestCase):

    def setUp(self) -> None:
        """Set up a FlightDataProcessor instance and sample data."""
        self.processor = FlightDataProcessor()
        self.sample_flights: List[Dict] = [
            {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30", 
             "arrival_time": "2025-02-20 03:45", "duration_minutes": 735, 
             "status": "ON_TIME"},
            {"flight_number": "AZ002", "departure_time": "2025-02-21 11:00", 
             "arrival_time": "2025-02-21 16:00", "duration_minutes": 300, 
             "status": "DELAYED"}
        ]
        for flight in self.sample_flights:
            self.processor.add_flight(flight)

    def test_add_flight(self):
        """Test adding flights, ensuring no duplicates."""
        self.processor.add_flight({"flight_number": "AZ001", "status": "CANCELLED"})
        self.assertEqual(len(self.processor.flights), 2)  # Should not add duplicate
        
        new_flight = {"flight_number": "AZ003", "departure_time": "2025-02-22 09:00", 
                      "arrival_time": "2025-02-22 12:00", "duration_minutes": 180, 
                      "status": "ON_TIME"}
        self.processor.add_flight(new_flight)
        self.assertEqual(len(self.processor.flights), 3)
        self.assertIn(new_flight, self.processor.flights)

    def test_remove_flight(self):
        """Test removing flights by flight number."""
        self.processor.remove_flight("AZ001")
        self.assertEqual(len(self.processor.flights), 1)
        self.assertFalse(any(flight["flight_number"] == "AZ001" for flight in self.processor.flights))

    def test_flights_by_status(self):
        """Test filtering flights by status."""
        delayed_flights = self.processor.flights_by_status("DELAYED")
        self.assertEqual(len(delayed_flights), 1)
        self.assertEqual(delayed_flights[0]["flight_number"], "AZ002")

    def test_get_longest_flight(self):
        """Test retrieving the flight with the longest duration."""
        longest_flight = self.processor.get_longest_flight()
        self.assertIsNotNone(longest_flight)
        self.assertEqual(longest_flight["flight_number"], "AZ001")

        self.processor.remove_flight("AZ001")
        self.assertEqual(self.processor.get_longest_flight()["flight_number"], "AZ002")

    def test_update_flight_status(self):
        """Test updating flight status."""
        self.processor.update_flight_status("AZ001", "CANCELLED")
        updated_flight = next(flight for flight in self.processor.flights if flight["flight_number"] == "AZ001")
        self.assertEqual(updated_flight["status"], "CANCELLED")

if __name__ == "__main__":
    unittest.main()
