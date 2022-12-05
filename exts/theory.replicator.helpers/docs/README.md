
# OmniGraph Extension [theory.replicator.helpers]
Extension with Replicator helpers

modify.write_physics_attribute_float write_physics_attribute_float must be used after rep.physics.rigid_body() and used with rep.utils.sequential.
Replicator nodes are not garanteed to run in an order unless rep.utils.sequential is used.
This has been testing in Code 2022.3.0

This code has not been tested with all physics attributes. These attributes have been tested:
1. physxCollision:contactOffset
2. physxCollision:restOffset

## OgnTheoryWritePhysicsAttributeFloat
    Write physics attributes.  To be used after write physics node. Must be a float value
    There is a convience function in theory.replicator.helpers.modify to create this node properly using omni.replicator.core

## Samples
Sample files can be found in the samples folder