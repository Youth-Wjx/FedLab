
from fedlab_core.server.pshandler import SyncSGDParameterServerHandler
from fedlab_core.models.lenet import LeNet
from fedlab_core.server.topology import ServerTop

if __name__ == "__main__":
    model = LeNet().cpu()
    ps = SyncSGDParameterServerHandler(model, client_num=2)
    top = ServerTop(ps, server_addr=('127.0.0.1', '3001'), args=None)
    top.run()
