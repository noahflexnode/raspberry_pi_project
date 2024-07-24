def toggle_relay(state):
        state = not state
        if state:
                print("ON")
        else:
                print("OFF")
        return state
