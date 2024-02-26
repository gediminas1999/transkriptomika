import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pysam import VariantFile

input_file = snakemake.input[0]  
output_file = snakemake.output[0] 

quals = [record.qual for record in VariantFile(input_file)]
plt.hist(quals)

plt.savefig(output_file)

