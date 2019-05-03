https://news.ycombinator.com/item?id=18039489	
jules 7 months ago [-]

The CAP theorem has been truly disastrous for databases. The CAP theorem simply says that if you have a database on 2 servers and the connection between those serves goes down, then queries against one server don't see new updates from the other server, so you either have to give up consistency (serve stale data) or give up availability (one of the servers refuses to process further requests). That's all that CAP is, but somehow half the industry has been convinced that slapping a fancy name on this concept is a justification for giving up consistency (even when the network and all servers are fully functional) to retain availability. The A for availability in CAP means that ALL database servers are fully available, which is unnecessary in practice, because clients can switch to the other servers. Giving up consistency introduces big engineering challenges. You're getting something that most people don't need in return for a large cost.

	
Dave_Rosenthal 7 months ago [-]

This is exactly right, and perhaps the most cogent explanation of the CAP theorem on the internet.
For a longer explanation of the same idea which includes a concrete example of how you can get "high availability" in a CP system, see: https://apple.github.io/foundationdb/cap-theorem.html


	
jshen 7 months ago [-]

"The A for availability in CAP means that ALL database servers are fully available"
Is this true? I always thought it meant that clients could continue to read and write to "the database" which could include the client switching to another node. There is nothing in CAP theorem about latency, so switching, even if it adds high latency, is fine by CAP theorem.

This lack of accounting for latency is what makes CAP theorem less useful than a lot of people realize IMO.


	
zzzcpan 7 months ago [-]

From implementation point of view networks are asynchronous and therefore are always partitioned. We don't actually have a luxury of arbitrary CAP interpretations, we can't know whether other nodes are available or not at any given moment. So instead we have to make requests to other nodes and always choose either to wait for responses (or more complex communications to achieve consensus) and get C or not wait for anything and get A, although each node can be a bit behind on updates from other nodes. Thus the CAP choices are pretty much about latency: waiting for globally visible updates vs not waiting and getting low latency. Both can be mixed in various proportions to get consistency with good latency, but still reasonable tolerance of byzantine failures.

	
jules 7 months ago [-]

It is true: if you allow clients to switch then you can have all three C,A,P.

	
zbentley 7 months ago [-]

No, you can't. Say you have two nodes, and a client has just sent a COMMIT to node 1. Then Node 1 gets partitioned away from node 2 and the committing client vanishes. Giving clients the ability to switch to node 2 doesn't help you determine whether node 2 does or does not have the data that was committed (consistency), so you have to choose between CP and AP.

	
jules 7 months ago [-]

You can trivially redirect all clients to node 1 whether or not there is a partition, and voila, you have a CAP system under that definition. If clients can be partitioned from servers then we're back in the original scenario in which switching is not allowed: just partition each client from all but one server (but a different server for each client).
Maybe there is a way to modify the CAP theorem so that it says something non-trivial (e.g. a theorem about the limit of how many node failures a Paxos-like algorithm can handle, but even this is probably trivial, namely half), but the CAP theorem as stated by the originators is trivial, and the proof is a dressed up version of what I stated above. I don't think the authors would disagree with this at all, since they explicitly state:

"The basic idea of the proof is to assume that all messages between G1 and G2 are lost. If a write occurs in G1 and later a read occurs in G2, then the read operation cannot return the results of the earlier write operation."

Isn't it interesting that such a paper has 1600 citations and has reshaped the database industry?


	
rwtxn 7 months ago [-]

> The A for availability in CAP means that ALL database servers are fully available, which is unnecessary in practice, because clients can switch to the other servers.
This assumes that only the servers are partitioned from each other and clients are not partitioned from the majority quorum. This might be rare but it is not impossible at scale.

There is also a latency cost of strict serializability or linearizability which is hard to mitigate at geo-replicated scale.


	
jules 7 months ago [-]

Read latency doesn't have to be impacted by linearizibility. Write latency is higher, but we have to do a fair comparison. If a non-consistent database acknowledges a write it doesn't have to have made that write visible, so comparing that latency to a linearizable DB write is apples to oranges. If we compare latency until the write is globally visible, the non-consistent DB can still do better, so it is definitely possible to imagine scenarios in which such a DB is better.
However, for what percentage of use cases does a reduction in write latency weigh up against the disadvantages? I think that's a very small percentage. Heck, the vast majority of companies that are using a hip highly available NoSQL database cluster would probably be fine running a DB on a single server with a hot standby.

You could image a system that gives you a bit of both. When you do a write, there are several points in time that you may care about, e.g. "the write has entered the system, and will eventually be visible to all clients" and "the write is visible to all clients". The database could communicate that information (asynchronously) to the client that's doing the write, so that this client can update the UI appropriately. When a client does a read, it could specify what level of guarantee it wants for the read: "give me the most recent data, regardless of whether the write has been committed" or "only give me data that is guaranteed to have been committed". Such a system could theoretically give you low latency or consistency on a case by case basis.


	
gowld 7 months ago [-]

You can't always "choose another server" while maintaining low latency operations.

	
zzzcpan 7 months ago [-]

> slapping a fancy name on this concept is a justification for giving up consistency (even when the network and all servers are fully functional) to retain availability
This is a misconception. AP databases are not supposed to give up consistency, just not wait for all nodes to see updates. That's it. Consistency is still there, nodes resync, users always see their own updates and all that.


	
jules 7 months ago [-]

Consistency in the CAP sense has a precise meaning: all reads see all completed writes. That is, if the database has told some client that their write succeeded, then it is not allowed to still serve other clients the old data.
Inconsistency in the CAP sense may also cause inconsistency in the sense that you mean, for instance if two transactions are simultaneously accepted, but each transaction violates the precondition of the other. In a consistent database one of the transactions will see the result of the other transaction and fail, whereas a DB without consistency may accept both transactions and end up in a semantically incorrect state.


	
he0001 7 months ago [-]

So then its CAP not AP? CAP was about you can’t have them all?

	
zzzcpan 7 months ago [-]

No, it's still AP, it's just CAP consistency is very specific thing and you can't generalize it into "giving up consistency". AP systems don't give up consistency, they just don't explicitly wait for it.

	
he0001 7 months ago [-]

Then you are saying that all the trouble Spanner goes through to actually be consistent is not needed? And by saying a AP system can be “consistent” there’s no need for a product as Spanner. Consistency is obviously a timing problem. Something that is not consistent at some time will not be consistent since it will be inconsistent at that time.

	
almostdeadguy 7 months ago [-]

CAP consistency is linearizability, so if what you mean is there are other models of consistency available to "AP systems" (kind of hate the framing that these are binary features of a distributed system rather than a huge space of design choices, but anyways), then yes that's true. But AP systems don't always guarantee things like read-your-own-write consistency models, and not all conflicts that occur during a partition can be resolved in many of these databases.

	
zzzcpan 7 months ago [-]

Sure. But it's kind of is a huge space of design choices (https://jepsen.io/consistency), so it's not ok to claim you give up consistency with any of them.

	
glic3rinu 7 months ago [-]

The C in there is for "Strong Consistency"; CAP allows for lessers forms of consistency, like "Eventual Consistency", without giving up on Availability.

	
he0001 7 months ago [-]

Well yes but that’s not what we are talking about here. And “eventual consistency” is not “consistency”. And I would argue that “eventual consistency” is not consistent since it can result in fake states since it’s not consistent.
