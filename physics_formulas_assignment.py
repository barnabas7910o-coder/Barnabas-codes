#print('a', 'b', 'c', 'd', 'e' formulas)
name=str(input('Enter your name: '))
print('Hey ' + name)

print("Welcome to Barnabas' Calculator :)")
print("Here are my available physics formulas")
print('a.impulse = force * time')
print('b.force = mass * acceleration')
print('c.voltage = current * resistance')
print('d.velocity = displacement / time')
print('e.kinetic_energy = 0.5 * mass * velocity^2')


chosen_formula = input('Which of the above physics formulas would you like to use? ')
if chosen_formula == 'a':
    force = float(input('Enter the force: '))
    print('force, F = ' + str(force) + 'N')
    time = float(input('Enter the time: '))
    print('time, t = ' + str(time) + 's')
    print('impulse = f * t')
    print('the calculated impulse = ' + str(force * time) + 'Ns')

elif chosen_formula == 'b':
    mass = float(input('Enter the mass: '))
    print('mass, m = ' + str(mass) + 'kg')
    acceleration = float(input('Enter the acceleration: '))
    print('acceleration, a = ' + str(acceleration) + 'm/s^2')
    print('F = m * a')
    print('the calculated force = ' + str(mass * acceleration) + 'N')

elif chosen_formula == 'c':
    current = float(input('Enter the current: '))
    print('current, I = ' + str(current) + 'A')
    resistance = float(input('Enter the resistance: '))
    print('resistance, R = ' + str(resistance) + 'ohms')
    print('V = I x R')
    print('the calculated voltage = ' + str(current * resistance) + 'V')

elif chosen_formula == 'd':
    displacement = float(input('Enter the displacement: '))
    print('displacement, d = ' + str(displacement) + 'm')
    time = float(input('Enter the time: '))
    print('time, t = ' + str(time) + 's')
    print('v = d / t')
    print('the calculated velocity = ' + str(displacement / time) + 'm/s')

elif chosen_formula == 'e':
    mass = float(input('Enter the mass: '))
    print('mass, m = ' + str(mass) + 'kg')
    velocity = float(input('Enter the velocity: '))
    print('velocity, v = ' + str(velocity) + 'm/s')
    print('K.E = 0.5 x m x v^2')
    print('the calculated velocity = ' + str(0.5 * mass * velocity*2) + 'J')

else:
    print("Oops! Seems like I don't have this physics formula")


print("Thanks for using Barnabas' calculator")