This repo contains the files needed to create Volume Renderings in Blender. It also contains the code to extract matplotlib color tables into files.


We need a point distribution to start. From the points we compute local densities using the Delaunay Tessellation Field Estimator method (DTFE) and save densities, positions and tetrahedra (decomposed in triangles) to files.

I added a script to read a Gadget file and produce a numpy file with positions.

The Blender file (blender 2.80+) DelauVolu_vertex_color.blend contains two scripts to load the tessellation and add vertex colors respectively.


