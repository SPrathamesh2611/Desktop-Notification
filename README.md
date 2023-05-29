# Desktop-Notification
To install the required module for the provided code (`win10toast`), you can use the following command in the terminal:

```
pip install win10toast
```

This command will use `pip`, the package installer for Python, to download and install the `win10toast` module from the Python Package Index (PyPI). Make sure you have a stable internet connection while running this command. Once the installation is complete, you'll be able to import and use the `win10toast` module in your Python code.

# Description
The provided code demonstrates the usage of the `win10toast` library to display a desktop notification on a Windows 10 system with the current date and time. Here's an introduction to the code:

The code begins by importing two modules: `ToastNotifier` from the `win10toast` library and `datetime`. 

The `win10toast` library allows the Python script to interact with the Windows 10 toast notifications feature, enabling the display of system-level notifications on the desktop.

The `datetime` module provides functionalities for working with dates and times in Python.

Next, the code retrieves the current date and time using `datetime.datetime.now()` and assigns it to the variable `data`. It then converts the `datetime` object to a string representation using `str(data)`.

After that, an instance of `ToastNotifier` is created and assigned to the variable `toast`. This instance represents the toast notification object, which will be used to display the notification on the desktop.

Finally, the `show_toast` method of the `toast` object is called. It takes three arguments: the title of the notification ("Date-Time Update"), the content of the notification (the current date and time stored in the `data` variable), and the duration of the notification in seconds (15 seconds in this case). This method triggers the display of the notification on the Windows 10 desktop.

Overall, this code demonstrates how to use the `win10toast` library to show a desktop notification with the current date and time on a Windows 10 system.
