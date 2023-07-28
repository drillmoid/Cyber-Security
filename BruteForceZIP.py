from zipfile import ZipFile
from alive_progress import alive_it
import os

class BruteForce:
    # This bruteforce script depends on an active\Ready payload 
    # Use a payload generator to make ready your payload or download payloads
    # This bruteforce script works solely on pdf files
    # The alive progress module has been used to track the progress of the bruteforce attack
    
    def __init__(self):
        print('BruteForce ZIP')
 
    def Bruteforce(self):
        myzip = 'test.zip' # Load Encrypted PDF
        self.load = [] # Initialize list to append the keys
        
        # Decrypt the encrypted file
        def Decode():
            # Initialize a delivery folder
            try:
                os.mkdir('Delivery')
            except:
                pass
            with open('PayLoad\PayLoad','r') as payload:
                # Loop through all keys and start testing
                for load in alive_it(payload,title='Delivering PayLoad - '):
                    # Testing
                    try:
                        with ZipFile(myzip) as zf:
                            zf.extractall(pwd=bytes(load[:-1],'utf-8'))
                            self.load.append(load[:-1])
                            break
                    except:
                        pass
                
                # Export the valid key to the delivery folder     
                with open('Delivery\Key.key','w') as payload:
                        for load in alive_it(self.load,title='Delivering Findings - '):
                            payload.write(load+'\n')

        Decode()
        
bruteforce = BruteForce()
bruteforce.Bruteforce()

