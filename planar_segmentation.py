import pcl

def segment(cloud):

    seg = cloud.make_segmenter_normals(ksearch=50)
    seg.set_optimize_coefficients(True)
    seg.set_model_type(pcl.SACMODEL_NORMAL_PLANE)
    seg.set_method_type(pcl.SAC_RANSAC)
    seg.set_distance_threshold(0.1)
    seg.set_normal_distance_weight(0.01)
    seg.set_max_iterations(100)
    indices, coefficients = seg.segment()

    print('Model inliers: ' + str(len(indices)))
    for i in range(0, len(indices)):
        print(str(indices[i]) + ', x: ' + str(cloud[indices[i]][0]) + ', y : ' + str(cloud[indices[i]][1]) + ', z : ' + str(cloud[indices[i]][2]))

    fil = cloud.make_passthrough_filter()
    fil.set_filter_field_name("z")
    fil.set_filter_limits(0, 1.5)
    cloud_filtered = fil.filter()

    segmented_cloud = cloud_filtered.extract(indices, negative=False)
    return segmented_cloud
