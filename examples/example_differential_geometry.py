import slam.io as sio
import slam.differential_geometry as sdg
import slam.plot as splt

if __name__ == '__main__':
    mesh = sio.load_mesh('data/example_mesh.gii')
    tex = sio.load_texture('data/example_texture.gii')

    triangle_grad = sdg.triangle_gradient(mesh, tex.darray[0])
    print(triangle_grad)
    grad = sdg.gradient(mesh, tex.darray[0])
    print(grad.values)
    norm_grad = sdg.norm_gradient(mesh, tex.darray[0])
    print(norm_grad)
    visb_sc = splt.visbrain_plot(mesh=mesh, tex=tex.darray[0],
                                 caption='mesh with curvature',
                                 cblabel='curvature')
    visb_sc = splt.visbrain_plot(mesh=mesh, tex=norm_grad,
                                 caption='norm of the gradient of curvature',
                                 cblabel='gradient magnitude', visb_sc=visb_sc)
    visb_sc.preview()

    lap, lap_b = sdg.compute_mesh_laplacian(mesh, lap_type='fem')
    print(mesh.vertices.shape)
    print(lap.shape)
    lap, lap_b = sdg.compute_mesh_laplacian(mesh, lap_type='conformal')
    lap, lap_b = sdg.compute_mesh_laplacian(mesh, lap_type='meanvalue')
    lap, lap_b = sdg.compute_mesh_laplacian(mesh, lap_type='authalic')

    s_mesh = sdg.laplacian_mesh_smoothing(mesh, nb_iter=10, dt=0.1)
    # import slam.plot as splt
    # splt.pyglet_plot(mesh, lap[:, 0].todense().squeeze())
