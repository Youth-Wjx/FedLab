import sys
sys.path.append('/home/zengdun/FedLab')
import argparse

from fedlab_core.server.handler import SyncParameterServerHandler
from fedlab_core.models.lenet import LeNet
from fedlab_core.server.topology import ServerBasicTop

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Distbelief training example')

    parser.add_argument('--server_ip', type=str)
    parser.add_argument('--server_port', type=str)
    parser.add_argument('--world_size', type=int)
    args = parser.parse_args()

    model = LeNet().cpu()
    ps = SyncParameterServerHandler(model, client_num_in_total=2)  #client = world_size-1
    top = ServerBasicTop(ps, server_address=(args.server_ip, args.server_port))
    top.run()
