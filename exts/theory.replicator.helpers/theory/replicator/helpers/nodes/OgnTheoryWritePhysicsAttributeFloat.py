"""
This is the implementation of the OGN node defined in OgnTheoryWritePhysicsAttribute.ogn
"""

# Array or tuple values are accessed as numpy arrays so you probably need this import
import numpy

import omni.usd
import omni.graph.core as og
import omni.replicator.core as rep


class OgnTheoryWritePhysicsAttributeFloat:
    """
         Write physics attributes.  To be used after write physics node
    """
    @staticmethod
    def compute(db) -> bool:
        """Compute the outputs from the current input"""

        try:
            # With the compute in a try block you can fail the compute by raising an exception
            attribute = db.inputs.attribute
            value_float = db.inputs.valueFloat
            sample_prim_paths = rep.utils.get_node_targets(db.node, "inputs:prims")
            if len(sample_prim_paths):
                stage = omni.usd.get_context().get_stage()
                sample_prims = [stage.GetPrimAtPath(prim_path) for prim_path in sample_prim_paths]
                for prim in sample_prims:
                    prim.GetAttribute(attribute).Set(value_float)

        except Exception as error:
            # If anything causes your compute to fail report the error and return False
            db.log_error(str(error))
            return False

        db.outputs.execOut = og.ExecutionAttributeState.ENABLED
        # Even if inputs were edge cases like empty arrays, correct outputs mean success
        return True
