from gl import Raytracer, V3
from obj import *
from figures import *

# Dimensiones
width = 512
height = 512

# Materiales
wood = Material(diffuse = (0.6,0.2,0.2), spec = 64)
stone = Material(diffuse = (0.4,0.4,0.4), spec = 64)
gold = Material(diffuse = (0.9, 0.85, 0.2), spec = 128, matType = REFLECTIVE)
water = Material(spec = 64, ior = 1.33, matType = TRANSPARENT)
glass = Material(spec = 64, ior = 1.5, matType = TRANSPARENT)
diamond = Material(spec = 64, ior = 2.417, matType = TRANSPARENT)

wall = Material(diffuse = (1, 0.76, 0.79 ),spec = 64)
piso = Material(texture = Texture('piso.bmp'))

# Inicializacion
rtx = Raytracer(width,height)
rtx.envmap = EnvMap('envmap1.bmp')

# Luces
rtx.ambLight = AmbientLight(strength = 0.1)
rtx.dirLight = DirectionalLight(direction = V3(1, -1, -2), intensity = 0.5)
rtx.pointLights.append( PointLight(position = V3(0, 2, 0), intensity = 0.5))

# Objetos

rtx.scene.append( Plane(position = V3(0,0,-200), normal = V3(0,0,1), material = wall) )
rtx.scene.append( Plane(position = V3(0,-10,0), normal = V3(0,1,0), material = piso) )
rtx.scene.append( Plane(position = V3(0,30,0), normal = V3(0,1,0), material = piso) )
rtx.scene.append( Plane(position =V3(-40,0,0), normal = V3(1,0,0), material = wall) )
rtx.scene.append( Plane(position =V3(40,0,0), normal = V3(1,0,0), material = wall) )
rtx.scene.append( AABB(position = V3(-3,-3,-10), size = V3(2,2,2), material = gold) )
rtx.scene.append( AABB(position = V3(3,2,-10), size = V3(2,2,2), material = diamond) )



# Terminar
rtx.glRender()
rtx.glFinish('output.bmp')



