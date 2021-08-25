========
pyvislam
========

Python implementation of visual-inertial SLAM

* Developer
    * Youmin Ha <youmin78.ha@gmail.com>

* License
    * Free software: GNU General Public License v3
    * For commercial use, please contact to youmin78.ha@gmail.com

* Documentation: https://github.com/youminha/pyvislam

------------
Requirements
------------
* opencv python
* GTSAM python (pip3 install gtsam)

---------
Structure
---------
* Feature : Visual or depth feature.
* Landmark: Feature remembered and managed by SLAM system.
* Frame : Image
* PoseTransformer : 3d pose transformer
* PoseExtrapolator : Pose should be interpolated/extrapolated, because the timestamps between IMU and camera frames are not exactly matched. PoseExtrapolator works for it.

--------
Features
--------
DONE
====
* Feature detection

TODO
====
* Mono camera
* Feature matching
* Sensor(camera/IMU) extrinsic/intrinsic config
* IMU preintegration
* Local graph optimization
* Global graph optimization
* Mapping : save/load maps
* Relocalization : Find a current pose in given map
* Stereo camera
* RGB-D camera
* Multiple trajectory merging in a map

