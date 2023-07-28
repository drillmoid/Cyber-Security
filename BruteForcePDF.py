import fitz
from alive_progress import alive_it
import os

class BruteForce:
    # This bruteforce script depends on an active\Ready payload 
    # Use a payload generator to make ready your payload or download payloads
    # This bruteforce script works solely on pdf files
    # The alive progress module has been used to track the progress of the bruteforce attack
    
    def __init__(self):
        print('BruteForce PDF')
 
    def Bruteforce(self):
        mypdf = 'Encrypted.pdf' # Load Encrypted PDF
        self.load = [] # Initialize list to append the keys
        
        # Check whether the loaded PDF document is encrypted
        def Check(pdf):
            epdf = fitz.Document(pdf)
            return epdf.isEncrypted
        Check(mypdf)
        
        # Decrypt the encrypted file
        def Decode(file):
            # Initialize a delivery folder
            try:
                os.mkdir('Delivery')
            except:
                pass
            
            # Initialize bruteforce
            if Check(file):
                pdf = fitz.open(file) 

                # Open the payload file
                with open('PayLoad','r') as payload:
                    # Loop through all keys and start testing
                    for load in alive_it(payload,title='Delivering PayLoad - '):
                        # Testing
                        try:
                            if pdf.authenticate(load[:-1]):
                                pdf.save('Delivery\Decrypted.pdf') # Export the decrypted file to the delivery folder
                                self.load.append(load[:-1])
                            else:
                                pass
                        except:
                            pass
                
                # Export the valid key to the delivery folder     
                with open('Delivery\Key.key','w') as payload:
                        for load in alive_it(self.load,title='Delivering Findings - '):
                            payload.write(load+'\n')

        Decode(mypdf)
        
bruteforce = BruteForce()
bruteforce.Bruteforce()
