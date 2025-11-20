suffix "ltop": circuits with number of edges = [50, 100, 250, 500, 750, 1000, 1250, 1500, 1750, 2000]
suffix "htop": circuits with number of edges = [200, 1000, 3000, 5000, 10000, 15000, 20000, 30000]

intersect_ratio_qc_{ltop or htop}.pdf: on average, how many percents of a query circuit's edges are in the capability circuit of the same size.

jaccard_similarity_qc_{ltop or htop}.pdf: the averaged jaccard similarity between a query circuit and a capability circuit.

jaccard_similarity_qq_{ltop or htop}.pdf: the averaged jaccard similarity between two query circuits of a query (e.g., the circuit derived from the original query, and the circuit derived from the paraphrase 1).

edgeNum_{num of edges}_paraNum_{num of paraphrases}/: UpSet plots. Each plot is a randomly selected query's query circuits and the capability circuit's edge overlap.

circuit_plot/: plotted circuits of a query (index=0), containing (1) query circuits by the original query and five of its paraphrases and (2) the capability circuit. Edges and nodes that exist in all these circuits are marked in red (i.e., shared subgraph); otherwise green.