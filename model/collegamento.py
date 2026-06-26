from dataclasses import dataclass
@dataclass
class Collegamento:
    constructorId: str
    driverId: str
    def __hash__(self):
        return hash((self.driverId, self.constructorId))
    def __eq__(self, other):
        return  (self.driverId == other.driverId and
                self.constructorId == other.constructorId)
    def __str__(self):
        return self.driverId + "-" + self.constructorId