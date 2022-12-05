from typing import Union, List

import omni.replicator.core as rep
import omni.graph.core as og


@rep.utils.ReplicatorWrapper
def write_physics_attribute_float(
    name: str,
    value_float: float,
    input_prims: Union[rep.utils.ReplicatorItem, List[str]] = None,
) -> og.Node:
    """Modify the attribute of the prims specified in `input_prims`.
    Attribut must exist.  Only works using a float value.  Must be used with Sequence to ensure that physics attributes have been added.
    There is no checking to see if attribute exists.

    Args:
        name: The name of the attribute to modify.
        value_float: The value to set the attribute to. Must be a float
        input_prims: The prims to be modified. If using `with` syntax, this argument can be omitted.

    Example:
        >>> import omni.replicator.core as rep
        >>> import theory.replicator.helpers as helpers
        >>> cube = rep.create.cube(scale=0.01, position=(0, 0 , 2))
        >>> with cube:
        ...     with rep.utils.sequential():
        ...         rep.physics.rigid_body()
        ...         helpers.modify.write_physics_attribute_float("physxCollision:contactOffset", 0.02)
        ...         helpers.modify.write_physics_attribute_float("physxCollision:restOffset", 0.01)
        theory.replicator.helpers.scripts.modify.write_physics_attribute_float
    """
    node = rep.utils.create_node(
        "theory.replicator.helpers.OgnTheoryWritePhysicsAttributeFloat",
        attribute=name,
        valueFloat=value_float,
    )
    if input_prims:
        rep.utils.set_target_prims(node, "inputs:prims", input_prims)

    return node
