import time
import datetime
import winsound


def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime(
            "%H:%M")  # Get the current time in HH:MM format
        if current_time == alarm_time:  # Check if the current time matches the alarm time
            print("Time to wake up!")
            for i in range(5):
                winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 1 second
            break
        time.sleep(60)  # Check every minute


def main():
    print("Welcome to the Alarm Clock!")
    # Prompt the user to enter the alarm time
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    set_alarm(alarm_time)


if __name__ == "__main__":
    main()
