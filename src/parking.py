from .errors import SizeError, SlotError, CarError, FileError

class parking(object):
    def __init__(self):
        self.parking_capacity = 0
        self.slot_status = dict()
        
    def intialize_parking(self, size):
        if int(size) > 0:
            self.parking_capacity = int(size)
        else:
            self.parking_capacity = 0
            raise SizeError('Invalid parking size')
        
    def _available_slots(self):
        slot  = [_slot for _slot in self._slot_status if self._slot_status[_slot] is  None]
        if len(slot)!=0:
            return min(slot)
        return None
    def used_slots(self):
        return {i: self.slot_status[i] for i in self.slot_status if self.slot_status[i] is not None}
       
    def add_car(self,car_object):
        if car_object.get_registration_number and car_object.get_color:
            slot_available = self._available_slots()
            if slot_available is not None:
                self.slot_status.update{slot_available:car_object}
                return "{}".format(slot_available)
            raise SlotError('Sorry, Parking lot is full.')
        raise CarError('invalid car details')
    
    def remove_car(self,slot_number):
        if slot_number in  self.slot_status.keys():
            if self.slot_status[slot_number] is not None:
                self.slot_status[slot_number] = None
                return True
            else:
                raise SlotError('Slot is already empty')
        else:
            raise SlotError('Invalid slot number')
        
    def get_status(self):
        return self.slot_status
    
    
                
         