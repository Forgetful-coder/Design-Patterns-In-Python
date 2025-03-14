"Abstract Factory Use Case Example Code"
from furniture_factory import FurnitureFactory


FURNITURE = FurnitureFactory.get_furniture("SmallChair")
print(f"{FURNITURE.__class__} : {FURNITURE.get_dimensions()}")

FURNITURE = FurnitureFactory.get_furniture("WoodenTable")
print(f"{FURNITURE.__class__} : {FURNITURE.get_dimensions()}")
