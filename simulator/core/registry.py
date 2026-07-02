"""
Global registry.

Stores every object created during simulation.
"""

from dataclasses import dataclass, field


@dataclass
class Registry:

    jobs: dict = field(default_factory=dict)

    users: dict = field(default_factory=dict)

    accounts: dict = field(default_factory=dict)

    clusters: dict = field(default_factory=dict)

    nodes: dict = field(default_factory=dict)

    gpus: dict = field(default_factory=dict)

    # ----------------------------

    def add_job(self, job):

        self.jobs[job.job_id] = job

    def get_job(self, job_id):

        return self.jobs.get(job_id)

    # ----------------------------

    def add_user(self, user):

        self.users[user.user_id] = user

    def get_user(self, user_id):

        return self.users.get(user_id)

    # ----------------------------

    def add_cluster(self, cluster):

        self.clusters[cluster.cluster_id] = cluster

    def get_cluster(self, cluster_id):

        return self.clusters.get(cluster_id)

    # ----------------------------

    def summary(self):

        return {

            "jobs": len(self.jobs),

            "users": len(self.users),

            "clusters": len(self.clusters),

            "nodes": len(self.nodes),

            "gpus": len(self.gpus)

        }
    def add_account(self, account):

         self.accounts[account.account_id] = account


    def get_account(self, account_id):

         return self.accounts.get(account_id)
