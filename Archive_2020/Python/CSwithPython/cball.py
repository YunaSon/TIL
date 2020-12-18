from class_Projectile import Projectile

def getInputs():
    angle = float(input("Enter the launch angle (in degree): "))
    vel = float(input("Enter the initial velocity (in m/s): "))
    h0 = float(input("Enter the initial height (in meters): "))
    time = float(input("Enter the time interval between position calculations: "))

    return angle, vel, h0, time

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))

if __name__ == "__main__":
    main()