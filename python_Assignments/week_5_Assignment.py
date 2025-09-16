# Assignment 1: Design Your Own Class! 🏗️
# Creating a Superhero class with attributes, methods, and inheritance

class Superhero:
    """Base Superhero class with common attributes and methods"""
    
    # Class variable (shared by all instances)
    total_heroes = 0
    
    def __init__(self, name, real_name, power_level, city):
        """Constructor to initialize each superhero with unique values"""
        self.name = name
        self.real_name = real_name
        self.power_level = power_level
        self.city = city
        self.energy = 100
        self.is_active = True
        
        # Increment total heroes count
        Superhero.total_heroes += 1
    
    def introduce(self):
        """Method to introduce the superhero"""
        return f"I am {self.name}! Protector of {self.city}!"
    
    def use_power(self):
        """Generic power usage method"""
        if self.energy >= 20:
            self.energy -= 20
            return f"{self.name} uses their powers! Energy: {self.energy}"
        else:
            return f"{self.name} is too tired to use powers!"
    
    def rest(self):
        """Method to restore energy"""
        self.energy = min(100, self.energy + 30)
        return f"{self.name} rests and recovers energy: {self.energy}"
    
    def get_info(self):
        """Method to display hero information"""
        status = "Active" if self.is_active else "Retired"
        return f"""
╔══════════════════════════════╗
║ Hero: {self.name:<20} ║
║ Real Name: {self.real_name:<15} ║
║ Power Level: {self.power_level:<13} ║
║ City: {self.city:<20} ║
║ Energy: {self.energy:<18} ║
║ Status: {status:<18} ║
╚══════════════════════════════╝"""

# Inheritance Layer: Specialized Superhero Classes

class FlyingHero(Superhero):
    """Flying superhero with aerial abilities"""
    
    def __init__(self, name, real_name, power_level, city, flight_speed):
        super().__init__(name, real_name, power_level, city)
        self.flight_speed = flight_speed
        self.altitude = 0
    
    def fly(self):
        """Flying-specific method"""
        if self.energy >= 15:
            self.energy -= 15
            self.altitude = 1000
            return f"🦅 {self.name} soars into the sky at {self.flight_speed} mph!"
        else:
            return f"{self.name} is too tired to fly!"
    
    def land(self):
        """Landing method"""
        self.altitude = 0
        return f"🛬 {self.name} lands gracefully on the ground."
    
    def use_power(self):
        """Override parent method with flying-specific power"""
        if self.energy >= 20:
            self.energy -= 20
            return f"⚡ {self.name} unleashes aerial lightning strikes from above!"
        else:
            return f"{self.name} is too exhausted for aerial attacks!"

class TechHero(Superhero):
    """Technology-based superhero"""
    
    def __init__(self, name, real_name, power_level, city, tech_level):
        super().__init__(name, real_name, power_level, city)
        self.tech_level = tech_level
        self.gadgets = []
    
    def add_gadget(self, gadget):
        """Add a new gadget to inventory"""
        self.gadgets.append(gadget)
        return f"🔧 {self.name} adds {gadget} to their arsenal!"
    
    def use_power(self):
        """Override with tech-specific power"""
        if self.energy >= 20:
            self.energy -= 20
            gadget = self.gadgets[0] if self.gadgets else "advanced tech suit"
            return f"🤖 {self.name} activates their {gadget}!"
        else:
            return f"{self.name}'s tech systems are offline - low energy!"

# Assignment 2: Polymorphism Challenge! 🎭
# Creating different classes with the same method name but different implementations

class Vehicle:
    """Base Vehicle class"""
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def move(self):
        """Generic movement method - to be overridden"""
        return f"{self.name} is moving at {self.speed} mph"
    
    def info(self):
        """Display vehicle information"""
        return f"Vehicle: {self.name} | Speed: {self.speed} mph"

class Car(Vehicle):
    """Car class with specific movement"""
    
    def __init__(self, name, speed, fuel_type):
        super().__init__(name, speed)
        self.fuel_type = fuel_type
    
    def move(self):
        """Car-specific movement"""
        return f"🚗 {self.name} is driving on the road at {self.speed} mph"
    
    def honk(self):
        return f"🚨 {self.name} goes BEEP BEEP!"

