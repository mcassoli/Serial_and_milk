from datetime import datetime


class Rack:
    def __init__(self):
        '''
        
        '''
        self.bays = {} # Dict
        self.updated = 0 # Time stamp of last update
    
    def update_rack(self, status):
        '''
        
        '''
        self.updated = datetime.now() # set time to now
        
        # Check each bay in the new status stored in status
        for bay, state in status.items():
            
            self.bays[bay] = state
        self.log()
        
        '''# If the bay does not already exist, add it and log the update
            if bay not in self.bays:
                self.bays[bay] = state
                self.log_bay(bay, state)
            
            # If the bay exists and its status has changed, record and log the change
            elif state is not self.bays[bay]:
                self.bays[bay] = state
                self.log_bay(bay, state)'''
    
    def log(self):
        '''
        
        '''

        f = open('rack-log.txt', 'a')
        f.write('\n')
        f.write('{0}\n'.format(self.updated))
        for bay, state in self.bays.items():
            f.write('{0} {1}\n'.format(bay, state))
        f.close()


