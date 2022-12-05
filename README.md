# ov-helpers
Omniverse Extension with helper functions and nodes

## modify.write_physics_attribute_float
modify.write_physics_attribute_float must be used after rep.physics.rigid_body() and used with rep.utils.sequential.

Replicator nodes are not garanteed to run in an order unless rep.utils.sequential is used.
This has been testing in Code 2022.3.0

This code has not been tested with all physics attributes. These attributes have been tested:
1. physxCollision:contactOffset
2. physxCollision:restOffset

## Sample Code
```
import omni.replicator.core as rep

import theory.replicator.helpers as helpers

with rep.new_layer():
    cube = rep.create.cube(scale=0.01, position=(0, 0 , 2))
    with cube:
        with rep.utils.sequential():
            rep.physics.rigid_body()
            helpers.modify.write_physics_attribute_float("physxCollision:contactOffset", 0.02)
            helpers.modify.write_physics_attribute_float("physxCollision:restOffset", 0.01)

```

# Getting Started

## Add this extension to your *Omniverse App*

1. Fork and clone this repo, for example in `C:\projects\kit-extension-template`
2. In the *Omniverse App* open extension manager: *Window* &rarr; *Extensions*.
3. In the *Extension Manager Window* open a settings page, with a small gear button in the top left bar.
4. In the settings page there is a list of *Extension Search Paths*. Add cloned repo `exts` subfolder.
5. Now you can find `theory.replicator.helpers` extension in the top left search bar. Select and enable it.

# Linking with an *Omniverse* app

For a better developer experience, it is recommended to create a folder link named `app` to the *Omniverse Kit* app installed from *Omniverse Launcher*. A convenience script to use is included.

Run:

```
> link_app.bat --app code
```

# Contributing
The source code for this repository is provided as-is and we are not accepting outside contributions.