import omni.replicator.core as rep

import theory.replicator.helpers as helpers

with rep.new_layer():
    cube = rep.create.cube(scale=0.01, position=(0, 0 , 2))
    with cube:
        with rep.utils.sequential():
            rep.physics.rigid_body()
            helpers.modify.write_physics_attribute_float("physxCollision:contactOffset", 0.02)
            helpers.modify.write_physics_attribute_float("physxCollision:restOffset", 0.01)
