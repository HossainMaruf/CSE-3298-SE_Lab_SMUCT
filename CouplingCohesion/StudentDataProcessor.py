# Separate class for reading student data
class StudentDataReader:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        # Simulated function to read student data from the file
        print(f"Reading student data from {self.filename}")
        # Returning sample data for demonstration
        return [
            {"name": "Alice", "grade": 85},
            {"name": "Bob", "grade": 70},
            {"name": "Charlie", "grade": 92},
            # More student records...
        ]

# Separate class for statistics calculations
class StatisticsCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_statistics(self):
        # Calculating statistics on student data
        average_grade = sum(student["grade"] for student in self.data) / len(self.data)
        highest_grade = max(student["grade"] for student in self.data)
        # You can add more statistics as needed
        return average_grade, highest_grade

    def display_results(self, average_grade, highest_grade):
        # Displaying statistics
        print(f"Average Grade: {average_grade}")
        print(f"Highest Grade: {highest_grade}")

# Data Processor Class
class StudentDataProcessor:
    def __init__(self, filename):
        self.reader = StudentDataReader(filename)
        self.data = None
        self.statistics_calculator = None

    def process_data(self):
        self.data = self.reader.read_data()
        self.statistics_calculator = StatisticsCalculator(self.data)
        average, highest = self.statistics_calculator.calculate_statistics()
        self.statistics_calculator.display_results(average, highest)

if __name__ == "__main__":
  # Using the refactored classes
  data_processor = StudentDataProcessor("student_records.txt")
  data_processor.process_data()

# end main