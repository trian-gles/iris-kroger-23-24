import azure_contact
#import sensor_data

connection = azure_contact.Connection()

connection.send_message("Connected!")

connection.close()