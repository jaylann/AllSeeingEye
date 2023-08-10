from bin.entities.Person import Person
from bin.attributes.DOB import DOB
from bin.objects.Proof import Proof

if __name__ == "__main__":
    pers = Person(dob=DOB("23.08.2005", Proof("Test Text")))
    print(pers.age)