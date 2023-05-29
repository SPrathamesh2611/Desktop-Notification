from win10toast import ToastNotifier
import datetime

# Get the current date and time
data = datetime.datetime.now()
data = str(data)

# Create a ToastNotifier instance
toast = ToastNotifier()

# Display the desktop notification
toast.show_toast("Date-Time Update", data, duration=15)
