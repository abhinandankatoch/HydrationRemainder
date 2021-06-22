import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Have A Cup Of Water - Stay Healthy!",
            message = "Adequate daily fluid intake is about 15.5 cups of fluids a day for men and about 11.5 cups of fluids a day for women.",
            app_icon = ".\\icon.ico",
            timeout = 12
        )

        time.sleep(60*60)
