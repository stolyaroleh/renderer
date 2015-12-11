from math import cos, sin, radians


def from_spherical(r, theta, phi):
    return (r * cos(theta) * sin(phi),
            r * sin(theta) * sin(phi),
            r * cos(phi))


def from_spherical_deg(r, theta, phi):
    return from_spherical(r, radians(theta), radians(phi))
