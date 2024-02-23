import azure_contact
#import sensor_data

azure_contact.azure_setup()

azure_contact.send_message("Connected!")

azure_contact.azure_close()