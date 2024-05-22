Documentation
Python Code:

    __init__ Method: Initializes the main window, sets default study and break times, initializes serial communication with Arduino, and creates the GUI widgets.
    create_widgets Method: Creates and positions all the GUI components including labels, entries, buttons, and a meter.
    start_timer Method: Starts the timer, disables the start button, enables the stop button, initializes timer variables, sends the start signal to Arduino, and updates the timer.
    stop_timer Method: Stops the timer, enables the start button, disables the stop button, and sends the stop signal to Arduino.
    update_timer Method: Updates the timer display and meter, decrements the timer, and switches between study and break sessions, sending appropriate signals to Arduino.

Arduino Sketch:

    Pin Setup: Initializes pins 10 and 12 as output for the LEDs.
    Serial Setup: Begins serial communication at 9600 bps.
    Loop: Continuously checks for incoming serial data and updates the LEDs based on received commands ('S' for study, 'E' for break).

Setting Up the Breadboard

    LEDs:
        Connect the anode (long leg) of the first LED to digital pin 10 via a 220-ohm resistor.
        Connect the anode (long leg) of the second LED to digital pin 12 via a 220-ohm resistor.
        Connect the cathodes (short legs) of both LEDs to the GND rail on the breadboard.
    Power: Ensure the breadboard is powered by connecting the 5V and GND pins from the Arduino to the breadboard power rails.

Testing and Running

    Upload the Arduino Sketch: Open the Arduino IDE, paste the Arduino code, select the correct board and port, and upload the sketch.
    Run the Python Script: Ensure all required Python packages are installed (ttkbootstrap, PIL, pySerial). Run the script to start the Pomodoro Timer.
    Observe the LEDs: The LEDs should turn on and off according to the timer status, indicating study and break sessions.

This setup integrates software and hardware to create a functional Pomodoro Timer with visual indicators using LEDs, providing a helpful tool for managing study sessions.