class Plane(Vehicle):
    """Plane class with flying movement"""
    
    def __init__(self, name, speed, altitude):
        super().__init__(name, speed)
        self.altitude = altitude
    
    def move(self):
        """Plane-specific movement"""
        return f"✈️ {self.name} is flying through the sky at {self.speed} mph at {self.altitude} feet"
    
    def takeoff(self):
        return f"🛫 {self.name} is taking off!"

class Boat(Vehicle):
    """Boat class with water movement"""
    
    def __init__(self, name, speed, water_type):
        super().__init__(name, speed)
        self.water_type = water_type
    
    def move(self):
        """Boat-specific movement"""
        return f"🚢 {self.name} is sailing across the {self.water_type} at {self.speed} mph"
    
    def anchor(self):
        return f"⚓ {self.name} drops anchor!"

class Bicycle(Vehicle):
    """Bicycle class with pedaling movement"""
    
    def __init__(self, name, speed, gear_count):
        super().__init__(name, speed)
        self.gear_count = gear_count
    
    def move(self):
        """Bicycle-specific movement"""
        return f"🚴 {self.name} is pedaling along the path at {self.speed} mph"
    
    def ring_bell(self):
        return f"🔔 {self.name} goes RING RING!"

# Demonstration and Testing
def main():
    print("=" * 60)
    print("🦸 ASSIGNMENT 1: SUPERHERO CLASS DEMONSTRATION")
    print("=" * 60)
    
    # Create different types of superheroes
    hero1 = FlyingHero("Sky Guardian", "Alex Storm", 85, "Metroplex", 300)
    hero2 = TechHero("Cyber Knight", "Jordan Tech", 78, "Neo City", 9)
    hero3 = Superhero("Earth Shaker", "Morgan Stone", 92, "Rock Valley")
    
    # Add gadgets to tech hero
    print(hero2.add_gadget("plasma cannon"))
    print(hero2.add_gadget("force field generator"))
    
    # Demonstrate methods
    heroes = [hero1, hero2, hero3]
    
    for hero in heroes:
        print(hero.introduce())
        print(hero.use_power())
        if isinstance(hero, FlyingHero):
            print(hero.fly())
        print("-" * 40)
    
    print(f"\nTotal Heroes Created: {Superhero.total_heroes}")
    
    print("\n" + "=" * 60)
    print("🚀 ASSIGNMENT 2: POLYMORPHISM DEMONSTRATION")
    print("=" * 60)
    
    # Create different vehicles
    vehicles = [
        Car("Lightning Bolt", 120, "Electric"),
        Plane("Sky Cruiser", 550, 35000),
        Boat("Ocean Explorer", 45, "ocean"),
        Bicycle("Speed Demon", 25, 21)
    ]
    
    # Demonstrate polymorphism - same method name, different behaviors
    print("🎭 Polymorphism in Action - All vehicles 'move' differently:")
    print("-" * 50)
    
    for vehicle in vehicles:
        print(vehicle.move())
        
        # Demonstrate unique methods for each vehicle type
        if isinstance(vehicle, Car):
            print(vehicle.honk())
        elif isinstance(vehicle, Plane):
            print(vehicle.takeoff())
        elif isinstance(vehicle, Boat):
            print(vehicle.anchor())
        elif isinstance(vehicle, Bicycle):
            print(vehicle.ring_bell())
        
        print("-" * 30)
    
    print("\n🎯 Key OOP Concepts Demonstrated:")
    print("✅ Classes and Objects")
    print("✅ Constructors (__init__)")
    print("✅ Inheritance (FlyingHero, TechHero inherit from Superhero)")
    print("✅ Method Overriding (use_power method)")
    print("✅ Polymorphism (move method behaves differently)")
    print("✅ Encapsulation (private-like attributes with methods)")
    print("✅ Class vs Instance variables")

if __name__ == "__main__":
    main()
