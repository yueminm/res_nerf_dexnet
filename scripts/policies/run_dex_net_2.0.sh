set -e

echo "RUNNING"
# python3 examples/policy.py GQCNN-2.0 --depth_image data/ngp_wrap_ep0100_dex_depth.npy --config_filename cfg/examples/replication/dex-net_2.0.yaml
python3 examples/policy.py GQCNN-2.0 --depth_image data/depth.npy --config_filename cfg/examples/replication/dex-net_2.0.yaml
 