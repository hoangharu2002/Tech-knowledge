# 1. Leader-follower (Primary Replica)
* Probably the most common strategy
* Principle: A query is written to a single designated leader, then leader fowards to followers. And both leader and followers have to commit before right successful.
* Synchronization: when a follower gets fail and goes down, the whole system has to wait until the considered right successful => this will raise latency => asynchronous replication for solution (option) where transaction speed is more important than consistency
* Asynchronization: the leader feeds back immediately to clients without waiting for the followers => if leader goes down and the most up-to-date data is lost => replica is promoted to be the leader and takes over
