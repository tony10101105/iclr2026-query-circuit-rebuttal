# iclr2026-query-circuit-rebuttal

## This repo contains 5 sets of additional experimental results, each organized in a folder:

**Edge_Pruning_on_IOI/**: Contains experiments to show and analyze why optimization-based circuit discovery methods tend to fail on the setting of query circuit.

**gpt2-xl_and_llama-3-8b/**: Contains experiments on three datasets with target model as GPT2-XL and Llama-3-8B-Instruct to show the generalizability of our methods.

**more_circuit_analysis/**: Contains experiments on fine-grained analysis on and demonstration of the relationship (1) between query and capability circuits and (2) among query circuits.

**rephrase_whole_queries/**: Contains experiments on three datasets with target model as Llama-3.2-1B-Instruct to show the performance of our methods and baselines when rephrasing is done on the whole query instead of only the question stem.

**nfs_and_ndf_on_query_and_paraphrases/**: NFS and NDF on the query circuit discovered by the original query and its paraphrases.
