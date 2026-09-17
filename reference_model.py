import math
import numpy as np

MASS=0.525
I=np.array([[4.9138e-4,0,-5.1552e-4],[0,4.5830e-3,0],[-5.1552e-4,0,4.5126e-3]])

def gyro_acceleration(p):
    omega=np.array([p,0.,0.])
    return np.linalg.solve(I,-np.cross(omega,I@omega))[1]

if __name__=="__main__":
    for p in [100,150,200,300,400,500]:
        print(f"p={p:3d} rad/s  gyro qdot={gyro_acceleration(p): .6f} rad/s^2")
