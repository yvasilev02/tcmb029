import os
import logging
import sys

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Debug: Print Python path and check if Mininet is in the path
logger.info(f"Python sys.path: {sys.path}")
try:
    from mininet.net import Mininet
    from mininet.node import RemoteController
    from mininet.cli import CLI
    from mininet.link import TCLink
    from mininet.topo import Topo
    logger.info("Mininet modules imported successfully")
except ImportError as e:
    logger.error(f"Error importing Mininet modules: {e}")
    sys.exit(1)

class CustomTopo(Topo):
    def build(self, num_switches=79, num_hosts=17):
        logger.info(f"Building topology with {num_switches} switches and {num_hosts} hosts")
        
        # Adding switches
        switches = [self.addSwitch(f's{i}') for i in range(num_switches)]
        
        # Adding hosts
        hosts = [self.addHost(f'h{i}') for i in range(num_hosts)]
        
        # Connecting each host to a corresponding switch
        for i in range(num_hosts):
            self.addLink(hosts[i], switches[i], cls=TCLink)
        
        # Connecting switches in a ring topology
        for i in range(num_switches):
            self.addLink(switches[i], switches[(i + 1) % num_switches], cls=TCLink)

def run_network():
    num_switches = int(os.getenv('NUM_SWITCHES', 79))
    num_hosts = int(os.getenv('NUM_HOSTS', 17))

    topo = CustomTopo(num_switches=num_switches, num_hosts=num_hosts)
    
    try:

        logger.info("Starting network")
        controller_ip = os.getenv('CONTROLLER_IP', '127.0.0.1')
        controller_port = int(os.getenv('CONTROLLER_PORT', 6653))
        controller = RemoteController('c0', ip=controller_ip, port=controller_port)
        
        net = Mininet(topo=topo, controller=controller, link=TCLink)
        net.start()
        
        # Basic network testing commands
        logger.info("Testing network connectivity")
        net.pingAll()
        
        # Start CLI for manual testing
        CLI(net)
    
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    
    finally:
        logger.info("Stopping network")
        net.stop()

if __name__ == '__main__':
    run_network()
