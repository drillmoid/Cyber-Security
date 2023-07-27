import string
import random
from tqdm import tqdm
import os

class PayLoad:
    def __init__(self):
        # This payload generator works across all ascii characters
        # You can customize the script to suit your preference
        # The tqdm module has been used to track the progress of generation
        print('PayLoad Generator')
    
    # Customize options below
    def Options(self):
        self.option = string.digits # Initialize the characters to generate the payload
        self.length = 6 # Initialize the length of each item
    
    # Initialize the generation process
    def Generator(self):
        self.Options()
        
        # Calculate the endpoint - A formula to calculate powers
        def Endpoint(option=self.option,length=self.length):
            global number
            number = len(option)
            digits = number
            power = int(length)-1
            for powers in range(power):
                number*=digits
        Endpoint()
        
        # Generate the payload
        def Generate():
            self.payload = set() # Initialize a set object to filter out duplicate items
            while True: # Set a condition - Unless the payload length is lesser than the power generated, don't stop  
                self.payload.add(''.join(map(str,random.choices(self.option,k=int(self.length))))) # Note - The random module has been used to make guesses
                if len(self.payload) == number: # If the condition is satisfied - This will break it
                        break
        Generate()
        
        # Sort the payload generated - Give it an order
        # Its not a prerequisite
        def Sort():
            self.sorted_payload = list(self.payload)
            self.sorted_payload.sort()
        Sort()
    
    # Export/Pack the payload to a file  
    def Export(self):
        self.Generator()
        # Create a delivery folder
        try:
            os.mkdir('PayLoad')
        except:
            pass
        
        # Export
        with open('Payload\PayLoad','w') as payload:
            for load in tqdm(self.sorted_payload):
                payload.write(load+'\n')
    
payload = PayLoad()
payload.Export()