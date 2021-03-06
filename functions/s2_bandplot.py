"""
Function for plotting all bands except the sen2cor scene classification (scl)
and the not Level 2A included cirrus band.
Usage : s2_bandplot(dataset, timestep)
            dataset: xarray with BDC preprocessed Sentinel-2 tiles
            timestep: integer variable, starting with 0, ending with the last dataset entry
"""



def s2_bandplot(dataset, timestep):
    #subplot(r,c) provide the no. of rows and columns
    fig, axes = plt.subplots(3,4, figsize=(24,12), sharex = True, sharey = True) 

    # use the created array to output your multiple images. In this case I have stacked 4 images vertically
    axes[0,0].axis('off')
    plt.sca(axes[0,0])
    plt.imshow(dataset.isel(time=timestep).coastal_aerosol, cmap='viridis')
    plt.title('coastal_aerosol')
    #plt.xlabel('Spalte')
    #plt.ylabel('Zeile')
    clb = plt.colorbar(shrink=0.8, extend='both')
    clb.set_label('Reflectance', labelpad=20, y=.5, rotation=-90)
    fig.suptitle('Aquisition Date: ' + np.datetime_as_string(liste.values).split('T')[0], fontsize=20)

    plt.sca(axes[0,1])
    axes[0,1].axis('off')
    plt.imshow(dataset.isel(time=timestep).blue, cmap='viridis')
    plt.title('blue')
    #plt.xlabel('Spalte')
    #plt.ylabel('Zeile')
    clb = plt.colorbar(shrink=0.8, extend='both')
    clb.set_label('Reflectance', labelpad=20, y=.5, rotation=-90)

    plt.sca(axes[0,2])
    axes[0,2].axis('off')
    plt.imshow(dataset.isel(time=timestep).green, cmap='viridis')
    plt.title('green')
    #plt.xlabel('Spalte')
    #plt.ylabel('Zeile')
    clb = plt.colorbar(shrink=0.8, extend='both')
    clb.set_label('Reflectance', labelpad=20, y=.5, rotation=-90)

    plt.sca(axes[0,3])
    axes[0,3].axis('off')
    plt.imshow(dataset.isel(time=timestep).red, cmap='viridis')
    plt.title('red')
    #plt.xlabel('Spalte')
    #plt.ylabel('Zeile')
    clb = plt.colorbar(shrink=0.8, extend='both')
    clb.set_label('Reflectance', labelpad=20, y=.5, rotation=-90)

    #####################################################################################
    # use the created array to output your multiple images. In this case I have stacked 4 images vertically
    axes[1,0].axis('off')
    plt.sca(axes[1,0])
    plt.imshow(dataset.isel(time=timestep).red_edge1, cmap='viridis')
    plt.title('red_edge1')
    #plt.xlabel('Spalte')
    #plt.ylabel('Zeile')
    clb = plt.colorbar(shrink=0.8, extend='both')
    clb.set_label('Reflectance', labelpad=20, y=.5, rotation=-90)

    plt.sca(axes[1,1])
    axes[1,1].axis('off')
    plt.imshow(dataset.isel(time=timestep).red_edge2, cmap='viridis')
    plt.title('red_edge2')
    #plt.xlabel('Spalte')
    #plt.ylabel('Zeile')
    clb = plt.colorbar(shrink=0.8, extend='both')
    clb.set_label('Reflectance', labelpad=20, y=.5, rotation=-90)

    plt.sca(axes[1,2])
    axes[1,2].axis('off')
    plt.imshow(dataset.isel(time=timestep).red_edge3, cmap='viridis')
    plt.title('red_edge3')
    #plt.xlabel('Spalte')
    #plt.ylabel('Zeile')
    clb = plt.colorbar(shrink=0.8, extend='both')
    clb.set_label('Reflectance', labelpad=20, y=.5, rotation=-90)

    plt.sca(axes[1,3])
    axes[1,3].axis('off')
    plt.imshow(dataset.isel(time=timestep).nir, cmap='viridis')
    plt.title('nir')
    #plt.xlabel('Spalte')
    #plt.ylabel('Zeile')
    clb = plt.colorbar(shrink=0.8, extend='both')
    clb.set_label('Reflectance', labelpad=20, y=.5, rotation=-90)
    #####################################################################################
    # use the created array to output your multiple images. In this case I have stacked 4 images vertically
    axes[1,0].axis('off')
    plt.sca(axes[2,0])
    plt.imshow(dataset.isel(time=timestep).narrow_nir, cmap='viridis')
    plt.title('narrow_nir')
    #plt.xlabel('Spalte')
    #plt.ylabel('Zeile')
    clb = plt.colorbar(shrink=0.8, extend='both')
    clb.set_label('Reflectance', labelpad=20, y=.5, rotation=-90)

    plt.sca(axes[2,1])
    axes[1,1].axis('off')
    plt.imshow(dataset.isel(time=timestep).water_vapour, cmap='viridis')
    plt.title('water_vapour')
    #plt.xlabel('Spalte')
    #plt.ylabel('Zeile')
    clb = plt.colorbar(shrink=0.8, extend='both')
    clb.set_label('Reflectance', labelpad=20, y=.5, rotation=-90)

    plt.sca(axes[2,2])
    axes[1,2].axis('off')
    plt.imshow(dataset.isel(time=timestep).swir1, cmap='viridis')
    plt.title('swir1')
    #plt.xlabel('Spalte')
    #plt.ylabel('Zeile')
    clb = plt.colorbar(shrink=0.8, extend='both')
    clb.set_label('Reflectance', labelpad=20, y=.5, rotation=-90)

    plt.sca(axes[2,3])
    axes[1,3].axis('off')
    plt.imshow(dataset.isel(time=timestep).swir2, cmap='viridis')
    plt.title('swir2')
    #plt.xlabel('Spalte')
    #plt.ylabel('Zeile')
    clb = plt.colorbar(shrink=0.8, extend='both')
    clb.set_label('Reflectance', labelpad=20, y=.5, rotation=-90)
