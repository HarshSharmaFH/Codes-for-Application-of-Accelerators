#Write a python class for a particle, don't forget the init, by giving Z and A. this class
#should have a method which gives the number of neutron back. Instantiate this class with an example.
class particle:
    def __init__(data,z,a):
        data.z=z
        data.a=a
        data.n=data.a-data.z
    def __str__(data):
        return f"Atomic Mass = {data.a}\nAtomic number = {data.z}\nNeutron Number = {data.n}"
z=int(input("Enter the number of atomic number = "))
a=int(input("Enter the number of atomic mass = "))        
x_1=particle(z,a)
print(x_1)
