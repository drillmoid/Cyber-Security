![](Drill%20Moid.svg)

# CYBER SECURITY (TOOLKIT)
## [1] BruteForce
### PayLoad
This script uses python to generate custom payloads and export them to a file to come in handy during a bruteforce attack. However, it is still in development but and works just fine for someone conversant with python.

The <code>self.option</code> variable controls the items to use for payload generation while the <code>self.length</code> variable controls the length of each payload item.For example, lets say you want to generate all the possible combinations of the letters <code>A,B and C</code> and have each combination to have a length of <code>3</code> characters. This is how and where to edit.
```python
def Options(self):
    self.option = 'ABC' # Accepts a string
    self.length = 6 # Accepts an integer
```

### BruteForcePDF
This script does the "heavy-lifting" when it comes to PDF bruteforce attacks. It accepts the encrypted PDF file <code>mypdf = 'Encrypted.pdf'</code> and the payload. 
```python
def Bruteforce(self):
    mypdf = 'Your Encrypted PDF' # Edit Here
    self.load = []
```
The payload should be administered as follows
```python
# Open the payload file
with open('Your PayLoad File','r') as payload:
# Loop through all keys and start testing
    for load in alive_it(payload,title='Delivering PayLoad - '):
        # Testing
```

>The above tools are still in development. They will inconvenience those who lack the knowledge of <code>python</code>. However, the above procedures and some little knowledge will be just fine.
















