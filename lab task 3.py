class SmartHeater:
    def __init__(self, desired_temperature):

        self.desired_temperature = desired_temperature

        self.previous_action = None
    def check_temperature(self, current_temperature):
    
        if current_temperature < self.desired_temperature:
            action = "Turn Heater ON"
        else:
            action = "Turn Heater OFF"

        if action == self.previous_action:
            action = "No Change (Keep same state)"
        else:
            self.previous_action = action

        return action
rooms = {
    "Lounge": 20,
    "Guest Room": 22,
    "Kitchen": 25,
    "Bedroom": 19,
    "Bathroom": 22,
}
heater = SmartHeater(22)
for room, temp in rooms.items():
    decision = heater.check_temperature(temp)
    print(f"{room}: {temp}°C -> {decision}")
