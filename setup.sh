conda create -f environment.yaml -y
echo "Downloading Carla sim"
wget https://tiny.carla.org/carla-0-9-10-1-linux -O carla.tar.gz
mkdir -p third_party/CARLA_0.9.10/
tar -xzf carla.tar.gz -C third_party/CARLA_0.9.10/
rm carla.tar.gz
echo "Downloading Habitat PointNav Gibson Data"
wget https://dl.fbaipublicfiles.com/habitat/data/datasets/pointnav/gibson/v1/pointnav_gibson_v1.zip -O pointnav_gibson.zip
mkdir -p data/datasets/pointnav/gibson/v1/
unzip pointnav_gibson.zip -d data/datasets/pointnav/gibson/v1/
rm pointnav_gibson.zip
echo "Done!"