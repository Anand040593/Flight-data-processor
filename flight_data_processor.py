from typing import List, Dict, Optional

class FlightDataProcessor:
    def __init__(self):
        self.flights: List[Dict] = []

    def add_flight(self, data: Dict) -> None:
        """Adds a new flight to the list, ensuring no duplicates by flight number."""
        if not any(flight["flight_number"] == data["flight_number"] for flight in self.flights):
            self.flights.append(data)

    def remove_flight(self, flight_number: str) -> None:
        """Removes a flight based on the flight number."""
        self.flights = [flight for flight in self.flights if flight["flight_number"] != flight_number]

    def flights_by_status(self, status: str) -> List[Dict]:
        """Returns all flights with a given status."""
        return [flight for flight in self.flights if flight["status"] == status]

    def get_longest_flight(self) -> Optional[Dict]:
        """Returns the flight with the longest duration in minutes."""
        if not self.flights:
            return None
        return max(self.flights, key=lambda flight: flight["duration_minutes"])

    def update_flight_status(self, flight_number: str, new_status: str) -> None:
        """Updates the status of a flight and ensures it reflects in the overall data."""
        for flight in self.flights:
            if flight["flight_number"] == flight_number:
                flight["status"] = new_status
                break
