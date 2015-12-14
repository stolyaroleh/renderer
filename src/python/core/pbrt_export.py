from pbrt import *
from subprocess import call

def render(filename, dimensions, meshes, camera_pos, light_intensity):
    Init()
    LookAt(camera_pos[0], camera_pos[1], camera_pos[2],
           0, 0, 0,
           0, 1, 0)
    p = ParamSet()
    p.AddFloat('fov', [50.0])
    Camera('perspective', p)

    p = ParamSet()
    p.AddFloat('xwidth', [2])
    p.AddFloat('ywidth', [2])
    PixelFilter('mitchell', p)

    p = ParamSet()
    p.AddString('filename', [filename + '.exr'])
    p.AddInt('xresolution', [dimensions[0]])
    p.AddInt('yresolution', [dimensions[1]])
    Film('image', p)

    WorldBegin()

    AttributeBegin()
    CoordSysTransform('world')
    p = ParamSet()
    p.AddRGBSpectrum('L', [float(light_intensity),
                           float(light_intensity),
                           float(light_intensity)])
    p.AddInt('nsamples', [256])
    p.AddString('mapname', ['skylight-sunset.exr'])
    LightSource('infinite', p)
    AttributeEnd()

    AttributeBegin()
    p = ParamSet()
    CoordSysTransform('world')
    p.AddRGBSpectrum('Kd', [0.8, 0.5, 0.6])
    Material('matte', p)

    for mesh in meshes.values():
        p = ParamSet()
        p.AddPoint3f('P', list(mesh.v))
        p.AddInt('indices', list(mesh.vi))
        Shape('trianglemesh', p)

    AttributeEnd()
    WorldEnd()

    flush_STDOUT()
    Cleanup()

    call(['hdrtoldr.exe', filename + '.exr', filename + '.png'])