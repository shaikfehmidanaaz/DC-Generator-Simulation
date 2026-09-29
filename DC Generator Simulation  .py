# DC Generator Simulation
# Simple simulation of generated EMF, current and power

class DCGenerator:

    def __init__(self, flux, conductors, speed, parallel_paths):
        self.flux = flux
        self.conductors = conductors
        self.speed = speed
        self.parallel_paths = parallel_paths

    def calculate_emf(self):
        # EMF equation:
        # Eg = (P * Phi * Z * N) / (60 * A)
        # Here P is assumed as 4 poles
        poles = 4

        emf = (poles * self.flux * self.conductors *
               self.speed) / (60 * self.parallel_paths)

        return emf

    def calculate_power(self, emf, current):
        return emf * current

    def display(self, current):
        emf = self.calculate_emf()
        power = self.calculate_power(emf, current)

        print("\n===== DC GENERATOR SIMULATION =====")
        print(f"Flux (Wb)           : {self.flux}")
        print(f"Armature Conductors : {self.conductors}")
        print(f"Speed (RPM)         : {self.speed}")
        print(f"Parallel Paths      : {self.parallel_paths}")

        print("\nGenerated EMF       : {:.2f} V".format(emf))
        print("Armature Current    : {:.2f} A".format(current))
        print("Generated Power     : {:.2f} W".format(power))

        if emf > 0:
            print("Generator Status    : RUNNING")
        else:
            print("Generator Status    : OFF")


# Main program
print("===== DC GENERATOR SIMULATION =====")

flux = float(input("Enter flux per pole (Wb): "))
conductors = int(input("Enter number of armature conductors: "))
speed = float(input("Enter speed (RPM): "))
parallel_paths = int(input("Enter number of parallel paths: "))
current = float(input("Enter armature current (A): "))

if flux <= 0 or conductors <= 0 or speed < 0 or parallel_paths <= 0 or current < 0:
    print("\nInvalid input values!")
else:
    generator = DCGenerator(
        flux,
        conductors,
        speed,
        parallel_paths
    )

    generator.display(current)
