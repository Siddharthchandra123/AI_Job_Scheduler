from simulator.state.cluster_state import ClusterState
from simulator.state.node_state import NodeState


class ClusterStateBuilder:

    @staticmethod
    def build(cluster):

        state = ClusterState(

            cluster_id=cluster.cluster_id

        )

        for node in cluster.nodes:

            node_state = NodeState(

                node_id=node.node_id,

                total_cpu=node.cpu_cores,

                total_ram=node.ram_gb,

                total_gpu=node.gpu_count

            )

            state.nodes[node.node_id] = node_state

        return state
