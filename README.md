# desktop_notify


**Libraries:**

* `notifypy` : Used for sending desktop notifications with icons, sounds, and messages.
* `time` : Used for pausing the program execution for a certain duration.
* `datetime` : Used for getting the current time and formatting it.

**Functionality:**

1. **Resource paths**: Defines paths to icons, sound effects, and notification messages for different tasks like drinking water, studying, etc., in a dictionary named `dic`.
2. **Alarm**: Sets an alarm time list called `alram_time`.
3. **Tasks**: Defines a list named `works` that contains tasks to be reminded of in a repeating cycle.
4. **Time restrictions**: Sets time intervals for restricting notifications during sleep/rest periods (`start_am`, `end_am`, `start_pm`, `end_pm`).
5. **Notification configuration**: Initializes the `Notify` library with default notification settings like title, application name, icon, and sound.
6. **Functions**:
    * `get_cur_time()`: Returns the current time in a formatted string (e.g., "09:13 PM").
    * `play_sound()`: Plays the alarm sound notification from the `dic` dictionary.
    * `is_alarm_time(time_now)`: Checks if the current time (`time_now`) matches any of the alarm times in the `alram_time` list.
    * `get_am_pm()`: Returns a list containing the current hour and AM/PM indicator.
    * `notify_me(hour_gap=5)`: This is the main function that runs continuously. It does the following:
        * Checks for alarm time and plays the alarm sound if it matches.
        * Selects a task from the `works` list based on a counter.
        * Retrieves notification details (icon, sound, message) for the selected task from the `dic` dictionary.
        * Checks if the current time falls within the restricted notification period. If so, it skips sending the notification and exits the function.
        * Sends the notification using the `Notify` library with the retrieved details.
        * Increments the counter to select the next task in the `works` list for the next notification cycle.
        * Pauses the program execution for a specified time (`lag`) before repeating the process.

**Overall, this program uses desktop notifications with sounds and icons to remind you about various tasks at regular intervals while avoiding notifications during sleep/rest times.**

**Additional Notes:**

* The code uses comments to explain different sections, which is helpful for understanding.
* You can modify the `dic` dictionary to add or remove tasks and customize their notification details.
* The `alram_time` list can be used to set one-time alarms.
* You might need to install the `notifypy` library using `pip install notifypy` before running this code.
