class Medicine:
    def __init__(self, name, time, dosage, date=None):
        self.name = name
        self.time = time
        self.dosage = dosage
        self.date = date  # Format: YYYY-MM-DD

    def __str__(self):
        return f"{self.name} at {self.time} – {self.dosage} – {self.date}"
