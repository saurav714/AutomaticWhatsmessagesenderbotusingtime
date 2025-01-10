import pywhatkit
import datetime
import logging

# Configure logging
logging.basicConfig(filename='whatsapp_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

try:
    # Get user input
    phone_number = input("Enter the phone number (with country code, e.g., +911234567890): ")
    message = input("Enter your message: ")
    
    # Get the date input and parse it
    date_input = input("Enter the date in YYYY-MM-DD format: ")
    hour = int(input("Enter the hour (24-hour format): "))
    minute = int(input("Enter the minute: "))
    
    # Parse the date input
    scheduled_date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
    
    # Get the current date and time
    now = datetime.datetime.now()
    
    # Combine date and time for scheduling
    scheduled_time = scheduled_date.replace(hour=hour, minute=minute)
    
    # Check if the scheduled time is in the past
    if scheduled_time < now:
        raise ValueError("Scheduled time is in the past. Please enter a future date and time.")
    
    # Calculate the delay in seconds from now to the scheduled time
    delay_seconds = (scheduled_time - now).total_seconds()
    
    # Convert delay to minutes and seconds
    delay_minutes = delay_seconds // 60
    delay_seconds = delay_seconds % 60
    
    # Schedule the message using pywhatkit
    pywhatkit.sendwhatmsg(phone_number, message, scheduled_time.hour, scheduled_time.minute)
    logging.info(f"Message scheduled to {phone_number} on {scheduled_date.strftime('%Y-%m-%d')} at {hour}:{minute}. Message: {message}")
    print("Message scheduled successfully!")

except ValueError as e:
    print(f"Input Error: {e}")
except pywhatkit.exceptions.InternetException:
    print("No internet connection. Please check your network and try again.")
except Exception as e:
    logging.error(f"An error occurred: {e}")
    print(f"An error occurred: {e}")
