from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# 1. World Setup
Sky()
light = DirectionalLight()
light.look_at(Vec3(1,-1,1))

# 2. The Marble (Player)
# We use a sphere and attach a collider to it
player = Entity(model='sphere', color=color.cyan, scale=1, 
                position=(0,2,0), collider='sphere')

# 3. Create a Level (A narrow bridge)
ground = Entity(model='cube', color=color.gray, scale=(5, 1, 50), 
                position=(0,0,20), collider='box', texture='white_cube')

# Floating platforms
platform1 = Entity(model='cube', color=color.orange, scale=(5, 1, 5), 
                   position=(0,2,55), collider='box')
platform2 = Entity(model='cube', color=color.orange, scale=(5, 1, 5), 
                   position=(10,4,65), collider='box')

# 4. Movement Variables
speed = 5
player.velocity = Vec3(0,0,0)

def update():
    # Camera follows the player
    camera.position = player.position + Vec3(0, 5, -15)
    camera.look_at(player)

    # Physics: Gravity
    if not player.intersects(ignore=(player,)).hit:
        player.velocity += Vec3(0, -9.8 * time.dt, 0) # Fall down
    else:
        player.velocity.y = 0 # Stay on ground

    # Control logic
    move_direction = Vec3(
        held_keys['d'] - held_keys['a'],
        0,
        held_keys['w'] - held_keys['s']
    ).normalized()

    player.position += move_direction * speed * time.dt
    player.position += player.velocity * time.dt

    # Fall check
    if player.y < -10:
        player.position = (0, 5, 0)
        player.velocity = Vec3(0,0,0)

app.run()