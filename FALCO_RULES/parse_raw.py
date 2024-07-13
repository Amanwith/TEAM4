import pandas as pd


df = pd.read_csv("01_FALCO_SYSCALL_RAW.tsv", delimiter="\t")


# filtering
res = []

for i, val in enumerate(df.values):
    val = val.tolist()
    params = val[-1]

    if not isinstance(params, str):
        continue

    if ("FSPATH" in params) or ("FD" in params) or ("PID" in params):
        res.append(val)


# saving
with open("02_FALCO_SYSCALL_FILTERED.tsv", "w") as f:
    for elem in res:
        f.write("\t".join(elem)+"\n")
